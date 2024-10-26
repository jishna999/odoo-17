# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    select = fields.Boolean(string='Select',default=False)
