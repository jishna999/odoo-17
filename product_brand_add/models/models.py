# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char(string="Brand Name")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(comodel_name='product.brand', string='Product Brand')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Many2one(
        comodel_name='product.brand',
        related='product_template_id.brand_id',
        string='Brand',
        store=True
    )



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                for move in line.move_ids:
                    move.brand_name = line.brand_name
        return res

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super(SaleOrder, self)._create_invoices(final=final, grouped=grouped)
        for order in self:
            for order_line in order.order_line:
                for move_line in order_line.invoice_lines:
                    move_line.brand_name = order_line.brand_name

        return res


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    brand_name = fields.Many2one(comodel_name='product.brand', string='Brand')




class StockMove(models.Model):
    _inherit = 'stock.move'

    brand_name = fields.Many2one(comodel_name='product.brand', string='Brand')
