from odoo.tests.common import TransactionCase
from datetime import date, timedelta

class TestBirthdayReminder(TransactionCase):

    def test_reminder_logic(self):
        today = date.today()
        emp = self.env['hr.employee'].create({
            'name': 'Empleado Prueba',
            'birthday': today + timedelta(days=7),
            'work_email': 'empleado@ejemplo.com',
        })
        # Solo se valida que no genere error
        emp._cron_send_birthday_reminders()
