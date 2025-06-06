from odoo import models,fields,api
class Member(models.Model):
    def _get_default_member_number(self):
        biggest_number_member = self.sudo().search([], order='member_number desc', limit=1)
        return biggest_number_member.member_number + 1


    _name = "library.member"
    _description = "Library Members"
    _rec_name = "name"
    active = models.fields.Boolean()
    name = models.fields.Char(string="Name")
    mail = models.fields.Char(string="Mail")
    phone = models.fields.Integer(string="Phone")
    member_number = models.fields.Integer(string="Number",default=_get_default_member_number)
    subsscription_date = models.fields.Date(string="Subscription")
    favorite_book_id = fields.Many2one(comodel_name='library.book', string="Bouquin Favori")
    loan_ids = fields.One2many(comodel_name='library.loan',inverse_name="member_id", string="Bouquin Emprunté", domain=[('state', '=', 'Ongoing')])
    loan_count = fields.Integer(compute="_compute_total_loans", string="Emprunts", default="0")

    @api.depends("loan_ids")
    def _compute_total_loans(self):
        for record in self:
            record.loan_count = len(record.loan_ids)

    def action_loans_count(self):
        return {
            'name': 'Loans',
            'view_mode': 'list',
            'domain': [('member_id', '=', self.id)],
            'res_model': 'library.loan',
            'type': 'ir.actions.act_window',
        }
