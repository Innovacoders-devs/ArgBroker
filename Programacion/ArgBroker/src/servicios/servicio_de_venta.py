from datetime import datetime
from decimal import Decimal
from ..modelo.transaccion import Transaccion
from ..modelo.historial_saldo import HistorialSaldo

class ServiciodeVenta:
    def __init__(self, dao_historial_saldo, dao_cotizacion_diaria, dao_estado_portafolio, dao_transaccion, comision_broker):
        self.__dao_historial_saldo = dao_historial_saldo
        self.__dao_cotizacion_diaria = dao_cotizacion_diaria
        self.__dao_estado_portafolio = dao_estado_portafolio
        self.__dao_transaccion = dao_transaccion
        self.__comision_broker = Decimal(comision_broker)
        self.__monto_venta = None
    
    def __calcular_monto_venta(self, accion):
        ultima_cotizacion = self.__dao_cotizacion_diaria.obtener_ultima_cotizacion(accion.id_accion)
        precio_venta_actual = Decimal(ultima_cotizacion.precio_venta_actual)  
        comision = precio_venta_actual * self.__comision_broker
        monto_venta = precio_venta_actual - comision
        self.__monto_venta = monto_venta

    def __verificar_cantidad_acciones(self, inversor, cantidad_acciones):
        estado_portafolio = self.__dao_estado_portafolio.obtener_uno(inversor.id_inversor)
        if estado_portafolio.cantidad < cantidad_acciones:
            raise ValueError("No es posible realizar la venta porque no hay suficientes acciones para vender")

    def __obtener_fecha_actual(self):
        return datetime.now().strftime('%Y-%m-%d')

    def realizar_venta(self, inversor, accion, cantidad_acciones):
        self.__verificar_cantidad_acciones(inversor, cantidad_acciones)
        self.__calcular_monto_venta(accion)

        try:
            estado_portafolio = self.__dao_estado_portafolio.obtener_uno(inversor.id_inversor)
            estado_portafolio.cantidad -= cantidad_acciones
            self.__dao_estado_portafolio.actualizar(estado_portafolio, estado_portafolio.id_estado_portafolio)

            fecha_actual = self.__obtener_fecha_actual()
            saldo_nuevo = Decimal(inversor.saldo_cuenta) + self.__monto_venta  # Convertir a Decimal
            motivo_historial = f"venta {accion.nombre_accion}"

            historial_saldo = HistorialSaldo(
                id_inversor=inversor.id_inversor,
                fecha=fecha_actual,
                saldo_anterior=inversor.saldo_cuenta,
                saldo_nuevo=saldo_nuevo,
                motivo= motivo_historial
            )
            self.__dao_historial_saldo.crear(historial_saldo)

            transaccion = Transaccion(
                id_accion=accion.id_accion,
                tipo='venta',
                fecha=fecha_actual,
                precio=self.__monto_venta,
                cantidad=cantidad_acciones,
                comision=self.__monto_venta * self.__comision_broker,
                id_portafolio=inversor.id_inversor
            )
            self.__dao_transaccion.crear(transaccion)
            return True
        except Exception as e:
            raise ValueError(f"No se pudo realizar la venta: {e}")