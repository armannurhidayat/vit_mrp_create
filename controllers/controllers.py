# -*- coding: utf-8 -*-
from odoo import http

# class VitMrp(http.Controller):
#     @http.route('/vit_mrp/vit_mrp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_mrp/vit_mrp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_mrp.listing', {
#             'root': '/vit_mrp/vit_mrp',
#             'objects': http.request.env['vit_mrp.vit_mrp'].search([]),
#         })

#     @http.route('/vit_mrp/vit_mrp/objects/<model("vit_mrp.vit_mrp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_mrp.object', {
#             'object': obj
#         })