# Documentación del Modelo Relacional de ARGBrokerDemo

## Entidades Principales

### 1. inversor

Esta tabla almacena la información de los usuarios inversores del sistema.

#### Campos:
- id_inversor (PK): Identificador único del inversor.
- nombre: Nombre del inversor.
- apellido: Apellido del inversor.
- cuil: CUIL (Código Único de Identificación Laboral) del inversor.
- email: Correo electrónico del inversor.
- contrasena: Contraseña del inversor (se recomienda almacenar de forma encriptada).
- saldo_cuenta: Saldo actual en la cuenta del inversor.
- intentos_fallidos: Número de intentos fallidos de inicio de sesión.

### 2. portafolio

Esta tabla representa el portafolio de inversiones de cada inversor.

#### Campos:
- id_portafolio (PK): Identificador único del portafolio.
- id_inversor (FK): Referencia al inversor propietario del portafolio.

### 3. accion

Esta tabla contiene la información básica de las acciones disponibles en el sistema.

#### Campos:
- id_accion (PK): Identificador único de la acción.
- nombre_accion: Nombre de la empresa o del título de la acción.
- simbolo_accion: Símbolo o ticker de la acción en el mercado.

### 4. cotizacion_diaria

Esta tabla almacena las cotizaciones diarias de cada acción.

#### Campos:
- id_cotizacion (PK): Identificador único de la cotización.
- id_accion (FK): Referencia a la acción asociada.
- fecha: Fecha de la cotización.
- ultimo_operado: Último precio operado.
- cantidad_compra_diaria: Cantidad de acciones compradas en el día.
- precio_compra_actual: Precio actual de compra.
- precio_venta_actual: Precio actual de venta.
- cantidad_venta_diaria: Cantidad de acciones vendidas en el día.
- valor_apertura: Precio de apertura del día.
- minimo_diario: Precio mínimo del día.
- maximo_diario: Precio máximo del día.
- valor_cierre: Precio de cierre del día.

### 5. transaccion

Esta tabla registra todas las transacciones de compra y venta realizadas por los inversores.

#### Campos:
- id_transaccion (PK): Identificador único de la transacción.
- id_inversor (FK): Referencia al inversor que realizó la transacción.
- id_accion (FK): Referencia a la acción involucrada en la transacción.
- tipo: Tipo de transacción (compra o venta).
- fecha: Fecha y hora de la transacción.
- precio: Precio al que se realizó la transacción.
- cantidad: Cantidad de acciones involucradas en la transacción.
- comision: Comisión cobrada por la transacción.
- id_portafolio (FK): Referencia al portafolio asociado a la transacción.

### 6. historial_saldo

Esta tabla mantiene un registro histórico de los cambios en el saldo de la cuenta de cada inversor.

#### Campos:
- id_historial_saldo (PK): Identificador único del registro de historial.
- id_inversor (FK): Referencia al inversor asociado.
- fecha: Fecha y hora del cambio en el saldo.
- saldo_anterior: Saldo antes del cambio.
- saldo_nuevo: Saldo después del cambio.
- motivo: Descripción del motivo del cambio en el saldo.

## Relaciones y Funcionamiento

1. Cada Inversor puede tener un Portafolio (relación 1:1).
2. Un Portafolio está asociado a múltiples Transacciones (relación 1:N).
3. Cada Acción tiene múltiples registros de Cotización_diaria (relación 1:N).
4. Las Transacciones están asociadas a un Inversor, una Acción y un Portafolio específicos.
5. Cada Inversor tiene un historial de saldo asociado (relación 1:N).

Este diseño nos permite:
- Registrar y autenticar inversores.
- Mantener un registro actualizado de las cotizaciones de las acciones.
- Realizar y registrar transacciones de compra y venta de acciones.
- Mantener un portafolio actualizado para cada inversor.
- Llevar un historial detallado de los cambios en el saldo de cada inversor