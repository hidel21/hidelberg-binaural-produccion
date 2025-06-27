from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    clasificacion_fiscal = fields.Selection(
        selection=[('A', 'A'),('B', 'B'),('C', 'C')],
        string='Clasificación Fiscal',
        default='A',
        required=True,
    )
