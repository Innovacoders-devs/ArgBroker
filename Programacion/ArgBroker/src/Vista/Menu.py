from src.acceso_a_datos.inversor_dao import InversorDAO
from src.acceso_a_datos.accion_dao import AccionDAO
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
import os

class Menu:
    def __init__ (self):
        self.ejecutando = True
    

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')


    def mostrar_menu_principal(self):
        while self.ejecutando: 
            self.clear_screen()
            print("\n" + "=" * 30)
            print("         🌟 ARGBroker 🌟         ")
            print("=" * 30)
            print(" 1️⃣  Iniciar Sesion")
            print(" 2️⃣  Registrarse")
            print(" 0️⃣  Salir")


            opcion = input("Seleccione una opción: \n")
            
            if opcion == "1":
                self.iniciar_sesion() 
            if opcion == "2":
                self.registrar_usuario()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Seleccione una opción para continuar...")


    def iniciar_sesion(self):
            self.clear_screen()
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
        self.clear_screen()
        print("=== REGISTRARSE ===\n")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cuil = input("CUIL: ")
        email = input("Email: ")
        contrasenia = input("Contraseña: ")

        print("Inversor creado exitosamente!\n")
        if nombre is not None and apellido is not None and cuil is not None and email is not None and contrasenia is not None:
             return self.iniciar_sesion()
                     
    def mostrar_menu_inversor(self): 
        self.clear_screen()
        while True:
            print("=== PANEL DE INVERSOR ===\n") 
            print("1. Datos Personales") 
            print("2. Mis Acciones") 
            print("3. Portafolio") # quiza convenga hacer un solo menu que contenga mi portafolio donde muestre:las acciones que tengo compradas y el historial de transacciones 
            print("4. Transacciones")
            print("5. Cotizaciones") #las cotizaciones se deberian poder ver en el panel de compra/venta menu que no esta, y se podria llamar operar 
            print("6. Eliminar inversor") #deseo eliminar mi cuenta (en ese caso deberian volver al panel principal luego de preguntar si esta seguro ya que la accion es irreversible)
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

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
            elif opcion == "6":
                self.eliminar_inversor()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def menu_inversor(self): #el menu se llama inversiones en el panel, menu inversor en el metodo pero implementa submenus relacionados a gestionar inversores, quiza deba ser un menu personal donde pueda ver y modificar mis datos o simplemente verlos 
            while True:
                self.clear_screen() #clear screen todavia no existe como metodo 
                print("=== Menú Personal === \n") 
                print("1. Mostrar mis datos") #mostrar mis datos (del inversor que inicio sesion)
                print("2. Actualizar mis datos") #actualizar mis datos
                print("0. Volver al menú principal")

                option = input("Seleccione una opción: \n")

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
                print("1. Crear nuevo portafolio") # segun la base de datos actualmente un usuario solo puede tener un solo portafolio por lo que no deberia permitir crear otro para el mismo usuario
                print("2. Obtener portafolio") #obtener potafolio es algo que la app deberia hacer y mostrar por si sola no dar una opcion
                print("3. Actualizar portafolio") #la app no permite actualizar el portafolio manualmente, lo hace cuando el inversor opera
                print("4. Eliminar portafolio") #el portafolio no se puede eliminar por si mismo, se elimina en cascada junto con el usuario
                print("5. Obtener portafolio por inversor") #no se pueden ver otros portafolios
                print("0. Volver al menú principal")

                option = input("\nSeleccione una opción: ")

                if option == "0":
                    break

                input("\nPresione Enter para continuar...")
    
    def menu_transacciones(self):
        while True:
            self.clear_screen()
            print("\n=== GESTIÓN DE TRANSACCIONES ===")
            print("1. Crear nueva transacción") #crear una nueva transaccion no es posible desde el panel del usuario ya que estas se crean cuando el usuario compra y vende una accion
            print("2. Obtener transacción") #el panel deberia mostrar el historial de transacciones en pantalla, no dar una opcion para obtenerlas
            print("3. Actualizar transacción") #las transacciones no se pueden actualizar desde el panel esto romperia el programa!
            print("4. Eliminar transacción") #las transacciones no se pueden eliminar desde el panel imaginemos si yo pudiera ir a la pagina de la afip y borrar mis compras y ventas para no pagar impuestos, eso seria correcto?
            print("5. Obtener transacciones por inversor") #no deberia ser posible
            print("0. Volver al menú principal")
           
            option = input("\nSeleccione una opción: ")
           
            if option == "0":
                break
         
            input("\nPresione Enter para continuar...")


    def menu_cotizaciones(self): #este menu deberia integrar el panel de compra venta
        while True:
            self.clear_screen()
            print("\n=== GESTIÓN DE COTIZACIONES ===") 
            print("1. Crear nueva cotización")
            print("2. Obtener cotización")
            print("3. Actualizar cotización")
            print("4. Eliminar cotización")
            print("5. Obtener cotizaciones por acción")
            print("6. Obtener última cotización")
            print("0. Volver al menú principal")
           
            option = input("\nSeleccione una opción: ")
           
            if option == "0":
                break
        
            input("\nPresione Enter para continuar...")


    def obtener_inversor(self): #no es una funcionalidad prometida mostrar otros inversores, en principio solo es posible ver datos personales 
        print("\n=== OBTENER DATOS DE INVERSOR ===")
        id_inversor = input("Ingrese ID del inversor: ")
        print("\nDatos del inversor:")
        print("ID:", id_inversor)
        print("Nombre: Juan Ejemplo")
        print("Email: juan@ejemplo.com")


if __name__ == "__main__":
    menu = Menu()
    menu.show_main_menu()











