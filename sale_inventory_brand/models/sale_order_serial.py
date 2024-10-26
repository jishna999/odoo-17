from odoo import models, fields, api


class SaleOrderSerial(models.Model):
    _inherit = 'sale.order'

    stock_reference = fields.Char(string='Stock Reference')

    def action_confirm(self):
        res = super(SaleOrderSerial, self).action_confirm()

        for picking in self.picking_ids:
            picking.stock_reference = self.stock_reference

        sale_order_lines = self.mapped('order_line')  # one2many from sale order to sale.order.line

        for line in sale_order_lines:
            stock_moves = self.env['stock.move'].search([('sale_line_id', '=', line.id)])
            for move in stock_moves:
                move.lots_id = line.serial_no_id
                move.serial_ids = line.serial_ids
                move.product_brand_id = line.product_brand_id

            stock_moves.picking_ids.write({'product_brand_id': stock_moves.order_line.mapped('product_brand_id').id})

        for move in self.mapped('order_line.move_ids'):
            for move_line in move.move_line_ids:
                move_line.lots_id = move.lots_id
                move_line.serial_ids = move.serial_ids

        return res

    def _create_invoices(self):
        result = super(SaleOrderSerial, self)._create_invoices()
        sale_order_lines = self.mapped('order_line')
        for line in sale_order_lines:
            account_moves = self.env['account.move.line'].search([('sale_line_ids', '=', line.id)])
            for account_move in account_moves:
                if line.product_brand_id:
                    account_move.product_brand = line.product_brand_id

        return result


class SaleOrderSerialLine(models.Model):
    _inherit = 'sale.order.line'

    serial_no_id = fields.Many2one(comodel_name='stock.lot', string="Serial Number",
                                   domain="[('product_id', '=', product_id)]")
    serial_ids = fields.Many2many(comodel_name='stock.lot', string="Serial Numbers",
                                  domain="[('product_id', '=', product_id)]")
