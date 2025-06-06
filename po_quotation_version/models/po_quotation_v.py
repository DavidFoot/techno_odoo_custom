# -*- coding: utf-8 -*-
from odoo import models, fields
class po_quotation_v(models.Model):
    _description = 'po_quotation_version.po_quotation_version'
    _inherit = 'purchase.order'
    quotation_version = fields.Char(string="Version du devis")