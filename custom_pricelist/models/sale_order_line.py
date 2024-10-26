from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty', 'product_id', 'order_id')
    def _onchange_product_uom_qty(self):
        for line in self:
            if line.product_id and line.product_uom_qty and line.order_id:
                pricelist = line.order_id.pricelist_id

                pricelist_item = pricelist.item_ids.filtered(
                    lambda item: line.product_id in item.product_variant_ids and item.compute_price == 'tiered'
                )
                if pricelist_item:
                    tiered_price = self._get_tiered_price(pricelist_item, line.product_uom_qty)
                    line.price_unit = tiered_price
                else:
                    line.price_unit = line.product_id.lst_price

    def _get_tiered_price(self, pricelist_item, quantity):

        tiered_price = 0.0
        for tier in pricelist_item.tiers_ids:
            if tier.tier_from <= quantity <= tier.tier_to:
                tiered_price = tier.list_price
                break

        return tiered_price