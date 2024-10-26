from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order'



    def add_product(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Products',
            'res_model': 'sale.order.add.product.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id

            },
        }