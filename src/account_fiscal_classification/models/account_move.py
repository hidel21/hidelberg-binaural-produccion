from odoo import fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    fiscal_classification = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ], string="Clasificación Fiscal", default="A", tracking=True)
