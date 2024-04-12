from odoo import api, fields, models, tools, SUPERUSER_ID, _


class WebsiteSaleExtraField(models.Model):
    _name = 'website.sale.extra.field.product.variant'
    _description = 'Enable to add variants specific fields on website'

    website_id = fields.Many2one('website')
    sequence = fields.Integer(default=10)
    field_id = fields.Many2one(
        'ir.model.fields',
        domain=[('model_id.model', '=', 'product.product'), ('ttype', 'in', ['char', 'binary'])],
        required=True,
        ondelete='cascade'
    )
    label = fields.Char(related='field_id.field_description')
    name = fields.Char(related='field_id.name')   


class Website(models.Model):
    _inherit = 'website'

    shop_extra_variants_field_ids = fields.One2many('website.sale.extra.field.product.variant', 'website_id', string='E-Commerce Extra Fields for variants')
