/** @odoo-module **/

import VariantMixin from "@website_sale/js/variant_mixin";
import { patch } from "@web/core/utils/patch";

patch(VariantMixin, "variantMixinPatchVariantsAttributes", {
    _onChangeCombination: function(ev, $parent, combination) {
        this._super(ev, $parent, combination);
        console.log("hey");
        console.log(document);
        // document.getElementsByClassName("custom_var_att")[0].innerHTML = combination.carousel_variants_attr 
    }
    
});

// const OriginalOnchangeCombination = VariantMixin._onChangeCombination;
// VariantMixin._onChangeCombination = function (ev, $parent, combination) {
//     this._super(ev, $parent, combination);
//     console.log("hey");
//     console.log(document);
//     document.getElementsByClassName("custom_var_att")[0].innerHTML = combination.carousel_variants_attr
//     OriginalOnchangeCombination.apply(this, [ev, $parent, combination]);
// };
