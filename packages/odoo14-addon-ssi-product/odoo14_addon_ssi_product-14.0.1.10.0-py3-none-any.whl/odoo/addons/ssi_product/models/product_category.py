# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ProductCategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"
    _order = "parent_id, sequence, id"

    sequence = fields.Integer(
        string="Sequence",
        default=4,
        required=True,
    )
