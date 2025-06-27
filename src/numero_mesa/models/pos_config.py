from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    mostrar_mesa = fields.Boolean(string='Mostrar Número de Mesa',
                                 help='Si está marcado, se mostrará el campo de número de mesa en el POS')
