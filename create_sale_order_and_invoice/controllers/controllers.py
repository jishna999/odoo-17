# -*- coding: utf-8 -*-
# from odoo import http


# class CreateSaleOrderAndInvoice(http.Controller):
#     @http.route('/create_sale_order_and_invoice/create_sale_order_and_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_sale_order_and_invoice/create_sale_order_and_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_sale_order_and_invoice.listing', {
#             'root': '/create_sale_order_and_invoice/create_sale_order_and_invoice',
#             'objects': http.request.env['create_sale_order_and_invoice.create_sale_order_and_invoice'].search([]),
#         })

#     @http.route('/create_sale_order_and_invoice/create_sale_order_and_invoice/objects/<model("create_sale_order_and_invoice.create_sale_order_and_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_sale_order_and_invoice.object', {
#             'object': obj
#         })

