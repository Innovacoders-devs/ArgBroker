from src.utils.mysql_connector import MySQLConnector
from src.dao.accion_dao import AccionDAO
from src.model.accion import Accion

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "redcros62"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
    connector.conectar_a_base_datos()
    try:
        connector.conectar_a_base_datos()
        accion_dao = AccionDAO(connector)
        
        try:
            accion = accion_dao.obtener_uno(5)
            print(f"Accion obtenida: {accion}")
        except Exception as error:
            print(f"Error: {error}")

        try:
            nuevos_valores = Accion('Pampa Energia S.A.', 'PAMP')
            id_accion = 5
            
            accion_dao.actualizar(nuevos_valores, id_accion)

            accion_actualizada = accion_dao.obtener_uno(id_accion)
            print(f"Accion actualizada: {accion_actualizada}")
        except Exception as error:
            print(f"Error: {error}")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        connector.desconectar_de_base_datos()

    """     try:
        acciones = accion_dao.obtener_todos()
        for accion in acciones:
            print(f"Accion obtenida: {accion}")

    except Exception as error:
        print(f"Error: {error}") """

    

    """     accion_dao = AccionDAO(connector)
    try:
        accion = accion_dao.obtener_uno(100)  
        print(f"Accion obtenida: {accion}")
    except Exception as error:
        print(f"Error: {error}")
 """
    """     
    prueba = AccionDAO(connector)
    nueva_accion = Accion("Ternium Argentina S.A.", "TXAR")
    try:
        prueba.crear(nueva_accion)
        print("Accion creada exitosamente.")
    except Exception as e:
        print(e) """
    
    """ Consulta para crear un nuevo inversor, esta comentada para no crear el mismo usuario todas las veces que se ejecuta 

    consulta_para_crear_inversor = "INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta, intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    usuario_nuevo = ("Juan","Perez","20-12345678-9","juan.perez@example.com","12345",10000, 0)
    connector.ejecutar_consulta(consulta_para_crear_inversor, usuario_nuevo)
    """

    """ print('--------consulta para traer a todos los inversores--------\n')
    consulta = "SELECT * FROM inversor"  
    usuarios = connector.traer_todos(consulta)
    for usuario in usuarios:
        print(usuario)
    print('----------------\n')

    print('--------Todas las transacciones del inversor 1--------\n')
    consulta_para_traer_recibos = "SELECT * FROM transaccion WHERE id_inversor = %s"
    id_inversor = 1
    recibos = connector.traer_todos(consulta_para_traer_recibos, (id_inversor,))

    for recibo in recibos:
        print(recibo)
    print('----------------\n')

    print('--------Consulta para Traer una sola accion--------\n')
    consulta_para_traer_accion = "SELECT * FROM accion WHERE nombre_accion = %s"
    nombre_accion = 'Banco Macro S.A.'
    accion = connector.traer_solo_uno(consulta_para_traer_accion, (nombre_accion,))
    print(accion)
    print('----------------\n')

    connector.desconectar_de_base_datos() """

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

    
