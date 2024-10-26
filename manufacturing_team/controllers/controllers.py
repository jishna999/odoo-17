# -*- coding: utf-8 -*-
# from odoo import http


# class ManufacturingTeam(http.Controller):
#     @http.route('/manufacturing_team/manufacturing_team', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturing_team/manufacturing_team/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturing_team.listing', {
#             'root': '/manufacturing_team/manufacturing_team',
#             'objects': http.request.env['manufacturing_team.manufacturing_team'].search([]),
#         })

#     @http.route('/manufacturing_team/manufacturing_team/objects/<model("manufacturing_team.manufacturing_team"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturing_team.object', {
#             'object': obj
#         })

