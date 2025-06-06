from odoo import models,fields
class BookTags(models.Model):
    _name = "library.book.tags"
    _description = "Library Book Tag"
    _order = 'sequence,id'
    _rec_name = "name"
    sequence = fields.Integer(default=10)
    name = fields.Char()
    color = models.fields.Integer(string='Color', help="Transparent tags are not visible in the kanban view of your projects and tasks.")
