{
    "name": "Recordatorio de Cumpleaños (RRHH)",
    "version": "17.0.1.0.0",
    "depends": ["hr", "mail"],
    "author": "Hidelberg Martinez",
    "category": "Human Resources",
    "description": "Envía recordatorios por correo 7 días antes del cumpleaños del empleado.",
    "data": [
        "data/cron_birthday_reminder.xml",
        "views/hr_employee_view.xml"
    ],
    "installable": True,
    "license": "LGPL-3",
}
