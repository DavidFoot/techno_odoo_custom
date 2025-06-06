# -*- coding: utf-8 -*-
# from odoo import http


# class PoQuotationVersion(http.Controller):
#     @http.route('/po_quotation_version/po_quotation_version', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_quotation_version/po_quotation_version/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_quotation_version.listing', {
#             'root': '/po_quotation_version/po_quotation_version',
#             'objects': http.request.env['po_quotation_version.po_quotation_version'].search([]),
#         })

#     @http.route('/po_quotation_version/po_quotation_version/objects/<model("po_quotation_version.po_quotation_version"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_quotation_version.object', {
#             'object': obj
#         })

