from odoo import models,fields,api


class Patient(models.Model):
    _name = "treatment.patient"
    _description = "Treatment patient"

    active = fields.Boolean(string="Active",default="True")
    lastname = fields.Char(string="Lastname")
    firstname = fields.Char(string="Firstname")
    birthdate = fields.Date(string="Birth Date")
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
        if not self.niss:
            self.niss = self.birthdate.strftime("%Y%m%d")

    @api.onchange('niss')
    def _clean_niss(self):
        if self.niss:
            self.niss = ''.join(filter(str.isdigit,self.niss))

    # @api.onchange('birthdate')
    # def _autocomplete_niss_with_birthdate(self):
    #     if not self.niss:
    #         self.niss = self.birthdate.strftime("%Y%m%d")
