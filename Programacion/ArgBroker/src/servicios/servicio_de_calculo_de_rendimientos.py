class ServiciodeCalculodeRendimientos:
    def __init__(self, transaccion_dao, cotizacion_dao):
        self.transaccion_dao = transaccion_dao
        self.cotizacion_dao = cotizacion_dao

    def calcular_rendimiento_por_accion(self, id_portafolio, id_accion):
        transacciones = self.transaccion_dao.obtener_por_portafolio_y_accion(id_portafolio, id_accion)
        ultima_cotizacion = self.cotizacion_dao.obtener_ultima_cotizacion(id_accion)

        if not transacciones or not ultima_cotizacion:
            return 0

        transacciones_compra = [transaccion for transaccion in transacciones if transaccion.tipo == 'compra']
        total_comprado = sum(transaccion.precio * transaccion.cantidad for transaccion in transacciones_compra)
        cantidad_comprada = sum(transaccion.cantidad for transaccion in transacciones_compra)
        precio_compra_promedio = total_comprado / cantidad_comprada if cantidad_comprada > 0 else 0

        precio_actual = ultima_cotizacion.precio_compra_actual
        rendimiento = (precio_actual - precio_compra_promedio) * cantidad_comprada

        return rendimiento
