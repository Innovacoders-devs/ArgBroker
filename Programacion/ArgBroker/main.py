from src.herramientas.conector_a_mysql import MySQLConnector
from src.acceso_a_datos.accion_dao import AccionDAO
from src.model.cotizacion_diaria import CotizacionDiaria
from src.model.accion import Accion
from src.acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from src.model.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO
from src.services.inversor_servicio import InversorServicio

def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "kari2024"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
    nueva_cotizacion_macro = CotizacionDiaria(1, 3, '2024-10-22',4, 5, 6, 7, 8, 9, 10, 11,12)

    try:
        cargar_cotizacion = CotizacionDAO(connector)
        cargar_cotizacion.crear(nueva_cotizacion_macro)

    except Exception as error:
        print(f"Error: {error}")


def registrar_usuario():
    inversorDAO = InversorDAO()
    servicio_inversor = InversorServicio(inversorDAO)

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su cuil: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    try:
        nuevo_inversor = servicio_inversor.registrar_usuario(nombre, apellido, cuil, email, contrasena)
        print(f"El usuario {nuevo_inversor.nombre} ha sido registrado con éxito")
    except ValueError as eroor:
        print(f"Error en el registro: {error}")
    

def iniciar_sesion():
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    inversorDAO = InversorDAO()
    servicio_inversor = InversorServicio(inversorDAO)

    try:
        if servicio_inversor.iniciar_sesion(email, contrasena):
            print("Inicio de sesión exitoso")
        else:
            print("Error en el inicio de sesión")
    except ValueError as error:
        print(f"Error en el inicio de sesión: {error}")


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

    
