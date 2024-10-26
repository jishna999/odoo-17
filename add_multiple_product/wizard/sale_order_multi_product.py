from odoo import models, fields, api

class AddMultipleProduct(models.TransientModel):
    _name = 'sale.order.multi.product'
    _description = 'Add Multiple Products to Sale Order'

    sale_order_id = fields.Many2one(
        'sale.order',
        string='Sale Order',
        default=lambda self: self.env.context.get('active_id'),
        required=True
    )
    
    product_ids = fields.Many2many(
        'product.product',
        string="Available Products",
        required=True
    )

    @api.onchange('sale_order_id')
    def _onchange_product_id(self):
        if self.sale_order_id:
            all_products = self.env['product.product'].search([('sale_ok', '=', True)])
            self.product_ids = all_products

    def action_add_product(self):
        selected_products = self.product_ids.filtered(lambda p: p.select)

        if not self.sale_order_id or not selected_products:
            return

        for product in selected_products:
            self.env['sale.order.line'].create({
                'order_id': self.sale_order_id.id,
                'product_id': product.id,
                'product_uom_qty': 1.0,
                'price_unit': product.lst_price,
            })

        selected_products.write({'select': True})
