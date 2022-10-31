# -*- coding: utf-8 -*-
# from odoo import http


# class Mymodule(http.Controller):
#     @http.route('/Real_Estate/Real_Estate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/Real_Estate/Real_Estate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('Real_Estate.listing', {
#             'root': '/Real_Estate/Real_Estate',
#             'objects': http.request.env['Real_Estate.Real_Estate'].search([]),
#         })

#     @http.route('/Real_Estate/Real_Estate/objects/<model("Real_Estate.Real_Estate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('Real_Estate.object', {
#             'object': obj
#         })
