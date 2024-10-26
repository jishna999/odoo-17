from odoo import models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_create_picking(self):
        for invoice in self:
            if invoice.state == 'posted':
                picking_vals = {
                    'origin': invoice.name,
                    'picking_type_id': self.env.ref('stock.picking_type_out').id,  # Example picking type
                    'partner_id': invoice.partner_id.id,
                    'location_dest_id': 1,  # Adjust based on your needs
                    'move_type': 'direct',  # Use valid move_type value ('direct', 'one', or 'two')
                    'move_line_ids': [],
                }
                picking = self.env['stock.picking'].create(picking_vals)
                return picking
