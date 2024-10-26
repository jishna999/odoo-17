# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceFromSale(http.Controller):
#     @http.route('/invoice_from_sale/invoice_from_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_from_sale/invoice_from_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_from_sale.listing', {
#             'root': '/invoice_from_sale/invoice_from_sale',
#             'objects': http.request.env['invoice_from_sale.invoice_from_sale'].search([]),
#         })

#     @http.route('/invoice_from_sale/invoice_from_sale/objects/<model("invoice_from_sale.invoice_from_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_from_sale.object', {
#             'object': obj
#         })

