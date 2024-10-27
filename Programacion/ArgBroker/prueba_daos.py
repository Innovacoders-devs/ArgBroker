from src.herramientas.conector_a_mysql import MySQLConnector
from src.acceso_a_datos.historial_saldo_dao import HistorialSaldoDAO
from src.acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from src.acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
from src.modelo.inversor import Inversor
from src.modelo.accion import Accion
from src.servicios.servicio_de_venta import VenderAccion
from src.servicios.servicio_de_compra import CompraAccion
from decimal import Decimal

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_demo_bdd"
    usuario = "root"
    contrasena = "redcros62"

    connector = MySQLConnector(host, base_datos, usuario, contrasena)

    try:
        # Instanciar los DAOs
        dao_historial_saldo = HistorialSaldoDAO(connector)
        dao_cotizacion_diaria = CotizacionDAO(connector)
        dao_estado_portafolio = EstadoPortafolioDAO(connector)
        dao_transaccion = TransaccionDAO(connector)

        # Datos de prueba
        inversor = Inversor(id_inversor=1, saldo_cuenta=Decimal('1000000.00'))  # Ajustado según la definición de Inversor
        accion_involucrada = Accion(id_accion=1, nombre_accion="YPF S.A.", simbolo_accion="YPF")
        cantidad_acciones = 10
        comision_broker = Decimal('0.01')  # Convertir a Decimal

        # Compra de acciones
        compra_accion = CompraAccion(inversor, connector, accion_involucrada, cantidad_acciones, comision_broker)

        # Obtener y mostrar el estado del portafolio antes de la compra
        estado_portafolio_antes_compra = dao_estado_portafolio.obtener_uno(inversor.id_inversor)
        print(f"Acciones antes de la compra:\n {estado_portafolio_antes_compra}")

        # Realizar la compra
        if compra_accion.realizar_compra():
            print("Compra realizada con éxito")

        # Obtener y mostrar el estado del portafolio después de la compra
        estado_portafolio_despues_compra = dao_estado_portafolio.obtener_uno(inversor.id_inversor)
        print(f"Acciones después de la compra: \n{estado_portafolio_despues_compra}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
