from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class SaleOrderLineSelectPricelist(models.TransientModel):
    _name = 'sale.order.line.select.pricelist'
    _description = 'Wizard to Select Price List from Sale Order Line'

    order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line', required=True)
    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    price_list_ids = fields.One2many('sale.order.line.select.pricelist.line', 'wizard_id', string='Pricelists')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:

            pricelist_items = self.env['product.pricelist.item'].search([
                ('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)
            ])

            pricelist_lines = [(0, 0, {
                'pricelist_id': item.pricelist_id.id,
                'select': False,
            }) for item in pricelist_items]

            self.price_list_ids = pricelist_lines

    @api.model
    def default_get(self, fields_list):
        res = super(SaleOrderLineSelectPricelist, self).default_get(fields_list)
        order_line_id = self._context.get('default_order_line_id')
        product_id = self._context.get('default_product_id')

        res.update({
            'order_line_id': order_line_id,
            'product_id': product_id,
        })
        return res

    def action_select_pricelist(self):

        selected_lines = self.price_list_ids.filtered('select')

        if not selected_lines:
            raise ValidationError("No price list selected. Please select a price list.")

        if len(selected_lines) > 1:
            raise ValidationError("Only one price list can be selected at a time.")

        current_date = datetime.now().date()
        price_list = selected_lines.pricelist_id


        active_items = price_list.item_ids.filtered(
            lambda item: (not item.date_start or current_date >= item.date_start.date()) and
                         (not item.date_end or current_date <= item.date_end.date())
        )

        if not active_items:
            raise ValidationError(
                f"The selected price list '{price_list.name}' is not active or has expired. Please select a valid price list."
            )

        sale_order_line = self.order_line_id

        price_item = next(
            (item for item in active_items if item.product_id.id == sale_order_line.product_id.id),
            None
        )

        if price_item:
            sale_order_line.price_unit = price_item.fixed_price

        return {'type': 'ir.actions.act_window_close'}

    @api.onchange('price_list_ids')
    def _onchange_price_list_ids(self):

        selected_pricelists = self.price_list_ids.filtered(lambda r: r.select)
        if len(selected_pricelists) > 1:
            for pricelist in selected_pricelists[1:]:
                pricelist.select = False

class SaleOrderLineSelectPricelistLine(models.TransientModel):
    _name = 'sale.order.line.select.pricelist.line'
    _description = 'Wizard Line for Selecting Pricelist'

    wizard_id = fields.Many2one('sale.order.line.select.pricelist', string='Wizard')
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    select = fields.Boolean(string='Select')
