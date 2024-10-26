# -*- coding: utf-8 -*-
# from odoo import http


# class AddMultipleProduct(http.Controller):
#     @http.route('/add_multiple_product/add_multiple_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_multiple_product/add_multiple_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_multiple_product.listing', {
#             'root': '/add_multiple_product/add_multiple_product',
#             'objects': http.request.env['add_multiple_product.add_multiple_product'].search([]),
#         })

#     @http.route('/add_multiple_product/add_multiple_product/objects/<model("add_multiple_product.add_multiple_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_multiple_product.object', {
#             'object': obj
#         })

