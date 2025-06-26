#!/bin/bash

# Nombre del contenedor de Odoo
CONTAINER="hidelberg-binaural-produccion-odoo-1"

# Diccionario: módulo => nombre de la base de datos temporal
declare -A modules
modules=(
  ["product_warranty"]="test_db_pw"
  ["hr_birthday_reminder"]="test_db_birthday"
  ["account_fiscal_classification"]="test_db_account"
  ["pos_table_number"]="test_db_pos"
)

# Ejecutar tests para cada módulo
for module in "${!modules[@]}"; do
  db="${modules[$module]}"
  
  echo "🚀 Ejecutando tests para el módulo: $module"
  echo "📦 Usando base de datos temporal: $db"
  echo "----------------------------------------"
  
  docker exec -e ODOO_DISABLE_HTTP=1 -it "$CONTAINER" odoo \
    --init "$module" \
    -d "$db" \
    --test-enable \
    --log-level=test \
    --stop-after-init

  echo "✅ Finalizado módulo: $module"
  echo "========================================"
  echo ""
done
