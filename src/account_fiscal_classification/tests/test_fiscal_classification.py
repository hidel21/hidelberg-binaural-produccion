from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged('post_install', '-at_install')
class TestFiscalClassification(TransactionCase):
    def setUp(self):
        super().setUp()
        self.env = self.env(context=dict(self.env.context, tracking_disable=True))
        
        # Crear un producto y partner para la factura
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'product',
            'list_price': 100.0
        })
        
        self.partner = self.env['res.partner'].create({
            'name': 'Test Partner'
        })

    def test_default_fiscal_classification(self):
        """Verificar que la clasificación fiscal por defecto es 'A'"""
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product.id,
                'quantity': 1,
                'price_unit': 100.0
            })]
        })
        
        self.assertEqual(invoice.fiscal_classification, 'A', 
                         "La clasificación fiscal por defecto debe ser 'A'")

    def test_change_fiscal_classification(self):
        """Verificar que se puede cambiar la clasificación fiscal"""
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product.id,
                'quantity': 1,
                'price_unit': 100.0
            })]
        })
        
        # Cambiar a B
        invoice.fiscal_classification = 'B'
        self.assertEqual(invoice.fiscal_classification, 'B', 
                         "La clasificación fiscal debe poder cambiarse a 'B'")
        
        # Cambiar a C
        invoice.fiscal_classification = 'C'
        self.assertEqual(invoice.fiscal_classification, 'C', 
                         "La clasificación fiscal debe poder cambiarse a 'C'")
