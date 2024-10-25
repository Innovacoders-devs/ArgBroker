-- INSERTS

INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta) 
VALUES 
('Roberto', 'Sánchez', '20-33445566-7', 'roberto.sanchez@gmail.com', 'pass123', 250000.00),
('Patricia', 'Gómez', '27-22334455-8', 'patricia.gomez@gmail.com', 'pass456', 180000.00);


INSERT INTO portafolio (id_inversor) 
SELECT id_inversor 
FROM inversor 
WHERE email IN ('roberto.sanchez@gmail.com', 'patricia.gomez@gmail.com');


INSERT INTO accion (nombre_accion, simbolo_accion) 
VALUES 
('Vista Oil & Gas', 'VIST'),
('Central Puerto', 'CEPU');


INSERT INTO cotizacion_diaria 
(id_accion, fecha, ultimo_operado, cantidad_compra_diaria, precio_compra_actual, 
precio_venta_actual, cantidad_venta_diaria, valor_apertura, minimo_diario, 
maximo_diario, valor_cierre) 
VALUES 
((SELECT id_accion FROM accion WHERE simbolo_accion = 'VIST'),
'2024-10-17', 800.50, 100, 800.00, 801.00, 95, 799.00, 798.00, 802.00, 800.50),
((SELECT id_accion FROM accion WHERE simbolo_accion = 'CEPU'),
'2024-10-17', 450.75, 150, 450.00, 451.50, 140, 449.00, 448.00, 452.00, 450.75);


INSERT INTO transaccion (id_portafolio, id_accion, cantidad, precio, tipo, fecha)
SELECT 
    p.id_portafolio,
    a.id_accion,
    50,
    cd.precio_compra_actual,
    'compra',
    '2024-10-17 15:00:00'
FROM inversor i
JOIN portafolio p ON i.id_inversor = p.id_inversor
CROSS JOIN accion a
JOIN cotizacion_diaria cd ON a.id_accion = cd.id_accion
WHERE i.email = 'roberto.sanchez@gmail.com'
AND a.simbolo_accion = 'VIST'
AND cd.fecha = '2024-10-17';

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
WHERE id_accion = (SELECT id_accion FROM accion WHERE simbolo_accion = 'VIST')
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
WHERE id_accion = (SELECT id_accion FROM accion WHERE simbolo_accion = 'VIST')
AND fecha = '2024-10-17';

-- SELECTS SIMPLES
-- 1. Mostrar información de los nuevos inversores
SELECT nombre, apellido, email, saldo_cuenta
FROM inversor
WHERE email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com');

-- 2. Ver cotización actual de las nuevas acciones
SELECT a.simbolo_accion, cd.ultimo_operado, cd.precio_compra_actual, cd.precio_venta_actual
FROM accion a
JOIN cotizacion_diaria cd ON a.id_accion = cd.id_accion
WHERE a.simbolo_accion IN ('VIST', 'CEPU')
AND cd.fecha = '2024-10-17';

-- 3. Verificar transacciones realizadas hoy
SELECT a.simbolo_accion, t.cantidad, t.precio, t.tipo, t.fecha
FROM transaccion t
JOIN accion a ON t.id_accion = a.id_accion
WHERE DATE(t.fecha) = '2024-10-17';

-- 4. Revisar saldos actualizados después de operaciones
SELECT nombre, apellido, saldo_cuenta
FROM inversor
WHERE email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com');

-- 5. Verificar disponibilidad de acciones para compra
SELECT a.simbolo_accion, cd.cantidad_compra_diaria, cd.precio_compra_actual
FROM accion a
JOIN cotizacion_diaria cd ON a.id_accion = cd.id_accion
WHERE a.simbolo_accion IN ('VIST', 'CEPU')
AND cd.fecha = '2024-10-17';

-- CONSULTAS MULTITABLA

-- 1. Verificar inversión inicial de los nuevos inversores
-- Esta consulta nos permite ver cuánto han invertido los nuevos inversores
-- en su primera compra de acciones y qué porcentaje de su saldo representa
SELECT 
    i.nombre,
    i.apellido,
    a.simbolo_accion,
    t.cantidad,
    t.precio,
    (t.cantidad * t.precio) as monto_invertido,
    i.saldo_cuenta,
    ROUND((t.cantidad * t.precio / i.saldo_cuenta) * 100, 2) as porcentaje_saldo_invertido
FROM inversor i
JOIN portafolio p ON i.id_inversor = p.id_inversor
JOIN transaccion t ON p.id_portafolio = t.id_portafolio
JOIN accion a ON t.id_accion = a.id_accion
WHERE i.email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com')
AND DATE(t.fecha) = '2024-10-17';

-- 2. Analizar rendimiento inicial de las nuevas acciones
-- Esta consulta muestra la variación de precio de las nuevas acciones
-- comparando su precio de apertura con el último precio operado
SELECT 
    a.simbolo_accion,
    cd.valor_apertura,
    cd.ultimo_operado,
    cd.ultimo_operado - cd.valor_apertura as variacion_absoluta,
    ROUND(((cd.ultimo_operado - cd.valor_apertura) / cd.valor_apertura) * 100, 2) as variacion_porcentual
FROM accion a
JOIN cotizacion_diaria cd ON a.id_accion = cd.id_accion
WHERE a.simbolo_accion IN ('VIST', 'CEPU')
AND cd.fecha = '2024-10-17';

-- 3. Resumen de operaciones del día para nuevos inversores
-- Esta consulta proporciona un resumen de todas las operaciones realizadas
-- por los nuevos inversores, incluyendo el volumen operado y el monto total
SELECT 
    i.nombre,
    i.apellido,
    COUNT(t.id_transaccion) as cantidad_operaciones,
    SUM(t.cantidad) as total_acciones,
    SUM(t.cantidad * t.precio) as monto_total,
    a.simbolo_accion
FROM inversor i
JOIN portafolio p ON i.id_inversor = p.id_inversor
JOIN transaccion t ON p.id_portafolio = t.id_portafolio
JOIN accion a ON t.id_accion = a.id_accion
WHERE i.email IN ('roberto.sanchez.nuevo@gmail.com', 'patricia.gomez@gmail.com')
AND DATE(t.fecha) = '2024-10-17'
GROUP BY i.nombre, i.apellido, a.simbolo_accion;