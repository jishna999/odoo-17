# -*- coding: utf-8 -*-
# from odoo import http


# class SaleInv(http.Controller):
#     @http.route('/sale_inv/sale_inv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_inv/sale_inv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_inv.listing', {
#             'root': '/sale_inv/sale_inv',
#             'objects': http.request.env['sale_inv.sale_inv'].search([]),
#         })

#     @http.route('/sale_inv/sale_inv/objects/<model("sale_inv.sale_inv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_inv.object', {
#             'object': obj
#         })

