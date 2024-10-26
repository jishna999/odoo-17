from odoo import models, fields, api

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    def action_create_manufacture(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mrp.manufacture',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_mrp_bill_of_materials_id': self.id,
            },
        }