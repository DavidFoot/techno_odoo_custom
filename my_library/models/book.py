from odoo import models,fields, api

class Book(models.Model):
    _name = "library.book"
    _description = "Library Book"
    _order = 'sequence,id'
    _rec_name = "title"
    active = models.fields.Boolean()
    sequence = models.fields.Integer(default=10)
    summary = models.fields.Char(string="Summary")
    title = models.fields.Char(string="Title")
    author = models.fields.Char(string="Author")
    pages = models.fields.Integer(string="Pages")
    quantity_available = models.fields.Integer(string="Nombre d'exemplaire")
    isbn = models.fields.Char(string="ISBN")
    state = models.fields.Selection(string="State",selection=[("Available","Available"),("Borrowed","Borrowed"),("Lost","Lost")],group_expand='_group_expand_states')
    books_ids = models.fields.Many2many(string="Serie", comodel_name="library.book", relation='library_book_library_book_rel',column1='book1_id',column2='book2_id')
    cover = models.fields.Binary(attachment=False)
    date_published = models.fields.Date(string="Date de publication")
    price = models.fields.Float(string="Price")
    color = models.fields.Integer(string='Color', help="Transparent tags are not visible in the kanban view of your projects and tasks.")
    tag_ids = models.fields.Many2many(string="Etiquette", comodel_name="library.book.tags", relation='library_book_library_book_tags_rel',column1='book_id',column2='tag_id')
    category_ids = models.fields.Many2many(string="Catégories", comodel_name="library.book.category")
    favorited_by_members_ids = fields.One2many(comodel_name='library.member', inverse_name="favorite_book_id" ,string="En Favori chez les membres")

    def _group_expand_states(self, states, domain):
        return [key for key, val in type(self).state.selection]

    def add_library_book_qty(self):
        for record in self:
            record.quantity_available += 1
            self.check_state_from_qty()
        return True

    @api.onchange("quantity_available")
    def on_change_state(self):
        self.check_state_from_qty()

    def check_state_from_qty(self):
        if  self.quantity_available < 0:
            self.state =  "Lost"
        elif  self.quantity_available == 0 :
            self.state = "Borrowed"
        else:
            self.state = "Available"
