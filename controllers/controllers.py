# -*- coding: utf-8 -*-
from odoo import http

# class Emex51Module(http.Controller):
#     @http.route('/emex51_module/emex51_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emex51_module/emex51_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emex51_module.listing', {
#             'root': '/emex51_module/emex51_module',
#             'objects': http.request.env['emex51_module.emex51_module'].search([]),
#         })

#     @http.route('/emex51_module/emex51_module/objects/<model("emex51_module.emex51_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emex51_module.object', {
#             'object': obj
#         })