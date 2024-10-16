from src.utils.mysql_connector import MySQLConnector


def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "redcros62"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)

    
    connector.conectar_a_base_datos()

    
    query = "SELECT * FROM inversor"  
    usuarios = connector.traer_todos(query)

    
    for usuario in usuarios:
        print(usuario)

    
    connector.desconectar_de_base_datos()





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

    
