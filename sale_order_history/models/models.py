from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_order_history_ids = fields.One2many(
        comodel_name='sale.order.history',
        inverse_name='order_id',
        string='Sale Order History'
    )

    @api.onchange('partner_id')
    def _onchange_partner_id_sale_order_history(self):
        self.sale_order_history_ids = [(5, 0, 0)]

        if self.partner_id:
            domain = [('partner_id', '=', self.partner_id.id), ('state', 'in', ['sale', 'done'])]
            if self.id:
                domain.append(('id', '!=', self.id))

            unique_products = set()

            for order in self.env['sale.order'].search(domain):
                for line in order.order_line:
                    if line.product_id.id not in unique_products:
                        self.sale_order_history_ids = [(0, 0, {
                            'order_id': order.id,
                            'product_id': line.product_id.id,
                            'product_uom_qty': line.product_uom_qty,
                            'price_unit': line.price_unit,
                        })]
                        unique_products.add(line.product_id.id)
    def action_reorder(self):
        """ Recreate a sale order based on the selected history item. """
        for history in self:
            order_lines = [(0, 0, {
                'product_id': history.product_id.id,
                'product_uom_qty': history.product_uom_qty,
                'price_unit': history.price_unit,
            })]

            new_order = self.env['sale.order'].create({
                'partner_id': history.order_id.partner_id.id,
                'order_line': order_lines,
            })

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'res_id': new_order.id,
                'view_mode': 'form',
                'target': 'current',
            }

class SaleOrderHistory(models.Model):
    _name = 'sale.order.history'
    _description = 'Sale Order History'

    order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Order',
        required=True,
        ondelete='cascade'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product'
    )

    product_uom_qty = fields.Float(string='Quantity')

    price_unit = fields.Float(string='Unit Price')

    def action_reorder(self):
        """ Recreate a sale order based on the selected history item. """
        for history in self:
            order_lines = [(0, 0, {
                'product_id': history.product_id.id,
                'product_uom_qty': history.product_uom_qty,
                'price_unit': history.price_unit,
            })]

            new_order = self.env['sale.order'].create({
                'partner_id': history.order_id.partner_id.id,  # Assuming same partner
                'order_line': order_lines,
            })

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'res_id': new_order.id,
                'view_mode': 'form',
                'target': 'current',
            }



