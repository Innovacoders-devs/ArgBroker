from src.utils.mysql_connector import MySQLConnector
from src.dao.accion_dao import AccionDAO
from src.model.accion import Accion

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "redcros62"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
    try:
        accion_dao = AccionDAO(connector)
        accion_dao.crear(('Patan SRL', 'PL'))
        acciones_de_bdd = accion_dao.obtener_todos()
        for accion in acciones_de_bdd:
            print(accion)


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

    
