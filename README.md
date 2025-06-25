# 🧪 Módulos desarrollados por Hidelberg Martínez

Este repositorio agrupa cinco módulos personalizados para Odoo 17, probados en Docker, que añaden funcionalidades de contabilidad, RRHH, POS, control de calidad y garantías.

---

## 📦 Módulos

- **account_fiscal_classification**  
  Clasificación fiscal en facturas.
- **hr_birthday_reminder**  
  Recordatorio de cumpleaños vía email.
- **pos_table_number**  
  Número de mesa en órdenes POS.
- **stock_quality_check**  
  Validación de calidad en transferencias de inventario.
- **product_warranty**  
  Gestión y propagación de garantía en ventas.

---

## ⚙️ Instalación

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/hidel21/hidelberg-binaural-produccion.git
   cd hidelberg-binaural-produccion
   ```

2. **Ejecutar el instalador**

   ```bash
   ./install.sh
   ```
3. **Acceder a Odoo**

   * Navegar a: `http://localhost:8069`
   * Crear base de datos (p. ej. `binaural_test`)
   * Activar modo desarrollador
   * Actualizar lista de módulos e instalar los desarrollados

---

## ✅ Pruebas funcionales manuales

### 1. **account\_fiscal\_classification**

#### Instalación y verificación

* Ajustes ▶ Actualizar lista de módulos
* Buscar “Clasificación Fiscal en Facturas”
* Confirmar módulo instalado

#### Flujo de facturas

1. Contabilidad ▶ Facturas ▶ Crear
2. Completar Cliente, Producto, Cantidad y Precio
3. Verificar campo **Clasificación Fiscal** (“A” por defecto)
4. Cambiar a “B” y “C” → guardar

#### Validación de lista y reporte

* Comprobar columna “Clasificación Fiscal” y filtros (A/B/C)
* Imprimir reporte ▶ confirmar línea “Clasificación Fiscal: A/B/C”

#### Casos y permisos

* Facturas tipo cliente/proveedor, validar/anular
* Historial de cambios en chatter
* Pruebas con distintos usuarios y roles

---

### 2. **hr\_birthday\_reminder**

#### Configuración

* RRHH ▶ Empleados ▶ verificar módulo
* Ajustes ▶ Técnico ▶ Acciones Programadas ▶ “Recordatorio de Cumpleaños”

  * Intervalo: diario
  * Forzar ejecución ▶ sin errores

#### Verificación de envío

* Ajustes ▶ Técnico ▶ Correos Salientes

  * Asunto, destinatario y contenido (nombre y fecha)
* Chatter del empleado ▶ registro de envío

#### Casos y permisos

* Empleados sin correo o fecha
* Cumpleaños hoy/mañana
* Acceso con usuario no administrador

---

### 3. **pos\_table\_number**

#### En POS

* Abrir sesión ▶ crear orden
* Ver campo “Número de mesa” ▶ ingresar y guardar
* Imprimir recibo ▶ “Número de Mesa: X”
* Ventas ▶ Órdenes POS ▶ filtro y edición

#### Casos especiales

* Formatos “01”, “12A”, “123456”
* Orden sin número
* Cambio de número tras creación
* Chatter registra cambios

---

### 4. **stock\_quality\_check**

#### Preparación

* Ajustes ▶ Empresa ▶ activar “Requerir Verificación de Calidad”

#### Flujo de transferencias

1. Inventario ▶ Transferencias ▶ crear
2. Estado “En espera” hasta verificar
3. Botón “Verificar Calidad” ▶ aprobar/rechazar
4. Validar transferencia cuando esté aprobada

#### Casos y historial

* Desactivar verificación ▶ validar directamente
* Múltiples transferencias
* Chatter con resultado, fecha, usuario, notas

---

### 5. **product\_warranty**

#### Configuración

* Productos ▶ crear “Producto de Prueba”

  * Tipo: Almacenable
  * Meses de garantía: 0, 1, 6, 12, 24

#### Flujo en ventas

* Ventas ▶ Pedidos ▶ añadir producto
* Confirmar campo garantía en línea de pedido
* Probar cambios en producto y ver actualización

#### Historial

* Chatter registra usuario, fecha y cambios

---

## 📁 Estructura del proyecto

```text
.
├── install.sh
├── docker-compose.yml
├── scripts/
│   └── test_all.sh        # Opcional: ejecutar todas las pruebas
└── src/
    ├── account_fiscal_classification/
    ├── hr_birthday_reminder/
    ├── pos_table_number/
    ├── stock_quality_check/
    └── product_warranty/
```

---

## 📬 Contacto

Desarrollado por **Hidelberg Martínez**
GitHub: [@hidel21](https://github.com/hidel21)