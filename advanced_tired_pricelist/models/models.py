from odoo import models, fields

class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    compute_price = fields.Selection(
        selection_add=[('tiered', 'Tiered')],
        ondelete={'tiered': 'cascade'}
    )
    product_id = fields.Many2one(comodel_name='product.product', string='Product Variant')
    tiered_ids = fields.One2many(comodel_name='tiered.price.list', inverse_name='price_list_item_id', string='Tiered Price List')


class TieredPriceList(models.Model):
    _name = 'tiered.price.list'
    _description = 'All tiered values of particular price list'

    price_list_item_id = fields.Many2one(comodel_name='product.pricelist.item', string='Price List Item')
    min_quantity = fields.Float(string='Minimum Quantity', default=0.0)
    max_quantity = fields.Float(string='Maximum Quantity', default=0.0)
    currency_id = fields.Many2one('res.currency', string="Currency")
    sale_price = fields.Monetary(string="Sale Price", currency_field='currency_id')

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty', 'product_id', 'order_id')
    def _onchange_product_uom_qty(self):
        for line in self:
            if line.product_id and line.product_uom_qty and line.order_id:
                pricelist = line.order_id.pricelist_id

                pricelist_item = pricelist.item_ids.filtered(
                    lambda item: line.product_id in item.product_id and item.compute_price == 'tiered'
                )
                if pricelist_item:
                    tiered_price = self._get_tiered_price(pricelist_item, line.product_uom_qty)
                    line.price_unit = tiered_price
                else:
                    line.price_unit = line.product_id.lst_price

    def _get_tiered_price(self, pricelist_item, quantity):

        tiered_price = 0.0
        for tier in pricelist_item.tiered_ids:
            if tier.min_quantity <= quantity <= tier.max_quantity:
                tiered_price = tier.sale_price
                break

        return tiered_price
