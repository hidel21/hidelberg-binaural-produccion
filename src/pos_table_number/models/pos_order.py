from odoo import fields, models

class PosOrder(models.Model):
    _inherit = "pos.order"

    table_number = fields.Char(string="Número de Mesa")
