from odoo import models, fields

class QualityVerificationWizard(models.TransientModel):
    _name = 'quality.verification.wizard'
    _description = 'Verificación de Calidad'

    picking_id = fields.Many2one('stock.picking', required=True)
    approved = fields.Boolean(string="Aprobar Verificación")

    def action_confirm(self):
        if self.approved:
            self.picking_id.quality_verified = True
