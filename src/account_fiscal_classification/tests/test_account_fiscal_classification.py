from odoo.tests.common import TransactionCase

class TestFiscalClassification(TransactionCase):

    def test_default_fiscal_classification(self):
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.env.ref('base.res_partner_1').id,
        })
        self.assertEqual(invoice.fiscal_classification, 'A')
