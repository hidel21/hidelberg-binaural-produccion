from odoo.tests.common import TransactionCase

class TestQualityCheck(TransactionCase):

    def test_quality_required_logic(self):
        company = self.env.user.company_id
        company.require_quality_verification = True

        picking = self.env['stock.picking'].create({
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'location_dest_id': self.env.ref('stock.stock_location_customers').id,
            'picking_type_id': self.env.ref('stock.picking_type_out').id,
        })

        with self.assertRaises(Exception):
            picking.button_validate()

        # Simular aprobación
        picking.quality_verified = True
        picking.button_validate()
