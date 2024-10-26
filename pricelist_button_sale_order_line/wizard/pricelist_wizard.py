from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PriceListWizard(models.TransientModel):
    _name = 'pricelist.wizard'
    _description = "Wizard for choosing pricelist for specific product on sale order line"

    sale_order_line_id = fields.Many2one(
        'sale.order.line',
        default=lambda self: self.env.context.get('active_id'),
        required=True
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        related='sale_order_line_id.product_id',
        string="Product",
        readonly=True
    )

    # price_list_ids = fields.Many2many(
    #     comodel_name='product.pricelist',
    #     string="Pricelists",
    #     help="Select pricelists for the current product.",
    #     default=lambda self: [(6, 0, self.env['product.pricelist'].search([]).ids)]
    # )

    price_list_ids = fields.Many2many(
        comodel_name='product.pricelist',
        string="Pricelists",
        help="Select pricelists for the current product."
    )


    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:

            pricelists = self.env['product.pricelist'].search([])

            matching_pricelists = []

            for pricelist in pricelists:
                for item in pricelist.item_ids:
                    if item.product_id == self.product_id:
                        matching_pricelists.append(pricelist.id)

            self.price_list_ids = [(6, 0, matching_pricelists)]


    def action_select_price_list_wizard(self):

        selection = self.price_list_ids.filtered('select')

        if not selection:
            raise ValidationError("No price list selected. Please select a price list.")

        if len(selection) > 1:
            raise ValidationError("Only one price list can be selected at a time.")

        current_date = datetime.now()
        price_list = selection[0]

        active_items = []
        for item in price_list.item_ids:
            if (not item.date_start or current_date >= item.date_start) and (not item.date_end or current_date <= item.date_end):
                active_items.append(item)

        if not active_items:
            raise ValidationError(
                f"The selected price list '{price_list.name}' is not active or has expired. Please select a valid price list."
            )

        sale_order_line = self.sale_order_line_id

        for item in active_items :
            if item.product_id.id == sale_order_line.product_id.id:
                price_item = item


        if price_item:
            sale_order_line.price_unit = price_item.fixed_price

        return {'type': 'ir.actions.act_window_close'}
