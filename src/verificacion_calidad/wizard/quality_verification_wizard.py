from odoo import models, fields, api

class QualityVerificationWizard(models.TransientModel):
    _name = 'quality.verification.wizard'
    _description = 'Wizard de Verificación de Calidad'

    picking_id = fields.Many2one(
        'stock.picking',
        string='Transferencia',
        readonly=True
    )

    verification_result = fields.Selection(
        [('approved', 'Aprobado'),
         ('rejected', 'Rechazado')],
        string='Resultado',
        required=True,
        default='approved'
    )

    notes = fields.Text(
        string='Notas'
    )

    @api.model
    def action_open_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Verificación de Calidad',
            'res_model': 'quality.verification.wizard',
            'view_mode': 'form',
            'target': 'new',
        }

    def action_validate(self):
        if self.verification_result == 'approved':
            self.picking_id.quality_verified = True
            return self.picking_id.button_validate()
        else:
            self.picking_id.message_post(
                body=f'Verificación de calidad rechazada. Razón: {self.notes}'
            )
            return {'type': 'ir.actions.act_window_close'}

    def action_cancel(self):
        return {'type': 'ir.actions.act_window_close'}
