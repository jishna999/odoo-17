from odoo import models, fields, api, _
import logging
from datetime import  timedelta
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_history_ids = fields.One2many(
        comodel_name='order.history',
        inverse_name='order_id',
        string='Order History'
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if not self.partner_id:
            return
        _logger.info("Partner ID changed: %s", self.partner_id.id)

        self.order_history_ids = [(5, 0, 0)]

        config_param = self.env['ir.config_parameter'].sudo()
        last_no_of_orders = int(config_param.get_param('sale.last_no_of_orders', default=10))
        last_no_of_days = int(config_param.get_param('sale.last_no_of_days', default=1))
        order_stages = config_param.get_param('sale.order_stages', default='all')
        date_limit = fields.Date.to_string(fields.Date.today() - timedelta(days=last_no_of_days))

        _logger.info("Configuration - last_no_of_orders: %d, last_no_of_days: %d, order_stages: %s",
                     last_no_of_orders, last_no_of_days, order_stages)

        domain = [('partner_id', '=', self.partner_id.id),('date_order', '>=', date_limit),('state', '=', order_stages)]

        _logger.info("Search domain: %s", domain)

        sale_orders = self.env['sale.order'].search(domain, order='date_order desc', limit=last_no_of_orders)

        _logger.info("Sale orders found: %d", len(sale_orders))

        histories = []
        for order in sale_orders:
            _logger.info("Order %d has %d lines", order.id, len(order.order_line))
            for line in order.order_line:
                _logger.info("Processing line %d with product %s", line.id, line.product_id.name)
                histories.append((0, 0, {
                    'order_id': order.id,
                    'order_line_id': line.id,
                    'name': order.name,
                    'date_order': order.date_order,
                    'product_id': line.product_id.id,
                    'price': line.price_unit,
                    'qty_unit': line.product_uom_qty,
                    'discount': line.discount,
                    'amount_total': line.price_subtotal,
                    'state': order.state,
                }))
        _logger.info("Histories to be set: %s", histories)
        self.order_history_ids = histories

    def action_reorder(self):
        config_param = self.env['ir.config_parameter'].sudo()

        if not config_param.get_param('sale.enable_reorder', False):
            raise UserError(_("Reorder is disabled in the settings. Please enable it to proceed."))


        if not self.partner_id:
            raise UserError(_("Customer is not set on the order. Please set the customer before reordering."))


        new_order_data = {
            'partner_id': self.partner_id.id,
            'state': 'draft',

        }

        new_order = self.env['sale.order'].create(new_order_data)

        order_lines = []
        for history in self.order_history_ids.filtered('order_history_selected'):
            if not history.product_id:
                raise UserError(
                    _("One or more products are missing in the order history. Please check your order history entries."))

            order_line_data = {
                'product_id': history.product_id.id,
                'product_uom_qty': history.qty_unit or 1.0,
                'price_unit': history.price,
                'discount': history.discount,
            }
            order_lines.append((0, 0, order_line_data))

        if not order_lines:
            raise UserError(_("No order lines available for reorder. Please select at least one item to reorder."))

        new_order.write({'order_line': order_lines})

        return {
            'type': 'ir.actions.act_window',
            'name': _('Sale Order'),
            'view_mode': 'form',
            'res_model': 'sale.order',
            'res_id': new_order.id,
            'target': 'current',
        }
