# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'


    select = fields.Boolean(string='Select',default=False)
