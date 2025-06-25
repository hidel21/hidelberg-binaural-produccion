{
    "name": "POS - Número de Mesa",
    "version": "17.0.1.0.0",
    "depends": ["point_of_sale"],
    "author": "Hidelberg Martinez",
    "category": "Point of Sale",
    "description": "Permite asociar un número de mesa a cada pedido en POS y mostrarlo en recibos y en el backend.",
    "data": [
        "views/pos_order_view.xml"
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_table_number/static/src/**/*"
        ]
    },
    "installable": True,
    "license": "LGPL-3"
}
