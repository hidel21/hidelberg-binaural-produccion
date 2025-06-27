from odoo.tests import common
from odoo import fields
from datetime import datetime, timedelta

class TestBirthdayReminder(common.TransactionCase):
    def setUp(self):
        super(TestBirthdayReminder, self).setUp()
        self.employee = self.env['hr.employee']
        self.mail_template = self.env['mail.template']
        
        # Crear un empleado de prueba
        self.test_employee = self.env['hr.employee'].create({
            'name': 'Test Employee',
            'work_email': 'test@example.com',
            'birthday': (fields.Date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        })

    def test_send_birthday_reminder(self):
        """Verifica que el recordatorio se envíe correctamente"""
        # Ejecutar el método de envío
        result = self.employee._send_birthday_reminders()
        
        # Verificar que se encontró el empleado
        self.assertTrue(self.test_employee in self.employee.search([]))
        
        # Verificar que se creó el correo
        mail = self.env['mail.mail'].search([
            ('email_to', '=', 'test@example.com'),
            ('subject', 'like', 'Recordatorio: Cumpleaños de')
        ])
        self.assertTrue(mail)
        
        # Verificar que el correo está en estado 'sent'
        self.assertEqual(mail.state, 'sent')

    def test_send_birthday_reminder_no_email(self):
        """Verifica que se maneje correctamente un empleado sin correo"""
        # Crear un empleado sin correo
        employee_no_email = self.env['hr.employee'].create({
            'name': 'Employee Without Email',
            'birthday': (fields.Date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        })
        
        # Ejecutar el método de envío
        result = self.employee._send_birthday_reminders()
        
        # Verificar que se creó una actividad de error
        activity = self.env['mail.activity'].search([
            ('res_model', '=', 'hr.employee'),
            ('res_id', '=', employee_no_email.id),
            ('summary', 'like', 'Error al enviar recordatorio')
        ])
        self.assertTrue(activity)

    def test_send_birthday_reminder_future_date(self):
        """Verifica que no se envíen recordatorios para cumpleaños muy lejanos"""
        # Crear un empleado con cumpleaños en 14 días
        future_employee = self.env['hr.employee'].create({
            'name': 'Future Employee',
            'work_email': 'future@example.com',
            'birthday': (fields.Date.today() + timedelta(days=14)).strftime('%Y-%m-%d')
        })
        
        # Ejecutar el método de envío
        result = self.employee._send_birthday_reminders()
        
        # Verificar que no se creó correo para este empleado
        mail = self.env['mail.mail'].search([
            ('email_to', '=', 'future@example.com'),
            ('subject', 'like', 'Recordatorio: Cumpleaños de')
        ])
        self.assertFalse(mail)
