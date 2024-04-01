# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request, route, Controller

from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController


class WebsiteSaleVariantControllerVariantsAttr(WebsiteSaleVariantController):
    @http.route(['/sale/get_combination_info_website'], type='json', auth="public", methods=['POST'], website=True)
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        """Special route to use website logic in get_combination_info override.
        This route is called in JS by appending _website to the base route.
        """
        kw.pop('pricelist_id')
        combination = self.get_combination_info(product_template_id, product_id, combination, add_qty, request.website.get_current_pricelist(), **kw)

        if request.website.google_analytics_key:
            combination['product_tracking_info'] = request.env['product.template'].get_google_analytics_data(combination)

        if request.website.product_page_image_width != 'none' and not request.env.context.get('website_sale_no_images', False):
            carousel_view = request.env['ir.ui.view']._render_template('website_sale.shop_product_images', values={
                'product': request.env['product.template'].browse(combination['product_template_id']),
                'product_variant': request.env['product.product'].browse(combination['product_id']),
                'website': request.env['website'].get_current_website(),
            })
            carousel_view_variants_attr = request.env['ir.ui.view']._render_template('variants_attributes_ecommerce.ecom_show_extra_fields_product_variant2', values={
                'product': request.env['product.template'].browse(combination['product_template_id']),
                'product_variant': request.env['product.product'].browse(combination['product_id']),
                'website': request.env['website'].get_current_website(),
            })
            combination['carousel'] = carousel_view
            combination['carousel_variants_attr'] = carousel_view_variants_attr
        return combination
