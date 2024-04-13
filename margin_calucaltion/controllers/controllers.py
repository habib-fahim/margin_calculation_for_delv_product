# -*- coding: utf-8 -*-
# from odoo import http


# class PickingReport(http.Controller):
#     @http.route('/picking_report/picking_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/picking_report/picking_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('picking_report.listing', {
#             'root': '/picking_report/picking_report',
#             'objects': http.request.env['picking_report.picking_report'].search([]),
#         })

#     @http.route('/picking_report/picking_report/objects/<model("picking_report.picking_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('picking_report.object', {
#             'object': obj
#         })
