from odoo import models, fields
from datetime import timedelta

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def _cron_send_birthday_reminders(self):
        today = fields.Date.today()
        target_date = today + timedelta(days=7)
        employees = self.search([])

        for emp in employees:
            if emp.birthday:
                birthday_this_year = emp.birthday.replace(year=today.year)
                if birthday_this_year == target_date:
                    template = self.env.ref("hr_birthday_reminder.mail_template_birthday_reminder")
                    template.send_mail(emp.id, force_send=True)
