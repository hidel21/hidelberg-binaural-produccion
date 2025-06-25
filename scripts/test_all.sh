#!/bin/bash
MODS=(account_fiscal_classification product_warranty_extension hr_birthday_reminder stock_quality_check pos_table_number)
for mod in "${MODS[@]}"; do
  echo "== Testing $mod =="
  docker exec -u odoo -it docker-odoo odoo -d testing -w odoo -i $mod --test-enable --without-demo=true --stop-after-init
done
