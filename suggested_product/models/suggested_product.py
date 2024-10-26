from odoo import models, fields, api


class SuggestedProduct(models.Model):
    _name = 'suggested.product'
    _description = 'Description of the suggested product model'

    order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        domain="[('sale_ok', '=', True)]",

    )

    total_amount = fields.Monetary(
        string="Total",
        compute='_compute_total_amount',
        store=True,
        currency_field='currency_id'
    )
    product_uom_qty = fields.Float(string='Quantity')
    sale_price = fields.Float(string='Sale Price')

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string="Currency",
        related='order_id.currency_id',
        store=True
    )

    @api.onchange('product_id')
    def onchange_product_sale_price(self):
        if self.product_id:
            self.sale_price = self.product_id.list_price
        else:
            self.sale_price = 0.0

    @api.depends('product_uom_qty', 'sale_price')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.product_uom_qty * record.sale_price

