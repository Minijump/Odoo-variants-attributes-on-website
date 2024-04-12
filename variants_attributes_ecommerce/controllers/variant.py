# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route, Controller

from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController


class WebsiteSaleVariantControllerVariantsAttr(WebsiteSaleVariantController):

    @http.route()
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        combination = super().get_combination_info_website(product_template_id, product_id, combination, add_qty, **kw)
        combination['carousel_variants_attr'] = request.env['ir.ui.view']._render_template('variants_attributes_ecommerce.ecom_show_extra_fields_product_variant', values={
                'product': request.env['product.template'].browse(combination['product_template_id']),
                'product_variant': request.env['product.product'].browse(combination['product_id']),
                'website': request.env['website'].get_current_website(),
            })
        return combination
