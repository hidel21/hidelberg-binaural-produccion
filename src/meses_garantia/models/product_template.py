from odoo import models, fields, api
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    garantia_meses = fields.Integer(
        string='Meses de Garantía',
        help='Número de meses de garantía para este producto',
        default=0,
        tracking=True
    )
