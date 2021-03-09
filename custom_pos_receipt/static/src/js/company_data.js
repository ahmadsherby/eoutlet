odoo.define('ks_pos_low_stock_alert.ks_low_stock', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var _super_ordermodel = models.Order.prototype;
    models.load_fields('res.company', ['fox_town_name','fox_address','fox_vat_number','fox_phone','fox_email']);
    models.Order = models.Order.extend({
        export_for_printing: function(){
            var receipt = _super_ordermodel.export_for_printing.apply(this, arguments);
            receipt.company.fox_town_logo = '/web/image?model=res.company&field=fox_town_logo&id=1&unique=1';
            receipt.company.fox_town_name = this.pos.company.fox_town_name;
            receipt.company.fox_address = this.pos.company.fox_address;
            receipt.company.fox_vat_number = this.pos.company.fox_vat_number;
            receipt.company.fox_phone = this.pos.company.fox_phone;
            receipt.company.fox_email = this.pos.company.fox_email;
            return receipt;
        },
    });


});