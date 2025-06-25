from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    require_quality_verification = fields.Boolean(
        string="Requiere verificación de calidad en transferencias"
    )
