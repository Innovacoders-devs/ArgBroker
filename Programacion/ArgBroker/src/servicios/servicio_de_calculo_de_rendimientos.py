from decimal import Decimal
from datetime import datetime

class ServiciodeCalculodeRendimientos:
    def __init__(self, transaccion_dao, cotizacion_dao):
        self.transaccion_dao = transaccion_dao
        self.cotizacion_dao = cotizacion_dao

    def calcular_rendimiento_por_accion(self, id_portafolio, id_accion):
        transacciones = self.transaccion_dao.obtener_por_portafolio_y_accion(id_portafolio, id_accion)
        cotizaciones = self.cotizacion_dao.obtener_todos(id_accion)

        if not transacciones or not cotizaciones:
            return (0.0, 0.0), False

        # Filtrar cotizaciones posteriores a la fecha de la última transacción de compra
        ultima_transaccion_compra = max(transaccion.fecha for transaccion in transacciones if transaccion.tipo == 'compra')
        if isinstance(ultima_transaccion_compra, datetime):
            ultima_transaccion_compra = ultima_transaccion_compra.date()
        cotizaciones_filtradas = [cotizacion for cotizacion in cotizaciones if cotizacion.fecha > ultima_transaccion_compra]

        if not cotizaciones_filtradas:
            return (0.0, 0.0), False

        # Obtener precios de apertura y cierre
        precio_apertura = Decimal(cotizaciones_filtradas[0].valor_apertura)
        precio_cierre = Decimal(cotizaciones_filtradas[-1].valor_cierre)

        # Calcular rendimiento simple diario
        rendimiento_simple_diario = ((precio_cierre - precio_apertura) / precio_apertura) * 100

        # Calcular rendimiento acumulado
        transacciones_compra = [transaccion for transaccion in transacciones if transaccion.tipo == 'compra']
        total_comprado = sum(Decimal(transaccion.precio) * Decimal(transaccion.cantidad) for transaccion in transacciones_compra)
        cantidad_comprada = sum(Decimal(transaccion.cantidad) for transaccion in transacciones_compra)
        precio_compra_promedio = total_comprado / cantidad_comprada if cantidad_comprada > 0 else Decimal(0)
        rendimiento_acumulado = ((precio_cierre - precio_compra_promedio) / precio_compra_promedio) * 100

        return {
            'rendimiento_simple_diario': float(rendimiento_simple_diario),
            'rendimiento_acumulado': float(rendimiento_acumulado)
        }, True

    def calcular_rendimiento_por_accion_sin_cierre(self, id_portafolio, id_accion):
        transacciones = self.transaccion_dao.obtener_por_portafolio_y_accion(id_portafolio, id_accion)
        cotizaciones = self.cotizacion_dao.obtener_todos(id_accion)

        if not transacciones or not cotizaciones:
            return (0.0, 0.0), False

        # Filtrar cotizaciones posteriores a la fecha de la última transacción de compra
        ultima_transaccion_compra = max(transaccion.fecha for transaccion in transacciones if transaccion.tipo == 'compra')
        if isinstance(ultima_transaccion_compra, datetime):
            ultima_transaccion_compra = ultima_transaccion_compra.date()
        cotizaciones_filtradas = [cotizacion for cotizacion in cotizaciones if cotizacion.fecha > ultima_transaccion_compra]

        if not cotizaciones_filtradas:
            return (0.0, 0.0), False

        # Obtener precio de apertura
        precio_apertura = Decimal(cotizaciones_filtradas[0].valor_apertura)

        # Calcular rendimiento simple diario
        rendimiento_simple_diario = ((precio_apertura - precio_apertura) / precio_apertura) * 100  # Esto siempre será 0

        # Calcular rendimiento acumulado
        transacciones_compra = [transaccion for transaccion in transacciones if transaccion.tipo == 'compra']
        total_comprado = sum(Decimal(transaccion.precio) * Decimal(transaccion.cantidad) for transaccion in transacciones_compra)
        cantidad_comprada = sum(Decimal(transaccion.cantidad) for transaccion in transacciones_compra)
        precio_compra_promedio = total_comprado / cantidad_comprada if cantidad_comprada > 0 else Decimal(0)
        rendimiento_acumulado = ((precio_apertura - precio_compra_promedio) / precio_compra_promedio) * 100

        return {
            'rendimiento_simple_diario': float(rendimiento_simple_diario),
            'rendimiento_acumulado': float(rendimiento_acumulado)
        }, True

    def calcular_rendimiento_total(self, id_portafolio):
        transacciones = self.transaccion_dao.obtener_por_portafolio(id_portafolio)
        if not transacciones:
            return Decimal(0.0), Decimal(0.0), False

        transacciones_compra = [transaccion for transaccion in transacciones if transaccion.tipo == 'compra']
        if not transacciones_compra:
            return Decimal(0.0), Decimal(0.0), False

        total_invertido = sum(Decimal(transaccion.precio) * Decimal(transaccion.cantidad) for transaccion in transacciones_compra)
        rendimiento_total = Decimal(0.0)
        hay_cotizaciones_posteriores = False

        acciones = set(transaccion.id_accion for transaccion in transacciones_compra)
        for id_accion in acciones:
            ultima_cotizacion = self.cotizacion_dao.obtener_ultima_cotizacion(id_accion)
            if ultima_cotizacion:
                transacciones_accion = [transaccion for transaccion in transacciones_compra if transaccion.id_accion == id_accion]
                ultima_transaccion_compra = max(transaccion.fecha for transaccion in transacciones_accion)
                if isinstance(ultima_transaccion_compra, datetime):
                    ultima_transaccion_compra = ultima_transaccion_compra.date()
                cotizaciones_filtradas = [cotizacion for cotizacion in self.cotizacion_dao.obtener_todos(id_accion) if cotizacion.fecha > ultima_transaccion_compra]

                if not cotizaciones_filtradas:
                    continue

                hay_cotizaciones_posteriores = True
                cantidad_comprada = sum(Decimal(transaccion.cantidad) for transaccion in transacciones_accion)
                precio_compra_promedio = sum(Decimal(transaccion.precio) * Decimal(transaccion.cantidad) for transaccion in transacciones_accion) / cantidad_comprada
                precio_actual = Decimal(cotizaciones_filtradas[-1].valor_cierre)
                rendimiento_total += (precio_actual - precio_compra_promedio) * cantidad_comprada

        if not hay_cotizaciones_posteriores:
            return total_invertido, Decimal(0.0), True

        return total_invertido, rendimiento_total, True