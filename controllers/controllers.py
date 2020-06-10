# -*- coding: utf-8 -*-
# from odoo import http


# class Proforma-oto(http.Controller):
#     @http.route('/proforma-oto/proforma-oto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proforma-oto/proforma-oto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proforma-oto.listing', {
#             'root': '/proforma-oto/proforma-oto',
#             'objects': http.request.env['proforma-oto.proforma-oto'].search([]),
#         })

#     @http.route('/proforma-oto/proforma-oto/objects/<model("proforma-oto.proforma-oto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proforma-oto.object', {
#             'object': obj
#         })
