from odoo.tests.common import TransactionCase

class TestPOSTableNumber(TransactionCase):

    def test_field_exists(self):
        session = self.env['pos.session'].create({
            'config_id': self.env['pos.config'].search([], limit=1).id
        })
        order = self.env['pos.order'].create({
            'session_id': session.id,
            'partner_id': self.env.ref('base.res_partner_1').id,
            'table_number': 'M12'
        })
        self.assertEqual(order.table_number, 'M12')
