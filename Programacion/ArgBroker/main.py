from src.utils.mysql_connector import MySQLConnector
from src.dao.accion_dao import AccionDAO
from src.model.accion import Accion
from src.dao.cotizacion_diaria_dao import CotizacionDAO

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "kari2024"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
    try:
        cotizacion_dao = CotizacionDAO(connector)
        id_accion = 1  # Reemplaza con el id_accion que deseas consultar
        cotizaciones_diarias = cotizacion_dao.obtener_todos(id_accion)
        for cotizacion in cotizaciones_diarias:
                print(cotizacion)
    
         

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

    
