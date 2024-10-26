from odoo import models, fields, api

class SaleOrderAddProductWizard(models.TransientModel):
    _name = 'sale.order.add.product.wizard'
    _description = 'Wizard to Add Products to Sale Order'

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True)
    product_ids = fields.Many2many('product.product', string='Products')
    line_ids = fields.One2many('sale.order.wizard.line', 'wizard_id', string='Order Lines')

    def action_add_products(self):
        sale_order = self.order_id
        for product in self.product_ids:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': product.id,
                'product_uom_qty': 1,
                'price_unit': product.lst_price,
            })
        return {'type': 'ir.actions.act_window_close'}

    @api.onchange('product_ids')
    def _onchange_product_id(self):
        line_values = [(0, 0, {
            'product_id': product.id,
            'product_uom_qty': 1,
            'price_unit': product.lst_price,
        }) for product in self.product_ids]
        self.line_ids = line_values
        print('onchange......', line_values)

class SaleOrderWizardLine(models.TransientModel):
    _name = 'sale.order.wizard.line'
    _description = 'Sale Order Line Wizard Line'

    wizard_id = fields.Many2one('sale.order.add.product.wizard', string='Wizard Reference')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_uom_qty = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(string='Unit Price')
