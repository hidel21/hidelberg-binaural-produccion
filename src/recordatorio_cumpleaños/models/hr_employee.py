from odoo import models, fields, api
from datetime import datetime, timedelta

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _send_birthday_reminders(self):
        """Envía recordatorios de cumpleaños"""
        today = fields.Date.today()
        next_week = today + timedelta(days=7)
        
        # Buscar empleados con cumpleaños la próxima semana
        employees = self.env['hr.employee'].search([
            ('birthday', '!=', False),
            ('birthday', 'like', f'%{next_week.strftime("%m-%d")}')
        ])
        
        if not employees:
            return False
            
        for employee in employees:
            if employee.send_birthday_email():
                employee.message_post(
                    body='Recordatorio de cumpleaños enviado correctamente',
                    subtype_xmlid='mail.mt_note'
                )
        return True

    def send_birthday_email(self):
        """Envía el correo de recordatorio"""
        try:
            template = self.env.ref('recordatorio_cumpleaños.email_template_birthday_reminder')
            if template and self.work_email:
                # Enviar el correo usando el template directamente
                template.send_mail(
                    self.id,
                    force_send=True,
                    email_values={
                        'email_from': self.env.user.email,
                        'email_to': self.work_email,
                        'subject': f'Recordatorio: Cumpleaños de {self.name}'
                    }
                )
                return True
            return False
        except Exception as e:
            self.env['mail.activity'].create({
                'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                'summary': 'Error al enviar recordatorio de cumpleaños',
                'note': f'Error: {str(e)}',
                'res_model_id': self.env['ir.model'].search([('model', '=', 'hr.employee')]).id,
                'res_id': self.id,
                'user_id': self.env.user.id
            })
            return False
