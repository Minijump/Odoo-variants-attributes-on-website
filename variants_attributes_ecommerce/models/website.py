from odoo import api, fields, models, tools, SUPERUSER_ID, _


class WebsiteSaleExtraField(models.Model):
    _name = 'website.sale.extra.field.product.variant'

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


class PoductProduct(models.Model):
    _inherit = 'product.product'

    add_info_test = fields.Html()
    test_char_field = fields.Char() #because extra fields only take into account chars and binary
    

class Website(models.Model):
    _inherit = 'website'

    shop_extra_variants_field_ids = fields.One2many('website.sale.extra.field.product.variant', 'website_id', string='E-Commerce Extra Fields for variants')
