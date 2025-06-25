odoo.define('pos_table_number.models', function (require) {
    "use strict";

    const models = require('point_of_sale.models');
    const PosOrder = models.Order;

    models.Order = PosOrder.extend({
        initialize: function () {
            PosOrder.prototype.initialize.apply(this, arguments);
            this.table_number = this.table_number || "";
        },

        export_as_JSON: function () {
            const json = PosOrder.prototype.export_as_JSON.apply(this, arguments);
            json.table_number = this.table_number;
            return json;
        },

        init_from_JSON: function (json) {
            PosOrder.prototype.init_from_JSON.apply(this, arguments);
            this.table_number = json.table_number;
        },
    });
});
