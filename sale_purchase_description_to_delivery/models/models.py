# -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()

        for picking in self.picking_ids:
            for move in picking.move_ids:
                sale_order_line = self.order_line.filtered(lambda line: line.product_id == move.product_id)
                if sale_order_line:
                    move.description_picking = sale_order_line.name
        return res



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()

        for picking in self.picking_ids:
            for move in picking.move_ids:
                purchase_order_line = self.order_line.filtered(lambda line: line.product_id == move.product_id)
                if purchase_order_line:
                    move.description_picking = purchase_order_line.name
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    def _compute_name(self):
        pass




