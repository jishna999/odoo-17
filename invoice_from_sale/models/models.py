# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class invoice_from_sale(models.Model):
#     _name = 'invoice_from_sale.invoice_from_sale'
#     _description = 'invoice_from_sale.invoice_from_sale'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

