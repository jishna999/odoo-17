# -*- coding: utf-8 -*-
# from odoo import http


# class SoToPo(http.Controller):
#     @http.route('/so_to_po/so_to_po', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/so_to_po/so_to_po/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('so_to_po.listing', {
#             'root': '/so_to_po/so_to_po',
#             'objects': http.request.env['so_to_po.so_to_po'].search([]),
#         })

#     @http.route('/so_to_po/so_to_po/objects/<model("so_to_po.so_to_po"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('so_to_po.object', {
#             'object': obj
#         })

