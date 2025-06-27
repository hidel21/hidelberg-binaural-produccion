{
    'name': 'Clasificación Fiscal',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Agrega clasificación fiscal a facturas con valores A, B y C',
    'description': '''
Este módulo agrega un campo de clasificación fiscal a las facturas
para categorizar según los tipos A, B y C, facilitando el control tributario
y la gestión contable personalizada.
''',
    'author': 'Hidelberg Efren Martinez Espitia',
    'github': 'https://github.com/hidel21/',
    'maintainer': 'Hidelberg Martinez',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
