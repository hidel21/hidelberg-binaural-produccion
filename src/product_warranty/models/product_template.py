from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    warranty_months = fields.Integer(
        string="Meses de Garantía",
        default=12,
        tracking=True,
        help="Número de meses de garantía para este producto"
    )
