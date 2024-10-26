# -*- coding: utf-8 -*-
# from odoo import http


# class ProductBrandAdd(http.Controller):
#     @http.route('/product_brand_add/product_brand_add', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_brand_add/product_brand_add/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_brand_add.listing', {
#             'root': '/product_brand_add/product_brand_add',
#             'objects': http.request.env['product_brand_add.product_brand_add'].search([]),
#         })

#     @http.route('/product_brand_add/product_brand_add/objects/<model("product_brand_add.product_brand_add"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_brand_add.object', {
#             'object': obj
#         })

