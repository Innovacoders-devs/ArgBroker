from datetime import datetime
from decimal import Decimal
from ..acceso_a_datos.historial_saldo_dao import HistorialSaldoDAO
from ..acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from ..acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
from ..acceso_a_datos.transaccion_dao import TransaccionDAO
from ..modelo.transaccion import Transaccion
from ..modelo.historial_saldo import HistorialSaldo

class CompraAccion:
    def __init__(self, inversor, conector_a_base_datos, accion, cantidad, comision_broker):
        self.__inversor = inversor
        self.__conector_a_base_datos = conector_a_base_datos
        self.__accion = accion
        self.__cantidad = cantidad
        self.__comision_broker = Decimal(comision_broker)
        self.__dao_historial_saldo = HistorialSaldoDAO(self.__conector_a_base_datos)
        self.__dao_cotizacion_diaria = CotizacionDAO(self.__conector_a_base_datos)
        self.__dao_estado_portafolio = EstadoPortafolioDAO(self.__conector_a_base_datos)
        self.__dao_transaccion = TransaccionDAO(self.__conector_a_base_datos)
    
    def calcular_monto_compra(self):
        ultima_cotizacion = self.__dao_cotizacion_diaria.obtener_ultima_cotizacion(self.__accion.id_accion)
        precio_compra_actual = Decimal(ultima_cotizacion.precio_compra_actual)
        monto_compra = precio_compra_actual * self.__cantidad
        comision = monto_compra * self.__comision_broker
        monto_total = monto_compra + comision
        return monto_total, comision

    def verificar_saldo_suficiente(self, monto_total):
        if self.__inversor.saldo_cuenta < monto_total:
            raise ValueError("No es posible realizar la compra porque no hay suficiente saldo en la cuenta")

    def obtener_fecha_actual(self):
        return datetime.now().strftime('%Y-%m-%d')

    def realizar_compra(self):
        monto_total, comision = self.calcular_monto_compra()
        self.verificar_saldo_suficiente(monto_total)

        try:
            saldo_anterior = self.__inversor.saldo_cuenta
            self.__inversor.saldo_cuenta -= monto_total

            estado_portafolio = self.__dao_estado_portafolio.obtener_uno(self.__inversor.id_inversor)
            estado_portafolio.cantidad += self.__cantidad
            self.__dao_estado_portafolio.actualizar(estado_portafolio, estado_portafolio.id_estado_portafolio)

            fecha_actual = self.obtener_fecha_actual()
            saldo_nuevo = self.__inversor.saldo_cuenta
            motivo_historial = f"compra {self.__accion.nombre_accion}"

            historial_saldo = HistorialSaldo(
                id_inversor=self.__inversor.id_inversor,
                fecha=fecha_actual,
                saldo_anterior=saldo_anterior,
                saldo_nuevo=saldo_nuevo,
                motivo=motivo_historial
            )
            self.__dao_historial_saldo.crear(historial_saldo)

            transaccion = Transaccion(
                id_accion=self.__accion.id_accion,
                tipo='compra',
                fecha=fecha_actual,
                precio=monto_total / self.__cantidad,
                cantidad=self.__cantidad,
                comision=comision,
                id_portafolio=self.__inversor.id_inversor
            )
            self.__dao_transaccion.crear(transaccion)

            return True
        except Exception as e:
            raise ValueError(f"No se pudo realizar la compra: {e}")
