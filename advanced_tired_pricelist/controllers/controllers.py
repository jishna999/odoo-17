# -*- coding: utf-8 -*-
# from odoo import http


# class AdvancedTiredPricelist(http.Controller):
#     @http.route('/advanced_tired_pricelist/advanced_tired_pricelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advanced_tired_pricelist/advanced_tired_pricelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('advanced_tired_pricelist.listing', {
#             'root': '/advanced_tired_pricelist/advanced_tired_pricelist',
#             'objects': http.request.env['advanced_tired_pricelist.advanced_tired_pricelist'].search([]),
#         })

#     @http.route('/advanced_tired_pricelist/advanced_tired_pricelist/objects/<model("advanced_tired_pricelist.advanced_tired_pricelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advanced_tired_pricelist.object', {
#             'object': obj
#         })

