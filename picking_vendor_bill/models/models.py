from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vendor_bill_ids = fields.Many2many(
        'account.move',
        string="Vendor Bills",
        readonly=True,
        domain=[('move_type', '=', 'in_invoice')]
    )

    invoice_count = fields.Integer(
        string="Vendor Bill Count",
        compute="_compute_invoice_count",
        store=True,
    )

    @api.depends('vendor_bill_ids')
    def _compute_invoice_count(self):
        for picking in self:
            picking.invoice_count = len(picking.vendor_bill_ids)

    def action_view_invoice(self):
        if self.vendor_bill_ids:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Vendor Bills',
                'res_model': 'account.move',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.vendor_bill_ids.ids)],
                'target': 'current',
            }


