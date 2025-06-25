from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    warranty_months = fields.Integer(
        string="Meses de Garantía",
        readonly=True,
        help="Número de meses de garantía para este producto"
    )

    @api.onchange('product_id')
    def _onchange_product_id_warranty(self):
        for line in self:
            if line.product_id:
                line.warranty_months = line.product_id.warranty_months
