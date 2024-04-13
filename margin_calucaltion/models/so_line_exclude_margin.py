from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    excluded_margin = fields.Boolean(string="Excluded Margin", related='product_id.excluded_from_margin')
