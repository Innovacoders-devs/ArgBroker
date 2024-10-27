-- INSERTS
INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta) 
VALUES 
('Roberto', 'Sánchez', '20-33445566-7', 'roberto.sanchez@gmail.com', 'pass123', 250000.00),
('Patricia', 'Gómez', '27-22334455-8', 'patricia.gomez@gmail.com', 'pass456', 180000.00);

INSERT INTO portafolio (id_inversor) 
SELECT inversor.id_inversor 
FROM inversor 
WHERE inversor.email IN ('roberto.sanchez@gmail.com', 'patricia.gomez@gmail.com');

INSERT INTO accion (nombre_accion, simbolo_accion) 
VALUES 
('Vista Oil & Gas', 'VIST'),
('Central Puerto', 'CEPU');

INSERT INTO cotizacion_diaria 
(id_accion, fecha, ultimo_operado, cantidad_compra_diaria, precio_compra_actual, 
precio_venta_actual, cantidad_venta_diaria, valor_apertura, minimo_diario, 
maximo_diario, valor_cierre) 
VALUES 
((SELECT accion.id_accion FROM accion WHERE accion.simbolo_accion = 'VIST'),
'2024-10-17', 800.50, 100, 800.00, 801.00, 95, 799.00, 798.00, 802.00, 800.50),
((SELECT accion.id_accion FROM accion WHERE accion.simbolo_accion = 'CEPU'),
'2024-10-17', 450.75, 150, 450.00, 451.50, 140, 449.00, 448.00, 452.00, 450.75);

INSERT INTO estado_portafolio (id_portafolio, id_accion, nombre_accion, simbolo_accion, cantidad, valor_actual) 
SELECT 
    portafolio.id_portafolio,
    accion.id_accion,
    accion.nombre_accion,
    accion.simbolo_accion,
    50,
    cotizacion_diaria.precio_compra_actual
FROM inversor
JOIN portafolio ON inversor.id_inversor = portafolio.id_inversor
CROSS JOIN accion
JOIN cotizacion_diaria ON accion.id_accion = cotizacion_diaria.id_accion
WHERE inversor.email = 'roberto.sanchez@gmail.com'
AND accion.simbolo_accion = 'VIST'
AND cotizacion_diaria.fecha = '2024-10-17';

-- UPDATES
-- 1. Actualizar saldo después de la compra de acciones para Roberto
UPDATE inversor 
SET saldo_cuenta = saldo_cuenta - (50 * 800.00)
WHERE email = 'roberto.sanchez@gmail.com';

-- 2. Actualizar precio de la nueva acción VIST
UPDATE cotizacion_diaria 
SET ultimo_operado = 805.00,
    precio_compra_actual = 804.50,
    precio_venta_actual = 805.50
WHERE id_accion = (SELECT accion.id_accion FROM accion WHERE accion.simbolo_accion = 'VIST')
AND fecha = '2024-10-17';

-- 3. Modificar datos de contacto de nuevo inversor
UPDATE inversor 
SET email = 'roberto.sanchez.nuevo@gmail.com'
WHERE email = 'roberto.sanchez@gmail.com';

-- 4. Actualizar contraseña del nuevo inversor
UPDATE inversor 
SET contrasena = 'newpass'
WHERE email = 'patricia.gomez@gmail.com';

-- 5. Ajustar cantidad de acciones disponibles para compra
UPDATE cotizacion_diaria 
SET cantidad_compra_diaria = cantidad_compra_diaria - 50
WHERE id_accion = (SELECT accion.id_accion FROM accion WHERE accion.simbolo_accion = 'VIST')
AND fecha = '2024-10-17';

-- SELECTS SIMPLES
-- 1. Mostrar información de los nuevos inversores
SELECT nombre, apellido, email, saldo_cuenta
FROM inversor
WHERE email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com');

-- 2. Ver cotización actual de las nuevas acciones
SELECT accion.simbolo_accion, cotizacion_diaria.ultimo_operado, cotizacion_diaria.precio_compra_actual, cotizacion_diaria.precio_venta_actual
FROM accion
JOIN cotizacion_diaria ON accion.id_accion = cotizacion_diaria.id_accion
WHERE accion.simbolo_accion IN ('VIST', 'CEPU')
AND cotizacion_diaria.fecha = '2024-10-17';

-- 3. Verificar transacciones realizadas hoy (incluyendo comision)
SELECT accion.simbolo_accion, transaccion.cantidad, transaccion.precio, transaccion.tipo, transaccion.fecha, transaccion.comision
FROM transaccion
JOIN accion ON transaccion.id_accion = accion.id_accion
WHERE DATE(transaccion.fecha) = '2024-10-17';

-- 4. Revisar saldos actualizados después de operaciones
SELECT nombre, apellido, saldo_cuenta
FROM inversor
WHERE email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com');

-- 5. Verificar disponibilidad de acciones para compra
SELECT accion.simbolo_accion, cotizacion_diaria.cantidad_compra_diaria, cotizacion_diaria.precio_compra_actual
FROM accion
JOIN cotizacion_diaria ON accion.id_accion = cotizacion_diaria.id_accion
WHERE accion.simbolo_accion IN ('VIST', 'CEPU')
AND cotizacion_diaria.fecha = '2024-10-17';

-- CONSULTAS MULTITABLA

-- 1. Verificar inversión inicial de los nuevos inversores (incluyendo comision)
-- Esta consulta nos permite ver cuánto han invertido los nuevos inversores
-- en su primera compra de acciones y qué porcentaje de su saldo representa
SELECT 
    inversor.nombre,
    inversor.apellido,
    accion.simbolo_accion,
    transaccion.cantidad,
    transaccion.precio,
    transaccion.comision,
    (transaccion.cantidad * transaccion.precio) as monto_invertido,
    inversor.saldo_cuenta,
    ROUND((transaccion.cantidad * transaccion.precio / inversor.saldo_cuenta) * 100, 2) as porcentaje_saldo_invertido
FROM inversor
JOIN portafolio ON inversor.id_inversor = portafolio.id_inversor
JOIN transaccion ON portafolio.id_portafolio = transaccion.id_portafolio
JOIN accion ON transaccion.id_accion = accion.id_accion
WHERE inversor.email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com')
AND DATE(transaccion.fecha) = '2024-10-17';

-- 2. Analizar rendimiento inicial de las nuevas acciones
-- Esta consulta muestra la variación de precio de las nuevas acciones
-- comparando su precio de apertura con el último precio operado
SELECT 
    accion.simbolo_accion,
    cotizacion_diaria.valor_apertura,
    cotizacion_diaria.ultimo_operado,
    cotizacion_diaria.ultimo_operado - cotizacion_diaria.valor_apertura as variacion_absoluta,
    ROUND(((cotizacion_diaria.ultimo_operado - cotizacion_diaria.valor_apertura) / cotizacion_diaria.valor_apertura) * 100, 2) as variacion_porcentual
FROM accion
JOIN cotizacion_diaria ON accion.id_accion = cotizacion_diaria.id_accion
WHERE accion.simbolo_accion IN ('VIST', 'CEPU')
AND cotizacion_diaria.fecha = '2024-10-17';

-- 3. Resumen de operaciones del día para nuevos inversores (incluyendo comision)
-- Esta consulta proporciona un resumen de todas las operaciones realizadas
-- por los nuevos inversores, incluyendo el volumen operado y el monto total
SELECT 
    inversor.nombre,
    inversor.apellido,
    COUNT(transaccion.id_transaccion) as cantidad_operaciones,
    SUM(transaccion.cantidad) as total_acciones,
    SUM(transaccion.cantidad * transaccion.precio) as monto_total,
    SUM(transaccion.comision) as total_comision,
    accion.simbolo_accion
FROM inversor
JOIN portafolio ON inversor.id_inversor = portafolio.id_inversor
JOIN transaccion ON portafolio.id_portafolio = transaccion.id_portafolio
JOIN accion ON transaccion.id_accion = accion.id_accion
WHERE inversor.email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com')
AND DATE(transaccion.fecha) = '2024-10-17'
GROUP BY inversor.nombre, inversor.apellido, accion.simbolo_accion;