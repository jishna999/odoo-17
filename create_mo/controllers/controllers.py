# -*- coding: utf-8 -*-
# from odoo import http


# class CreateMo(http.Controller):
#     @http.route('/create_mo/create_mo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_mo/create_mo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_mo.listing', {
#             'root': '/create_mo/create_mo',
#             'objects': http.request.env['create_mo.create_mo'].search([]),
#         })

#     @http.route('/create_mo/create_mo/objects/<model("create_mo.create_mo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_mo.object', {
#             'object': obj
#         })

