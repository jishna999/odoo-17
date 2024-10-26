# -*- coding: utf-8 -*-
# from odoo import http


# class InvoicePicking(http.Controller):
#     @http.route('/invoice_picking/invoice_picking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_picking/invoice_picking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_picking.listing', {
#             'root': '/invoice_picking/invoice_picking',
#             'objects': http.request.env['invoice_picking.invoice_picking'].search([]),
#         })

#     @http.route('/invoice_picking/invoice_picking/objects/<model("invoice_picking.invoice_picking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_picking.object', {
#             'object': obj
#         })

