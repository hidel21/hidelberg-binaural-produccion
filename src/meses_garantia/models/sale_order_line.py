from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    garantia_meses = fields.Integer(
        string='Meses de Garantía',
        help='Número de meses de garantía para este producto',
        default=0,
        tracking=True
    )

    @api.onchange('product_id')
    def product_id_change(self):
        if self.product_id:
            self.garantia_meses = self.product_id.garantia_meses
            if not self.garantia_meses:
                self.garantia_meses = self.product_id.product_tmpl_id.garantia_meses

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'product_id' in vals and 'garantia_meses' not in vals:
                product = self.env['product.product'].browse(vals['product_id'])
                vals['garantia_meses'] = product.garantia_meses or product.product_tmpl_id.garantia_meses
        return super(SaleOrderLine, self).create(vals_list)
