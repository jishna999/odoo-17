# -*- coding: utf-8 -*-
# from odoo import http


# class SalePurchaseDescriptionToDelivery(http.Controller):
#     @http.route('/sale_purchase_description_to_delivery/sale_purchase_description_to_delivery', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_purchase_description_to_delivery/sale_purchase_description_to_delivery/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_purchase_description_to_delivery.listing', {
#             'root': '/sale_purchase_description_to_delivery/sale_purchase_description_to_delivery',
#             'objects': http.request.env['sale_purchase_description_to_delivery.sale_purchase_description_to_delivery'].search([]),
#         })

#     @http.route('/sale_purchase_description_to_delivery/sale_purchase_description_to_delivery/objects/<model("sale_purchase_description_to_delivery.sale_purchase_description_to_delivery"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_purchase_description_to_delivery.object', {
#             'object': obj
#         })

