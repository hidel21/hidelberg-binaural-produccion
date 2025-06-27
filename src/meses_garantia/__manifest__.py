{
    'name': 'Meses de Garantía',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Agrega campo de meses de garantía a productos, ventas y facturas',
    'description': '''
Este módulo agrega un campo para especificar los meses de garantía
en productos, ventas y facturas, permitiendo un mejor seguimiento
del compromiso postventa y servicio al cliente.
''',
    'author': 'Hidelberg Efren Martinez Espitia',
    'github': 'https://github.com/hidel21/',
    'maintainer': 'Hidelberg Martinez',
    'depends': ['sale', 'product', 'account'],
    'data': [
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
