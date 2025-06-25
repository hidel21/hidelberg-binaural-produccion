# 🧪 Modulos Desarrollados por Hidelberg Martinez

Este repositorio contiene módulos desarrollados como parte del proceso técnico para Binaural, implementados sobre Odoo 17 y probados en entorno Docker.

---

## 📦 Módulos desarrollados

- `account_fiscal_classification`: Clasificación fiscal en facturas
- `hr_birthday_reminder`: Recordatorio de cumpleaños vía email
- `pos_table_number`: Número de mesa en órdenes POS
- `stock_quality_check`: Validación de calidad en transferencias de inventario
- `product_warranty`: Garantía de productos y propagación en ventas

---

## ⚙️ Instalación del entorno

1. Clona el repositorio:
   ```bash
   git clone https://github.com/hidel21/hidelberg-binaural-produccion.git
   cd hidelberg-binaural-produccion
````

2. Ejecuta el script de instalación:

   ```bash
   ./install.sh
   ```

3. Accede a Odoo:

   * Navegador: [http://localhost:8069](http://localhost:8069)
   * Crea una base de datos (ej: `binaural_test`)
   * Activa el modo desarrollador
   * Actualiza la lista de módulos e instala los desarrollados

---

## ✅ Pruebas Funcionales Manuales

**Guía de Pruebas Funcionales para Módulos Personalizados en Odoo 17**

---

### 1. account\_fiscal\_classification

#### Instalación y verificación del módulo

* Ir a **Ajustes > Actualizar lista de módulos**
* Buscar "Clasificación Fiscal en Facturas"
* Confirmar que el módulo está instalado

#### Crear y modificar facturas

* Ir a **Contabilidad > Facturas** y hacer clic en "Crear"
* Completar los campos básicos:

  * Cliente
  * Producto
  * Cantidad y precio
* Verificar que el campo **Clasificación Fiscal** tenga el valor por defecto "A"
* Cambiar el valor a "B" y guardar. Luego a "C" y guardar nuevamente

#### Verificación en vista lista

* Confirmar que la columna "Clasificación Fiscal" aparece y muestra el valor correcto
* Aplicar filtros: A, B y C. Confirmar que los resultados coinciden

#### Generación de reporte

* Seleccionar una factura y hacer clic en "Imprimir"
* Confirmar que aparece la línea:

  * "Clasificación Fiscal: A/B/C"

#### Pruebas adicionales

* Crear facturas de cliente y proveedor (out\_invoice, in\_invoice) y confirmar funcionamiento
* Validar y anular facturas. Confirmar que la clasificación se mantiene
* Confirmar que el historial (tracking) refleja cambios de clasificación
* Validar comportamiento con diferentes tipos de usuario y permisos

---

### 2. hr\_birthday\_reminder

#### Configuración inicial

* Ir a **RRHH > Empleados** y verificar instalación del módulo
* Confirmar que el correo de la empresa está configurado correctamente

#### Crear empleado de prueba

* Nombre: Empleado Prueba
* Fecha de cumpleaños: dentro de 7 días
* Correo: [prueba@empresa.com](mailto:prueba@empresa.com)

#### Verificación del cron

* Ir a **Ajustes > Técnico > Acciones Programadas**
* Buscar "Recordatorio de Cumpleaños"
* Confirmar que está activo, con intervalo diario y última ejecución reciente
* Forzar ejecución y verificar ausencia de errores

#### Verificar correo

* Ir a **Ajustes > Técnico > Correos > Correos Salientes**
* Confirmar:

  * Asunto correcto
  * Destinatario: [prueba@empresa.com](mailto:prueba@empresa.com)
  * Cuerpo contiene nombre y fecha de cumpleaños

#### Verificación en empleado

* Revisar pestaña **Notas** y chatter para confirmar registro del envío
* Validar comportamiento con:

  * Empleados sin correo
  * Sin fecha de cumpleaños
  * Cumpleaños hoy/mañana

#### Verificar permisos

* Probar con usuario no administrador
* Confirmar acceso a recordatorios y correos

---

### 3. pos\_table\_number

#### Configuración inicial

* Confirmar instalación del módulo y que el POS esté operativo

#### Crear orden en POS

* Abrir nueva orden, seleccionar producto
* Verificar presencia del campo/botón para ingresar número de mesa
* Ingresar número (ej: 12), guardar y verificar

#### Verificaciones visuales

* Confirmar que el prompt funciona
* Número visible en la orden

#### Verificar en recibo y factura

* Finalizar orden e imprimir recibo. Confirmar que aparece "Número de Mesa: 12"
* Ir a **Ventas > Facturas** y verificar que el número se mantiene

#### Verificar en backend POS

* Ir a **Ventas > Órdenes del POS**, buscar orden y verificar campo
* Probar filtros por número de mesa

#### Casos especiales

* Probar con formatos: "01", "12A", "123456"
* Crear orden sin número. Confirmar funcionamiento y que no se imprime nada
* Cambiar número luego de creada la orden. Confirmar actualización
* Validar persistencia tras cerrar y reabrir POS

#### Historial

* Confirmar que el chatter de la orden registra cambios con usuario y fecha

---

### 4. stock\_quality\_check

#### Configuración inicial

* En **Ajustes > Empresa**, activar "Requerir Verificación de Calidad"

#### Crear transferencia

* Ir a **Inventario > Transferencias**
* Crear nueva transferencia con productos
* Confirmar estado inicial "En espera" y no validable hasta verificar

#### Verificación de calidad

* Usar botón "Verificar Calidad" para abrir wizard
* Probar:

  * Aprobación: cambiar estado, agregar nota, permitir validación
  * Rechazo: cancelar transferencia, registrar nota

#### Validación

* Validar transferencia aprobada
* Intentar validar transferencia sin verificar y confirmar bloqueo

#### Casos especiales

* Desactivar "Requerir Verificación" y confirmar que ya no bloquea
* Probar con múltiples transferencias y diferentes productos

#### Historial

* Confirmar que el chatter muestra:

  * Resultado
  * Fecha
  * Usuario
  * Notas

---

### 5. product\_warranty

#### Configuración inicial

* Verificar instalación del módulo
* Ir a **Productos > Productos**

#### Crear producto con garantía

* Crear producto "Producto de Prueba" con:

  * Tipo: Almacenable
  * Meses de Garantía: 12
* Confirmar que el campo:

  * Está visible
  * Guarda correctamente
  * Se muestra en el chatter

#### Crear pedido de venta

* Ir a **Ventas > Pedidos de Venta**
* Agregar producto con garantía
* Confirmar:

  * Valor de garantía se refleja en la línea
  * Se mantiene tras guardar y editar

#### Casos especiales

* Crear productos con 0, 1, 6, 24 meses de garantía
* Confirmar propagación correcta en pedidos
* Cambiar garantía en producto y verificar impacto en pedidos

#### Verificación del historial

* Confirmar que los cambios se registran en el chatter con usuario y fecha


## 📁 Estructura del proyecto

```
├── install.sh
├── docker-compose.yml
├── scripts/
│   └── test_all.sh (opcional)
├── src/
│   ├── account_fiscal_classification/
│   ├── hr_birthday_reminder/
│   ├── pos_table_number/
│   ├── product_warranty/
│   └── stock_quality_check/
```

---

## 📬 Contacto

Desarrollado por **Hidelberg Martínez**
GitHub: [@hidel21](https://github.com/hidel21)