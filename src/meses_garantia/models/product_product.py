from odoo import models, fields, api
class ProductProduct(models.Model):
    _inherit = 'product.product'

    garantia_meses = fields.Integer(
        string='Meses de Garantía',
        help='Número de meses de garantía para este producto',
        default=0,
        tracking=True
    )
