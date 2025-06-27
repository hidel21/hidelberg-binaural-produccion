#!/bin/bash

# Nombre del contenedor Odoo
CONTAINER="hidelberg-binaural-produccion-odoo-1"
DB_NAME="testing"
ADMIN_PASS="odoo"

# Módulos con pruebas unitarias
MODULES_WITH_TEST=("meses_garantia")

# Módulos sin pruebas unitarias (solo instalación)
MODULES_WITHOUT_TEST=("clasificacion_fiscal" "numero_mesa" "recordatorio_cumpleaños" "verificacion_calidad")

# Eliminar base de datos anterior si existe
echo "🧹 Eliminando base de datos $DB_NAME si existe..."
docker exec -u postgres ${CONTAINER/-odoo-1/-db-1} \
    psql -U odoo -c "DROP DATABASE IF EXISTS $DB_NAME;" > /dev/null

# Ejecutar pruebas en módulos con test
for mod in "${MODULES_WITH_TEST[@]}"; do
  echo "🚀 Ejecutando pruebas para $mod"
  docker exec -u odoo -it $CONTAINER \
    odoo -d $DB_NAME -w $ADMIN_PASS -i $mod \
    --test-enable --without-demo=true --stop-after-init --log-level=test
done

# Instalar módulos sin pruebas solo para validar que cargan correctamente
for mod in "${MODULES_WITHOUT_TEST[@]}"; do
  echo "📦 Instalando módulo sin test: $mod"
  docker exec -u odoo -it $CONTAINER \
    odoo -d $DB_NAME -w $ADMIN_PASS -i $mod \
    --without-demo=true --stop-after-init --log-level=info
done

echo "✅ Pruebas completadas para todos los módulos."
