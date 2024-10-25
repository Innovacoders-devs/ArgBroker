import traceback
from src.controller.broker_controller import ControladorBroker
from src.DAO.inversor_dao import InversorDAO
from src.DAO.accion_dao import AccionDAO
from src.DAO.portafolio_dao import PortafolioDAO
from src.DAO.transaccion_dao import TransaccionDAO
from src.utils.mysql_connector import MySQLConnector
from src.model.accion import Accion

class Menu:
    def __init__ (self):

        def mostrar_menu_principal(self):
            while self.ejecutando:
                print("\n=== ARGBroker ===")
                print("1. Iniciar Sesion")
                print("2. Registrarse")
                print("0. Salir")


        opcion = input("\nSeleccione una opción: ")
            
        if opcion == "1":
                    self.iniciar_sesion()
        if opcion == "2":
                    self.registrar_usuario()
        elif opcion == "0":
                    self.ejecutando = False
        else:
                    input("Opción inválida. Seleccione una opción para continuar...")

        try:
                correo_electronico = input("Ingrese email del inversor: ")
                contrasenia_ingresada = input("Ingrese su contraseña: ")
               
                if not correo_electronico or not contrasenia_ingresada:
                            raise ValueError("El email y la contraseña no pueden estar vacíos")
                if correo_electronico == self.inversor.email and contrasenia_ingresada == self.inversor.contrasena:
                            return self.mostrar_menu_inversor()
                else:
                    raise ValueError("Credenciales incorrectas")
        except ValueError as error:
                print(f"Error de autenticación: {str(error)}")
                return False





