# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.api import ondelete

review_max_note = 10
review_list_note = [("null","Pas de note")]
for i in range(0,review_max_note + 1):
    review_list_note.append((str(i),str(i)))

class Anime(models.Model):
    _name = 'my.animes.anime'
    _description = 'Anime Model'
    _inherit = ['mail.thread.cc','mail.activity.mixin']
    label_name = fields.Char(string="Titre")
    full_name = fields.Text(string="Titres Alternatifs")
    original_name = fields.Char(string="Titres Original")
    review_note = fields.Selection(tracking=True,selection=review_list_note,default='null',string="Note")
    episode_count = fields.Integer(string="Nombres d'épisodes")
    season_id = fields.Many2one(comodel_name='my.animes.season',ondelete='set null', auto_join=True,string="Saison")
    genre_ids = fields.Many2many(comodel_name='my.animes.genre',relation='my_anime_anime_my_anime_genre_rel',column1='id_anime',column2='id_genre')
    theme_ids = fields.Many2many(comodel_name='my.animes.theme', relation='my_anime_anime_my_anime_theme_rel', column1='id_anime', column2='id_theme')
    cover_image = fields.Image(string="Image")
    state = fields.Selection(tracking=True,selection=[("None","---"),('Backlog','Backlog'),('En cours', 'En cours'),('En pause','En pause'),('Abandonné','Abandonné'),('Terminé','Terminé')], default='None', string="Etat")
    synopsis = fields.Text(string="Synopsis")
    commentaire = fields.Text(string="Commentaire", tracking=True)