from datetime import datetime
from decimal import Decimal
from ..modelo.transaccion import Transaccion
from ..modelo.historial_saldo import HistorialSaldo

class ServiciodeCompra:
    def __init__(self, dao_historial_saldo, dao_cotizacion_diaria, dao_estado_portafolio, dao_transaccion, comision_broker):
        self.__dao_historial_saldo = dao_historial_saldo
        self.__dao_cotizacion_diaria = dao_cotizacion_diaria
        self.__dao_estado_portafolio = dao_estado_portafolio
        self.__dao_transaccion = dao_transaccion
        self.__comision_broker = Decimal(comision_broker)
    
    def __calcular_monto_compra(self, accion, cantidad):
        ultima_cotizacion = self.__dao_cotizacion_diaria.obtener_ultima_cotizacion(accion.id_accion)
        precio_compra_actual = Decimal(ultima_cotizacion.precio_compra_actual)
        monto_compra = precio_compra_actual * cantidad
        comision = monto_compra * self.__comision_broker
        monto_total = monto_compra + comision
        return monto_total, comision

    def __verificar_saldo_suficiente(self, inversor, monto_total):
        if inversor.saldo_cuenta < monto_total:
            raise ValueError("No es posible realizar la compra porque no hay suficiente saldo en la cuenta")

    def __obtener_fecha_actual(self):
        return datetime.now().strftime('%Y-%m-%d')

    def realizar_compra(self, inversor, accion, cantidad):
        monto_total, comision = self.__calcular_monto_compra(accion, cantidad)
        self.__verificar_saldo_suficiente(inversor, monto_total)

        try:
            saldo_anterior = inversor.saldo_cuenta
            inversor.saldo_cuenta -= monto_total

            estado_portafolio = self.__dao_estado_portafolio.obtener_uno(inversor.id_inversor)
            estado_portafolio.cantidad += cantidad
            self.__dao_estado_portafolio.actualizar(estado_portafolio, estado_portafolio.id_estado_portafolio)

            fecha_actual = self.__obtener_fecha_actual()
            saldo_nuevo = inversor.saldo_cuenta
            motivo_historial = f"compra {accion.nombre_accion}"

            historial_saldo = HistorialSaldo(
                id_inversor=inversor.id_inversor,
                fecha=fecha_actual,
                saldo_anterior=saldo_anterior,
                saldo_nuevo=saldo_nuevo,
                motivo=motivo_historial
            )
            self.__dao_historial_saldo.crear(historial_saldo)

            transaccion = Transaccion(
                id_accion=accion.id_accion,
                tipo='compra',
                fecha=fecha_actual,
                precio=monto_total / cantidad,
                cantidad=cantidad,
                comision=comision,
                id_portafolio=inversor.id_inversor
            )
            self.__dao_transaccion.crear(transaccion)

            return True
        except Exception as e:
            raise ValueError(f"No se pudo realizar la compra: {e}")