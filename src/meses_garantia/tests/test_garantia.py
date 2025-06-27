from odoo.tests import common
from odoo import fields

class TestGarantia(common.TransactionCase):
    def setUp(self):
        super(TestGarantia, self).setUp()
        self.product = self.env['product.product']
        self.sale_order = self.env['sale.order']
        self.sale_order_line = self.env['sale.order.line']
        
        # Crear un producto de prueba
        self.product_test = self.product.create({
            'name': 'Producto de Prueba',
            'type': 'product',
            'garantia_meses': 12
        })

    def test_garantia_propagacion(self):
        """Verifica que la garantía se propague correctamente"""
        # Crear una orden de venta
        sale_order = self.sale_order.create({
            'partner_id': self.env.ref('base.res_partner_1').id,
            'order_line': [(0, 0, {
                'product_id': self.product_test.id,
                'product_uom_qty': 1,
                'price_unit': 100.00
            })]
        })
        
        # Verificar que la garantía se copió a la línea de orden
        self.assertEqual(
            sale_order.order_line.garantia_meses,
            self.product_test.garantia_meses,
            "La garantía no se copió correctamente a la línea de orden"
        )
        
        # Confirmar la orden
        sale_order.action_confirm()
        
        # Verificar que la garantía se mantiene en la factura
        invoice = sale_order._create_invoices()
        self.assertEqual(
            invoice.garantia_meses,
            self.product_test.garantia_meses,
            "La garantía no se mantuvo en la factura"
        )

    def test_garantia_cambio_producto(self):
        """Verifica que la garantía se actualice al cambiar el producto"""
        # Crear una orden de venta con un producto
        sale_order = self.sale_order.create({
            'partner_id': self.env.ref('base.res_partner_1').id,
            'order_line': [(0, 0, {
                'product_id': self.product_test.id,
                'product_uom_qty': 1,
                'price_unit': 100.00
            })]
        })
        
        # Crear un nuevo producto con diferente garantía
        new_product = self.product.create({
            'name': 'Nuevo Producto',
            'type': 'product',
            'garantia_meses': 24
        })
        
        # Cambiar el producto en la línea
        sale_order.order_line.product_id = new_product.id
        
        # Verificar que la garantía se actualizó
        self.assertEqual(
            sale_order.order_line.garantia_meses,
            new_product.garantia_meses,
            "La garantía no se actualizó al cambiar el producto"
        )
