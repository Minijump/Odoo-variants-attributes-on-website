/** @odoo-module **/

import VariantMixin from 'sale.VariantMixin';
import { patch } from "@web/core/utils/patch";

patch(VariantMixin, "find_a_nice_name", {
    _onChangeCombination: function(ev, $parent, combination) {
        this._super(ev, $parent, combination);
        document.getElementsByClassName("custom_var_att")[0].innerHTML = combination.carousel_variants_attr 
        // !!check if there is no elements by class name
    }
});
