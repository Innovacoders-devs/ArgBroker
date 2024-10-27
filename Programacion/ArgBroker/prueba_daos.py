from src.herramientas.conector_a_mysql import MySQLConnector
from src.modelo.portafolio import Portafolio
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.modelo.transaccion import Transaccion
from src.acceso_a_datos.transaccion_dao import TransaccionDAO

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_demo_bdd"
    usuario = "root"
    contrasena = "redcros62"

    connector = MySQLConnector(host, base_datos, usuario, contrasena)
 
    try:
        dao_transaccion = TransaccionDAO(connector)
        nueva_transaccion = Transaccion(
            id_transaccion=None,
            id_accion=2,
            tipo='compra',
            fecha='2023-10-10',
            precio=100.50,
            cantidad=10,
            comision=1.50,
            id_portafolio=1
        )
        resultado = dao_transaccion.crear(nueva_transaccion)
        if resultado:
            print('Se creó la transacción')

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
