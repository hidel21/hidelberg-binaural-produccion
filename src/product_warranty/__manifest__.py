{
    'name': 'Meses de Garantía en Productos',
    'version': '17.0.1.0.0',
    'depends': ['product', 'sale_management'],
    'author': 'Hidelberg Martinez',
    'category': 'Sales',
    'description': 'Agrega campo de meses de garantía a productos y lo propaga a las líneas de orden de venta.',
    'data': [
        'views/product_template_view.xml',
        'views/sale_order_view.xml'
    ],
    'demo': [],
    'test': [],
    'application': False,
    'auto_install': False,
    'installable': True,
    'license': 'LGPL-3',
}
