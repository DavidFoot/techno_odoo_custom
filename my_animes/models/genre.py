# -*- coding: utf-8 -*-
from odoo import models, fields

class Genre(models.Model):
    _name = 'my.animes.genre'
    _description = 'Anime Genres'
    _rec_name = 'genre'
    genre= models.fields.Char("Genre")