/** @odoo-module **/

import VariantMixin from "@website_sale/js/variant_mixin";
import publicWidget from "@web/legacy/js/public/public_widget";

/**
 * @param {MouseEvent} ev
 * @param {$.Element} $parent
 * @param {Array} combination
 */
VariantMixin._onChangeCombinationVariantsAttributes = function (ev, $parent, combination) {
    document.getElementsByClassName("custom_var_att")[0].innerHTML = combination.carousel_variants_attr
};

publicWidget.registry.WebsiteSale.include({
    /**
     * @override
     */
    _onChangeCombination: function () {
        this._super.apply(this, arguments);
        VariantMixin._onChangeCombinationVariantsAttributes.apply(this, arguments);
    },
});

export default VariantMixin;
