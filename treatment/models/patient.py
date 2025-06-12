from odoo import models,fields,api
import datetime

class Patient(models.Model):
    _name = "treatment.patient"
    _description = "Treatment patient"

    active = fields.Boolean(string="Active",default="True")
    lastname = fields.Char(string="Lastname")
    firstname = fields.Char(string="Firstname")
    birthdate = fields.Date(string="Birth Date", compute="_compute_birthdate_with_niss", readonly=False, store=True)
    niss = fields.Char(string="National Number", compute="_compute_niss_with_birthdate", readonly=False, store=True )
    therapy_id = fields.Many2one(comodel_name="treatment.therapy",string="Therapy")
    treatments_ids = fields.Many2many(comodel_name="treatment.treatment", string="Current Treatments")

    @api.onchange("therapy_id")
    def _set_default_treatments(self):
        for rec in self:
            if rec.therapy_id:
                rec.treatments_ids = rec.therapy_id.treatment_ids

    @api.depends("birthdate")
    def _compute_niss_with_birthdate(self):
        for record in self:
            if not record.niss and record.birthdate:
                record.niss = record.birthdate.strftime("%Y%m%d")

    @api.depends("niss")
    def _compute_birthdate_with_niss(self):
        for record in self:
            if record.niss:
                record.niss = ''.join(filter(str.isdigit,record.niss))
            if not record.birthdate and record.niss:
                try:
                    record.birthdate = datetime.datetime.strptime( record.niss, "%Y%m%d").date()
                except ValueError :
                    record.birthdate = ""

    #
    # Exemples with onchange method
    #
    # @api.onchange('niss')
    # def _clean_niss(self):
    #     if self.niss:
    #         self.niss = ''.join(filter(str.isdigit,self.niss))
    #     if not self.birthdate and self.niss:
    #         self.birthdate = datetime.datetime.strptime( self.niss, "%Y%m%d").date()

    # @api.onchange('birthdate')
    # def _autocomplete_niss_with_birthdate(self):
    #     if not self.niss:
    #         self.niss = self.birthdate.strftime("%Y%m%d")
