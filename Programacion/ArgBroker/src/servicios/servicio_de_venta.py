from datetime import datetime
from decimal import Decimal
from ..acceso_a_datos.historial_saldo_dao import HistorialSaldoDAO
from ..acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from ..acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
from ..acceso_a_datos.transaccion_dao import TransaccionDAO
from ..modelo.transaccion import Transaccion
from ..modelo.historial_saldo import HistorialSaldo

class VenderAccion:
    def __init__(self, inversor, conector_a_base_datos, accion_involucrada, cantidad_acciones, comision_broker):
        self.__inversor = inversor
        self.__conector_a_base_datos = conector_a_base_datos
        self.__accion_involucrada = accion_involucrada
        self.__cantidad_acciones_a_vender = cantidad_acciones
        self.__comision_broker = Decimal(comision_broker)
        self.__dao_historial_saldo = HistorialSaldoDAO(self.__conector_a_base_datos)
        self.__dao_cotizacion_diaria = CotizacionDAO(self.__conector_a_base_datos)
        self.__dao_estado_portafolio = EstadoPortafolioDAO(self.__conector_a_base_datos)
        self.__dao_transaccion = TransaccionDAO(self.__conector_a_base_datos)
        self.__monto_venta = None
    
    def calcular_monto_venta(self):
        ultima_cotizacion = self.__dao_cotizacion_diaria.obtener_ultima_cotizacion(self.__accion_involucrada.id_accion)
        precio_venta_actual = Decimal(ultima_cotizacion.precio_venta_actual)  
        comision = precio_venta_actual * self.__comision_broker
        monto_venta = precio_venta_actual + comision
        self.__monto_venta = monto_venta

    def verificar_cantidad_acciones(self):
        estado_portafolio = self.__dao_estado_portafolio.obtener_uno(self.__inversor.id_inversor)
        if estado_portafolio.cantidad < self.__cantidad_acciones_a_vender:
            raise ValueError("No es posible realizar la venta porque no hay suficientes acciones para vender")

    def obtener_fecha_actual(self):
        return datetime.now().strftime('%Y-%m-%d')

    def realizar_venta(self):
        self.verificar_cantidad_acciones()
        self.calcular_monto_venta()

        try:
            estado_portafolio = self.__dao_estado_portafolio.obtener_uno(self.__inversor.id_inversor)
            estado_portafolio.cantidad -= self.__cantidad_acciones_a_vender
            self.__dao_estado_portafolio.actualizar(estado_portafolio, estado_portafolio.id_estado_portafolio)

            fecha_actual = self.obtener_fecha_actual()
            saldo_nuevo = Decimal(self.__inversor.saldo_cuenta) + self.__monto_venta  # Convertir a Decimal
            motivo_historial = f"venta {self.__accion_involucrada.nombre_accion}"

            historial_saldo = HistorialSaldo(
                id_inversor=self.__inversor.id_inversor,
                fecha=fecha_actual,
                saldo_anterior=self.__inversor.saldo_cuenta,
                saldo_nuevo=saldo_nuevo,
                motivo= motivo_historial
            )
            self.__dao_historial_saldo.crear(historial_saldo)

            transaccion = Transaccion(
                id_accion=self.__accion_involucrada.id_accion,
                tipo='venta',
                fecha=fecha_actual,
                precio=self.__monto_venta,
                cantidad=self.__cantidad_acciones_a_vender,
                comision=self.__monto_venta * self.__comision_broker,
                id_portafolio=self.__inversor.id_inversor
            )
            self.__dao_transaccion.crear(transaccion)
            return True
        except Exception as e:
            raise ValueError(f"No se pudo realizar la venta: {e}")
