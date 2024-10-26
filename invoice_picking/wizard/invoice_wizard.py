from odoo import models,fields,api
class InvoiceWizard(models.TransientModel):
    _name = 'create.invoice.wizard'
    _description = "wizard to invoice picking"

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", required=True)
    picking_id = fields.Many2one('stock.picking', string="picking invoice", required=True)
    journal_id = fields.Many2one('account.journal', string="journal")
    invoice_date = fields.Many2one( string="invoice date", required=True)

    def action_create_invoice(self):
       sale_order = self.sale_id
       return {
         'type': 'ir.actions.act_window',
         'res_model': 'account.move',
         'view_mode': 'form',
         'res_id': 'invoice.id',
     }
