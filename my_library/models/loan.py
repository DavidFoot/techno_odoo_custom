import datetime

from dateutil.relativedelta import relativedelta

from odoo import models,fields,api, exceptions
class Loan(models.Model):
    _name = "library.loan"
    _description = "Library Loan"
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    active = models.fields.Boolean()
    check_out_date = models.fields.Date(string="Check out date")
    return_date_due = models.fields.Date(string="Return date")
    return_date_effective = models.fields.Date(string="Effective Return Date")
    state = models.fields.Selection(tracking=True,string="State", selection=[("Ongoing","Ongoing"),("Returned","Returned"),("Late","Late")])
    member_id = models.fields.Many2one(comodel_name="library.member",string="Emprunteur")
    book_id = models.fields.Many2one(comodel_name="library.book", string="Livre emprunté")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals['book_id']:
                raise exceptions.ValidationError("Pas de bouquin selectionné pour la location")
        res = super().create(vals_list)
        for record in res :
            record.book_id.quantity_available -=1
        return res

    def write(self, values):
        if 'state' in values and values['state'] == "Returned" :
            values['active'] = False
            for record in self:
                if record.book_id:
                    record.book_id.quantity_available +=  1
                    values['book_id'] = record.book_id
        return  super().write(values)

    def _run_update_chatter_loan_return_date(self):
        self.sudo().search([])._late_loan_notification()

    def _late_loan_notification(self):
        for loan_model in self:
            if loan_model.return_date_due < datetime.date.today():
                loan_model.message_post(body='Livre en retard')

    def _display_loan_in_chatter(self):
        for model_loan in self:
            model_loan.message_post(body=f'Livre {model_loan.book_id.title} emprunté par {model_loan.member_id.name} du {model_loan.check_out_date.strftime('%d-%m-%Y')} au {model_loan.return_date_due.strftime('%d-%m-%Y')}')

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        if 'check_out_date' in fields_list:
            res['check_out_date'] = fields.Date.today()
        if 'return_date_due' in fields_list:
            res['return_date_due'] = fields.Date.today() + relativedelta(months=3)
        return res