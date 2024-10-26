from odoo import models, fields, api

class RegisterPayment(models.TransientModel):
    _name = 'picking.vendor.bill'
    _description = 'Wizard for Vendor Bill from Picking'

    picking_id = fields.Many2one(comodel_name='stock.picking', string='Picking')
    bill_date = fields.Date(string="Bill Date", required=True)
    journal_id = fields.Many2one('account.journal', string='Journal', required=True)

    @api.model
    def default_get(self, fields_list):
        res = super(RegisterPayment, self).default_get(fields_list)
        picking_id = self._context.get('default_picking_id')
        if picking_id:
            res.update({
                'picking_id': picking_id,
            })
        return res

    def action_create_vendor_bill(self):
        picking = self.picking_id
        purchase_order = picking.purchase_id

        invoice_lines = []

        for move in picking.move_ids:
            if move.state == 'done':
                line_vals = {
                    'product_id': move.product_id.id,
                    'quantity': move.product_uom_qty,
                    'purchase_line_id': move.purchase_line_id.id,
                    'price_unit': move.purchase_line_id.price_unit,
                }
                invoice_lines.append((0, 0, line_vals))

        if invoice_lines:
            bill_vals = {
                'move_type': 'in_invoice',
                'partner_id': purchase_order.partner_id.id,
                'invoice_date': self.bill_date,
                'invoice_origin': f"{purchase_order.name}, {picking.name}",
                'ref': picking.name,
                'journal_id': self.journal_id.id,
                'invoice_line_ids': invoice_lines,
            }

            created_bill = self.env['account.move'].create(bill_vals)
            created_bill.action_post()

            picking.write({'vendor_bill_ids': [(4, created_bill.id)]})

            return [created_bill.id]

        return []
