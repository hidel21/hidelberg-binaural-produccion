from odoo import models, fields, api, _, exceptions

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    quality_verified = fields.Boolean(
        string='Verificado',
        copy=False,
        readonly=True,
        help='Indica si la transferencia ha sido verificada por calidad'
    )

    @api.model
    def _check_quality_verification(self):
        if not self.company_id.quality_verification_required:
            return True
        if self.quality_verified:
            return True
        return False

    def button_validate(self):
        if not self._check_quality_verification():
            wizard = self.env['quality.verification.wizard'].create({
                'picking_id': self.id
            })
            return {
                'type': 'ir.actions.act_window',
                'name': 'Verificación de Calidad',
                'res_model': 'quality.verification.wizard',
                'view_mode': 'form',
                'target': 'new',
                'res_id': wizard.id
            }
        return super(StockPicking, self).button_validate()
