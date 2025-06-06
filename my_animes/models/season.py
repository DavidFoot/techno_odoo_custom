# -*- coding: utf-8 -*-
from odoo import models, fields

class Season(models.Model):
    _name = 'my.animes.season'
    _description = 'Anime season'
    _rec_name = 'season_name'
    season_name= models.fields.Char("Season")