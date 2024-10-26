# -*- coding: utf-8 -*-
# from odoo import http


# class PickingVendorBill(http.Controller):
#     @http.route('/picking_vendor_bill/picking_vendor_bill', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/picking_vendor_bill/picking_vendor_bill/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('picking_vendor_bill.listing', {
#             'root': '/picking_vendor_bill/picking_vendor_bill',
#             'objects': http.request.env['picking_vendor_bill.picking_vendor_bill'].search([]),
#         })

#     @http.route('/picking_vendor_bill/picking_vendor_bill/objects/<model("picking_vendor_bill.picking_vendor_bill"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('picking_vendor_bill.object', {
#             'object': obj
#         })

