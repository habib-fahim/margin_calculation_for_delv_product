from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    excluded_from_margin = fields.Boolean('Excluded from Margin')


