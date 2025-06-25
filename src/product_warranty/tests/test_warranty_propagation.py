from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged('post_install', '-at_install')
class TestWarrantyPropagation(TransactionCase):
    def setUp(self):
        super().setUp()
        self.env = self.env(context=dict(self.env.context, tracking_disable=True))
        
        # Crear un producto de prueba
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'warranty_months': 24
        })
        
        # Crear una orden de venta de prueba
        self.sale_order = self.env['sale.order'].create({
            'partner_id': self.env.ref('base.res_partner_1').id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
                'price_unit': 100
            })]
        })

    def test_warranty_propagation(self):
        """Verificar que la garantía se propaga correctamente"""
        # Verificar que el producto tiene la garantía correcta
        self.assertEqual(self.product.warranty_months, 24)
        
        # Verificar que la garantía se copia a la línea de venta
        sale_line = self.sale_order.order_line[0]
        self.assertEqual(sale_line.warranty_months, 24)
        
        # Cambiar la garantía del producto y verificar que se actualiza
        self.product.warranty_months = 36
        self.assertEqual(sale_line.warranty_months, 36)
        
        # Verificar que la garantía se mantiene al cambiar el producto
        new_product = self.env['product.product'].create({
            'name': 'New Test Product',
            'warranty_months': 18
        })
        sale_line.product_id = new_product
        self.assertEqual(sale_line.warranty_months, 18)
