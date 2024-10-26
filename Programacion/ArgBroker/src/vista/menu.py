from src.acceso_a_datos.inversor_dao import InversorDAO
from src.acceso_a_datos.accion_dao import Acciondao
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
from src.acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
import os

class Menu:
    def __init__ (self, base_de_datos, COMISION_BROKER):
        self.__base_de_datos = base_de_datos
        self.__comision_broker = COMISION_BROKER
        self.__usuario_autenticado = None
        self.__portafolio_inversor = EstadoPortafolioDAO(__base_de_datos)
        self.__historial_saldo_inversor = HistorialSaldoDAO(__base_de_datos)

        self.ejecutando = True
    

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')


    def mostrar_menu_principal(self): #Menu principal
        while self.ejecutando: True
        self.clear_screen()
        print("=== ARGBroker ===\n")
        print("1. Iniciar Sesion") #servicio de iniciar_sesion
        print("2. Registrarse") #servicio de autenticacion
        print("0. Salir")
        acciones_en_haber_del_inversor = self.__portafolio_inversor.obtener_todos(__usuario_autenticado._id_inversor)

        for iteracion in acciones_en_haber_del_inversor:
            print(iteracion.nombre,)



        opcion = input("Seleccione una opción: \n")
            
        if opcion == "1":
            self.mostrar_panel_iniciar_sesion() 
        if opcion == "2":
            self.registrar_usuario()
        elif opcion == "0":
            self.ejecutando = False
        else:
            input("Opción inválida. Seleccione una opción para continuar...")


    def mostrar_panel_iniciar_sesion(self):
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
             return self.servicio_de_autenticacion.autenticar_usuario(email, contrasenia)
        return self.iniciar_sesion()
                     
    def mostrar_panel_de_inversor(self): #Menu de inversor 
        self.clear_screen()
        while True:
            print("=== PANEL DE INVERSOR ===\n") 
            print("1. Datos Personales") 
            print("2. Mi Portafolio") 
            print("3. Transacciones")
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self.mostrar_mis_datos()
            elif opcion == "2":
                self.mostrar_portafolio()
            elif opcion == "3":
                self.mostrar_transacciones()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def mostrar_mis_datos(self): 
        self.clear_screen()
        print("=== OBTENER DATOS DE INVERSOR === \n")
        print (f'id del inversosr: {self.inversor.id_inversor}')
        print(f'Nombre: {self.inversor.apellido}, {self.inversor.nombre}')
        print(f'Email: {self.inversor.email}')
        print(f'Saldo actual: {self.inversor.saldo_cuenta}')

    


    

    
    def actualizar_datos(self):
       self.clear_screen()
       print("=== ACTUALIZAR DATOS DE INVERSOR === \n")
       nuevo_correo_elecrtonico = input("Ingrese nuevo email: ")
       self.inversor.email = nuevo_correo_elecrtonico
       