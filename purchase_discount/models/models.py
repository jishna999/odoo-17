# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order.line'

    discount_on_purchase =fields.Float(string='Fixed discount amount')
