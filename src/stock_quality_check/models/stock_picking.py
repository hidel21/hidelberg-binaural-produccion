from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = "stock.picking"

    quality_verified = fields.Boolean(string="Verificación de Calidad Aprobada", default=False, readonly=True)

    def button_validate(self):
        for picking in self:
            if picking.company_id.require_quality_verification and not picking.quality_verified:
                raise UserError("Esta transferencia requiere verificación de calidad antes de validar.")
        return super().button_validate()
