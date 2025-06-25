from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = "product.product"

    warranty_months = fields.Integer(
        string="Meses de Garantía",
        related="product_tmpl_id.warranty_months",
        store=True,
        tracking=True,
        help="Número de meses de garantía para este producto"
    )
