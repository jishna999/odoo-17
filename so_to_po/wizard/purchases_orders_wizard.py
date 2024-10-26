from odoo import models, fields, api

class CreatePurchaseOrderWizard(models.TransientModel):
    _name = 'create.purchase.order.wizard'
    _description = 'Wizard to Create Purchase Orders from Sale Order'

    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    scheduled_date = fields.Date(string="Scheduled Date", required=True)
    sale_order_id = fields.Many2one('sale.order',default=lambda self: self.env.context.get('active_id'), string="Sale Order", required=True)
    sale_order_line_ids = fields.Many2many(
        'sale.order.line',
        string="Sale Order Lines",
        required=True,
        default=lambda self: [(6, 0, self.env['sale.order'].browse(
            self.env.context.get('active_id')).order_line.ids)]
    )

    @api.onchange('vendor_id')
    def _onchange_vendor_id(self):
        if not self.vendor_id:
            return

        for line in self.sale_order_line_ids:
            supplier_info = self.env['product.supplierinfo'].search([
                ('partner_id', '=', self.vendor_id.id),
                ('product_tmpl_id', '=', line.product_id.product_tmpl_id.id),
            ], limit=1)

            line.price_unit = supplier_info.price if supplier_info else line.price_unit

    def create_purchase_orders(self):
        sale_order = self.sale_order_id


        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.vendor_id.id,
            'sale_order_id': sale_order.id,
            'date_planned': self.scheduled_date,
        })

        for line in self.sale_order_line_ids:
            self.env['purchase.order.line'].create({
                'order_id': purchase_order.id,
                'product_id': line.product_id.id,
                'name': line.name,
                'product_qty': line.product_uom_qty,
                'price_unit': line.price_unit,
            })

        self.sale_order_line_ids.write({
            'purchase_line_ids': [(4, line_id) for line_id in purchase_order.order_line.ids]
        })

        return {'type': 'ir.actions.act_window_close'}
