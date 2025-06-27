
# 🧾 Módulos Odoo 17 desarrollados por Hidelberg Martínez

Este repositorio contiene una colección de módulos personalizados para Odoo 17, diseñados para ampliar funcionalidades clave en áreas como contabilidad, recursos humanos, punto de venta, inventario y gestión de productos. Todos los módulos han sido probados en un entorno Dockerizado.

---

## 📦 Lista de Módulos

| Módulo                  | Descripción                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `clasificacion_fiscal`  | Añade un campo de clasificación fiscal (A, B o C) en facturas               |
| `recordatorio_cumpleaños` | Envía correos recordatorios 7 días antes del cumpleaños de los empleados   |
| `numero_mesa`           | Permite agregar y mostrar el número de mesa en órdenes del Punto de Venta  |
| `verificacion_calidad`  | Incorpora una verificación de calidad en transferencias de inventario       |
| `meses_garantia`        | Propaga automáticamente los meses de garantía desde productos a ventas      |

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/hidel21/hidelberg-binaural-produccion.git
cd hidelberg-binaural-produccion
```

### 2. Levantar el entorno Docker

```bash
./install.sh
```

### 3. Acceder a Odoo

* URL: [http://localhost:8069](http://localhost:8069)
* Crear una base de datos (por ejemplo, `binaural_test`)
* Activar el modo desarrollador
* Actualizar la lista de módulos
* Instalar los módulos desarrollados

---

## 🧪 Pruebas Automatizadas

Cada módulo puede incluir su propio conjunto de pruebas funcionales. Para ejecutarlas:

```bash
docker exec -u odoo -it hidelberg-binaural-produccion-odoo-1 odoo \
  -d testing \
  -w odoo \
  -i <nombre_del_modulo> \
  --test-enable \
  --without-demo=true \
  --stop-after-init \
  --log-level=test
```

Reemplaza `<nombre_del_modulo>` por el nombre real del módulo, por ejemplo: `meses_garantia`.

---

## 🗂️ Estructura del Proyecto

```
.
├── docker-compose.yml           # Entorno de ejecución
├── Dockerfile                   # Imagen personalizada de Odoo
├── install.sh                   # Script de instalación rápida
├── odoo.conf                    # Configuración base de Odoo
├── test_module.sh               # Script opcional para pruebas
├── README.md                    # Este archivo
├── scripts/                     # Scripts auxiliares
└── src/                         # Módulos personalizados
    ├── clasificacion_fiscal/
    ├── meses_garantia/
    ├── numero_mesa/
    ├── recordatorio_cumpleaños/
    └── verificacion_calidad/
```

---

## 👤 Autor

**Hidelberg Efren Martínez Espitia**
📧 [hidelmartinez21@gmail.com](mailto:hidelmartinez21@gmail.com)
🌐 [https://github.com/hidel21](https://github.com/hidel21)