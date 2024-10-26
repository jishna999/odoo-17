from datetime import timedelta

from odoo import fields,models,api


class MrpManufactureLine(models.TransientModel):
    _name = 'mrp.manufacture.line'
    _description = 'Wizard Line for Creating Manufacture'

    manufacture_id = fields.Many2one(
        'mrp.manufacture',
        string='Manufacture',
        readonly=True,
        ondelete='cascade'
    )

    product_qty = fields.Float(string='Product Quantity', required=True)
    date_start = fields.Datetime(string='Scheduled Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Responsible User', required=True)
