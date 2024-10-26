# -*- coding: utf-8 -*-
# from odoo import http


# class PricelistButtonSaleOrderLine(http.Controller):
#     @http.route('/pricelist_button_sale_order_line/pricelist_button_sale_order_line', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pricelist_button_sale_order_line/pricelist_button_sale_order_line/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pricelist_button_sale_order_line.listing', {
#             'root': '/pricelist_button_sale_order_line/pricelist_button_sale_order_line',
#             'objects': http.request.env['pricelist_button_sale_order_line.pricelist_button_sale_order_line'].search([]),
#         })

#     @http.route('/pricelist_button_sale_order_line/pricelist_button_sale_order_line/objects/<model("pricelist_button_sale_order_line.pricelist_button_sale_order_line"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pricelist_button_sale_order_line.object', {
#             'object': obj
#         })

