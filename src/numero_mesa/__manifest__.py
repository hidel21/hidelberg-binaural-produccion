{
    'name': 'Número de Mesa en Facturas',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Agrega número de mesa a facturas',
    'description': '''
Este módulo agrega un campo personalizado para registrar el número de mesa
en las facturas y sus reportes, facilitando el control en entornos como
restaurantes o eventos con mesas asignadas.
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
