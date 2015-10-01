from openerp import models, fields


class crm_lead(models.Model):

    _inherit = 'crm.lead'
    emails = fields.One2many(comodel_name='mail.mail.statistics',
                             inverse_name='res_id',
                             domain=[('model', '=', 'crm.lead')])

crm_lead()
