from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    invoice_count = fields.Integer(
        string="Vendor Bill Count",
        related='purchase_id.invoice_count',
        store=True,
    )

    def action_view_invoice(self):
        if self.purchase_id:
            res = self.purchase_id.action_view_invoice()
            return res
