{
    'name': 'Recordatorio de Cumpleaños',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Envía recordatorios por correo 7 días antes del cumpleaños del empleado.',
    'description': '''
Este módulo envía recordatorios por correo 7 días antes del cumpleaños de los empleados,
facilitando la organización de celebraciones o detalles corporativos de reconocimiento.
''',
    'author': 'Hidelberg Efren Martinez Espitia',
    'github': 'https://github.com/hidel21/',
    'maintainer': 'Hidelberg Martinez',
    'depends': ['hr', 'mail'],
    'data': [
        'data/cron_data.xml',
        'data/email_template.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
