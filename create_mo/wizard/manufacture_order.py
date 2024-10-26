# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError



class ManufactureOrd(models.TransientModel):
    _name = 'manufacture.order'
    _description = "Wizard for creating manufacture order from bom"

    mrp_id = fields.Many2one(
        'mrp.bom', default=lambda self: self.env.context.get('active_id'))
    product_id = fields.Many2one(comodel_name='product.template',related='mrp_id.product_tmpl_id')
    mrp_line_ids = fields.One2many(comodel_name='manufacture.order.line',inverse_name='line_id',string='Wizard line')

    def create_manufacture_order(self):
        bom = self.mrp_id
        for line in self.mrp_line_ids:
            if line.product_quantity <= 0:
                raise UserError(f"Invalid quantity for product {bom.product_id.name}.")

            mo_value = {
                'bom_id': bom.id,
                'product_qty': line.product_quantity,
                'date_start': line.scheduled_date,
                'user_id': line.user_id.id
            }
            manufacturing_order = self.env['mrp.production'].create(mo_value)
            manufacturing_order.action_confirm()

class ManufactureOrdLine(models.TransientModel):
    _name='manufacture.order.line'
    _description = 'Wizard to fill the details to MO'

    line_id = fields.Many2one(comodel_name='manufacture.order')
    user_id = fields.Many2one(comodel_name='res.users', string="Responsible user ")
    product_quantity = fields.Float(string="Quantity")
    scheduled_date = fields.Datetime(string="Scheduled date")
