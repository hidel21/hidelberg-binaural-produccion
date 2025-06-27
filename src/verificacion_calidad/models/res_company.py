from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    quality_verification_required = fields.Boolean(
        string='Requerir Verificación de Calidad',
        help='Si está activado, se requiere verificación de calidad para todas las transferencias de inventario'
    )
