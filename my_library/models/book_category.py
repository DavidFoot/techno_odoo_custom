from email.policy import default

from odoo import models,fields, api
class BookCategory(models.Model):
    _name = "library.book.category"
    _description = "Categorie de Livre"
    _rec_name = "name"
    name= fields.Char(string="Catégorie")
    description = fields.Text(string="Description")
    book_ids = fields.Many2many(string="Liste des Livres",comodel_name="library.book")
    total_books = fields.Integer(compute="_compute_total_books", string="Livres", default = "0")

    @api.depends("book_ids")
    def _compute_total_books(self):
        for record in self:
            record.total_books = len(record.book_ids)
