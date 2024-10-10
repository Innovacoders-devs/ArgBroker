from src.utils.mysql_connector import MySQLConnector

if __name__ == "__main__":
    host = "127.0.0.1"
    database = "arg_broker_bdd"
    user = "root"
    password = "redcros62"

    mysql_connector = MySQLConnector(host, database, user, password)
    
    """
    host = "junction.proxy.rlwy.net"
    database = "railway"
    user = "root"
    password = "GhsHCPaNwJHOlpNepUsFVXoAyVZfDnGI"
    port = 47364

    # Crear conector MySQL
    mysql_connector = MySQLConnector(host, database, user, password, port)
    """

    
    try:
        mysql_connector.connect()
        
        query = "SELECT DATABASE();"
        resultado = mysql_connector.fetch_one(query)

        if resultado:
            print(f"Conectado a la base de datos: {resultado[0]}")
        else:
            print("No se pudo obtener el nombre de la base de datos.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        mysql_connector.disconnect()