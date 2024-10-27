from src.acceso_a_datos.inversor_dao import InversorDAO
from src.acceso_a_datos.accion_dao import Acciondao
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
from src.acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
from src.acceso_a_datos.historial_saldo_dao import HistorialSaldoDAO
import os

class Menu:
    def __init__ (self, base_de_datos, COMISION_BROKER):
        self.__base_de_datos = base_de_datos
        self.__comision_broker = COMISION_BROKER
        self.__usuario_autenticado = None
        self._portafolio_inversor = EstadoPortafolioDAO(self.__base_de_datos)
        self._historial_saldo_inversor = HistorialSaldoDAO(self.__base_de_datos)
        self.ejecutando = True
    

    def __limpiar_consola(self):
        if os.name == 'nt':
            os.system('cls')


    def mostrar_menu_principal(self): #Menu principal
        while self.ejecutando: True
        self.__limpiar_consola()
        print("=== ARGBroker ===\n")
        print("1. Iniciar Sesion") #servicio de iniciar_sesion
        print("2. Registrarse") #servicio de autenticacion
        print("0. Salir")
        
        opcion = input("Seleccione una opción: \n")
            
        if opcion == "1":
            self.__mostrar_panel_iniciar_sesion() 
        if opcion == "2":
            self.__registrar_usuario()
        elif opcion == "0":
            self.ejecutando = False
        else:
            input("Opción inválida. Seleccione una opción para continuar...")


    def __mostrar_panel_iniciar_sesion(self):
            self.__limpiar_consola()
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
        self.__limpiar_consola()
    
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
                     
    def _mostrar_panel_de_inversor(self): #Menu de inversor 
        self.__limpiar_consola()
        while True:
            print("=== PANEL DE INVERSOR ===\n") 
            print("1. Datos Personales") 
            print("2. Mi Portafolio") 
            print("3. Transacciones")
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self._mostrar_mis_datos()
            elif opcion == "2":
                self._mostrar_portafolio()
            elif opcion == "3":
                self._mostrar_transacciones()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def _mostrar_mis_datos(self): 
        self.__limpiar_consola()
        print("=== OBTENER DATOS DE INVERSOR === \n")
        print (f'id del inversosr: {self.InversorDAO.id_inversor}')
        print(f'Nombre: {self.InversorDAO.apellido}, {self.InversorDAO.nombre}')
        print(f'Email: {self.InversorDAO.email}')
        print(f'Saldo actual: {self.InversorDAO.saldo_cuenta}')

       
    def _actualizar_datos(self):
       self.__limpiar_consola()
       print("=== ACTUALIZAR DATOS DE INVERSOR === \n")
       nuevo_correo_elecrtonico = input("Ingrese nuevo email: ")
       self.InversorDAO.email = nuevo_correo_elecrtonico
       
    def _mostrar_portafolio(self): 
        self.__limpiar_consola()
        while True:
            print("=== PORTAFOLIO ===\n") 
            print("1. Mis acciones") 
            print("2. Historial") 
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self._mostrar_acciones()
            elif opcion == "2":
                self._mostrar_historial()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")  


    def _mostrar_acciones(self):
         acciones_en_haber_del_inversor = self._estado_portafolio_dao.obtener_todos(self.__usuario_autenticado._id_inversor)
         for accion in acciones_en_haber_del_inversor:
              print(accion)


    def _mostrar_historial(self):
         historial_de_inversor = self._estado_portafolio_dao.obtener_todos(self.__usuario_autenticado._id_inversor)
         for historial in historial_de_inversor:
          print(historial)

    

    def _mostrar_transacciones(self):
         self.__limpiar_consola()
    while True:
            print("=== TRANSACCIONES ===\n") 
            print("1. Acciones Disponibles") 
            print("2. Comprar")
            print("3. Vender") 
            print("4. Comision Broker")
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self._mostrar_acciones_disponibles()
            elif opcion == "2":
                self._comprar_acciones()
            elif opcion == "3":
                self._vender_acciones()
            elif opcion == "4":
                self._ver_comosiones_broker()
            elif opcion == "o":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")  

         
