from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one(
        related='order_line.sale_line_id.order_id',
        string="Sale Order",
        readonly=True
    )
