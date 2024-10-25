from src.dao.inversor_dao import InversorDAO
from src.dao.accion_dao import Acciondao
from src.dao.portafolio_dao import PortafolioDAO
from src.dao.transaccion_dao import TransaccionDAO


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

    def registrar_usuario(self):
            print("\n=== CREAR NUEVO INVERSOR ===")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            cuil = input("CUIL: ")
            email = input("Email: ")
            contrasenia = input("Contraseña: ")
               
            print("\nInversor creado exitosamente!")


    def mostrar_menu_inversor(self):
        while True:
            print("\n=== Portal inversor ===")
            print("1. Inversiones")
            print("2. Acciones")
            print("3. Portafolio")
            print("4. Transacciones")
            print("5. Cotizaciones")
            print("0. Salir")

            opcion = input("\n Seleccione una opción: ")

            if opcion == "1":
                self.menu_inversor()
            elif opcion == "2":
                self.menu_accion()
            elif opcion == "3":
                self.menu_portafolio()
            elif opcion == "4":
                self.menu_transaccion()
            elif opcion == "5":
                self.menu_cotizacion()
            elif option == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def menu_inversor(self):
            while True:
                self.clear_screen()
                print("\n=== GESTIÓN DE INVERSORES ===")
                print("1. Crear nuevo inversor")
                print("2. Obtener datos de inversor")
                print("3. Actualizar inversor")
                print("4. Eliminar inversor")
                print("5. Buscar inversor por email")
                print("6. Autenticar inversor")
                print("0. Volver al menú principal")

                option = input("\nSeleccione una opción: ")

                if option == "0":
                    break
                elif option == "1":
                    self.crear_inversor()
                elif option == "2":
                    self.obtener_inversor()
                input("\nPresione Enter para continuar...")

        def menu_acciones(self):
            while True:
                self.clear_screen()
                print("\n=== GESTIÓN DE ACCIONES ===")
                print("1. Crear nueva acción")
                print("2. Obtener datos de acción")
                print("3. Actualizar acción")
                print("4. Eliminar acción")
                print("5. Obtener última cotización")
                print("0. Volver al menú principal")

                option = input("\nSeleccione una opción: ")

                if option == "0":
                    break
                input("\nPresione Enter para continuar...")

        def menu_portafolio(self):
            while True:
                self.clear_screen()
                print("\n=== GESTIÓN DE PORTAFOLIO ===")
                print("1. Crear nuevo portafolio")
                print("2. Obtener portafolio")
                print("3. Actualizar portafolio")
                print("4. Eliminar portafolio")
                print("5. Obtener portafolio por inversor")
                print("0. Volver al menú principal")

                option = input("\nSeleccione una opción: ")

                if option == "0":
                    break

                input("\nPresione Enter para continuar...")








