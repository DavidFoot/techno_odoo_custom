from email.policy import default

from odoo import models,fields,api


class Therapy(models.Model):
    _name = "treatment.therapy"
    _description = "Treatment therapy"
    _rec_name = "display_name"

    active = fields.Boolean(string="Active", default="True")
    display_name = fields.Char(string="Display Name", compute="_compute_display_name",default="", store=True)
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    treatment_count = fields.Integer(compute='compute_treatment_count',default=0)
    treatment_ids = fields.One2many(comodel_name='treatment.treatment', inverse_name="therapy_id")

    @api.depends("code","name")
    def _compute_display_name(self):
        for record in self:
            if not record.code :
                record.code = ""
            if not record.name :
                record.name = ""
            record.display_name = f"[{record.code}] {record.name}"

    def compute_treatment_count(self):
        for record in self:
            record.treatment_count = self.env['treatment.treatment'].search_count(
                [('therapy_id.id', '=', self.id)])

    def action_button_treatment_list(self):
        return {
            'name': 'Treatments',
            'view_mode': 'list',
            'domain': [('therapy_id.id', '=', self.id)],
            'res_model': 'treatment.treatment',
            'type': 'ir.actions.act_window',
        }
