from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    garantia_meses = fields.Integer(string='Meses de Garantía')

    def _prepare_invoice_line(self, line):
        res = super(AccountMove, self)._prepare_invoice_line(line)
        res.update({
            'garantia_meses': line.garantia_meses,
        })
        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    garantia_meses = fields.Integer(
        string='Meses de Garantía',
        help='Número de meses de garantía para este producto',
        default=0,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'product_id' in vals and 'garantia_meses' not in vals:
                product = self.env['product.product'].browse(vals['product_id'])
                vals['garantia_meses'] = product.garantia_meses or product.product_tmpl_id.garantia_meses
        return super(AccountMoveLine, self).create(vals_list)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.garantia_meses = self.product_id.garantia_meses
            if not self.garantia_meses:
                self.garantia_meses = self.product_id.product_tmpl_id.garantia_meses
