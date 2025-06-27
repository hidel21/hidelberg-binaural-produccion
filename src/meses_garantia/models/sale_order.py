from odoo import models, fields, api
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['garantia_meses'] = self.order_line[0].garantia_meses if self.order_line else 0
        return invoice_vals
