from odoo import models,fields,api


class Treatment(models.Model):
    _name = "treatment.treatment"
    _description = "Treatment"

    active = fields.Boolean(string="Active",default=True)
    name = fields.Char(string="Name", required=True)
    comment = fields.Text(string="Comment")
    hospital_id = fields.Many2one(comodel_name="res.partner", string="Hospital",domain="[('is_company', '=', True)]")
    physician_id = fields.Many2one(comodel_name="res.partner", string="Physician",domain="[('is_company', '=', False)]")
    therapy_id = fields.Many2one(comodel_name="treatment.therapy", string="Current Therapy")
