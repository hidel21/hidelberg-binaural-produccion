from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    mesa = fields.Char(string='Número de Mesa', help='Número de mesa donde se realizó el pedido')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('mesa'):
                # Propagar el número de mesa a todas las líneas
                if vals.get('invoice_line_ids'):
                    for line_vals in vals['invoice_line_ids']:
                        if isinstance(line_vals, (tuple, list)) and len(line_vals) >= 3:
                            line_vals[2]['mesa'] = vals['mesa']
        return super(AccountMove, self).create(vals_list)

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'mesa' in vals:
            # Actualizar todas las líneas existentes cuando se cambia el número de mesa
            for line in self.invoice_line_ids:
                line.mesa = vals['mesa']
        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    mesa = fields.Char(string='Número de mesa', help='Número de mesa donde se realizó el pedido')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'move_id' in vals and 'mesa' not in vals:
                move = self.env['account.move'].browse(vals['move_id'])
                vals['mesa'] = move.mesa
        return super(AccountMoveLine, self).create(vals_list)

    @api.onchange('move_id')
    def _onchange_move_id(self):
        if self.move_id and not self.mesa:
            self.mesa = self.move_id.mesa

    @api.onchange('mesa')
    def _onchange_mesa(self):
        if self.move_id and self.mesa:
            # Propagar el cambio al encabezado si es la primera línea
            if not self.move_id.invoice_line_ids.filtered(lambda l: l != self and l.mesa):
                self.move_id.mesa = self.mesa

    def write(self, vals):
        res = super(AccountMoveLine, self).write(vals)
        if 'mesa' in vals and self.move_id:
            # Actualizar el encabezado si es la primera línea
            if not self.move_id.invoice_line_ids.filtered(lambda l: l != self and l.mesa):
                self.move_id.mesa = vals['mesa']
        return res

    @api.onchange('mesa')
    def _onchange_mesa(self):
        if self.move_id and self.mesa != self.move_id.mesa:
            self.move_id.mesa = self.mesa
