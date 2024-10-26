from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_name_with_brand = fields.Char(string='Product Brand', related='product_id.brand_id.name')
