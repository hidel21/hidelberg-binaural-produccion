{
    'name': 'Verificación de Calidad en Transferencias',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Quality Control',
    'summary': 'Añade verificación de calidad en transferencias de inventario',
    'description': '''
Este módulo añade un paso opcional de verificación de calidad al proceso de validación
de transferencias de inventario. Permite configurar si la verificación es requerida
por compañía y manejar la aprobación/rechazo de las transferencias.
''',
    'author': 'Hidelberg Efren Martinez Espitia',
    'github': 'https://github.com/hidel21/',
    'maintainer': 'Hidelberg Martinez',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/stock_picking_views.xml',
        'wizard/quality_verification_wizard.xml',
        'views/quality_verification_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}