# -*- coding: utf-8 -*-
from odoo import models, fields

class Theme(models.Model):
    _name = 'my.animes.theme'
    _description = 'Anime Themes'
    _rec_name = 'themes'
    themes= models.fields.Char("Themes")