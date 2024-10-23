from src.utils.mysql_connector import MySQLConnector
from src.dao.accion_dao import AccionDAO
from src.model.cotizacion_diaria import CotizacionDiaria
from src.model.accion import Accion
from src.dao.cotizacion_diaria_dao import CotizacionDAO

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "kari2024"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
    nueva_cotizacion_macro = CotizacionDiaria(None, 2, '2024-10-22',4, 5, 6, 7, 8, 9, 10, 11)

    try:
        cargar_cotizacion = CotizacionDAO(connector)
        cargar_cotizacion.crear(nueva_cotizacion_macro)
        
    except Exception as error:
        print(f"Error: {error}")



if __name__ == "__main__":

    main()


    """
    host = "junction.proxy.rlwy.net"
    database = "railway"
    user = "root"
    password = "GhsHCPaNwJHOlpNepUsFVXoAyVZfDnGI"
    port = 47364

    # Crear conector MySQL
    mysql_connector = MySQLConnector(host, database, user, password, port)
    """

    
