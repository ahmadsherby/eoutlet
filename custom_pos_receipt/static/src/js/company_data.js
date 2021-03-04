/*
    @Author: KSOLVES India Private Limited
    @Email: sales@ksolves.com
*/

odoo.define('ks_pos_low_stock_alert.ks_low_stock', function (require) {
    "use strict";

    var pos_model = require('point_of_sale.models');
    pos_model.load_fields("res.company", "fox_town_name");
    var ks_super_pos = pos_model.PosModel.prototype;
//    ks_models.PosModel = ks_models.PosModel.extend({
//
//        initialize: function (session, attributes) {
//            this.ks_load_product_quantity_after_product();
//            ks_super_pos.initialize.call(this, session, attributes);
//        },
//        });
return  ks_super_pos;

});