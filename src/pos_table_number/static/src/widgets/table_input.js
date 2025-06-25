odoo.define('pos_table_number.table_input', function (require) {
    "use strict";

    const { Component } = owl;
    const { useState } = owl.hooks;
    const ProductScreen = require('point_of_sale.ProductScreen');

    const TableInput = Component.extend({
        template: 'TableInput',
        setup() {
            this.state = useState({
                tableNumber: this.env.pos.get_order().table_number || ''
            });
        },
        onChange(ev) {
            this.state.tableNumber = ev.target.value;
            this.env.pos.get_order().table_number = this.state.tableNumber;
        }
    });

    ProductScreen.addControlButton({
        component: TableInput,
        condition: () => true,
    });

    return TableInput;
});
