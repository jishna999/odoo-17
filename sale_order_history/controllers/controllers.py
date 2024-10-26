# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderHistory(http.Controller):
#     @http.route('/sale_order_history/sale_order_history', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_history/sale_order_history/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_history.listing', {
#             'root': '/sale_order_history/sale_order_history',
#             'objects': http.request.env['sale_order_history.sale_order_history'].search([]),
#         })

#     @http.route('/sale_order_history/sale_order_history/objects/<model("sale_order_history.sale_order_history"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_history.object', {
#             'object': obj
#         })

