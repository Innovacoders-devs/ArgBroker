"""from src.herramientas.conector_a_mysql import MySQLConnector
from src.acceso_a_datos.accion_dao import AccionDAO
from src.modelo.cotizacion_diaria import CotizacionDiaria
from src.modelo.accion import Accion
from src.acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO


def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "redcros62"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
 

    try:
        cargar_cotizacion = CotizacionDAO(connector)
        cotizacion = cargar_cotizacion.obtener_todos(1)
        for e in cotizacion:
            print("\n")
            print(e)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":

    main()"""


"""
    host = "junction.proxy.rlwy.net"
    database = "railway"
    user = "root"
    password = "GhsHCPaNwJHOlpNepUsFVXoAyVZfDnGI"
    port = 47364

    # Crear conector MySQL
    mysql_connector = MySQLConnector(host, database, user, password, port)
    """

from src.Vista.Menu import Menu

menu = Menu()
menu.mostrar_menu_principal()