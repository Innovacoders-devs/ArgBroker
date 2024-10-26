from src.acceso_a_datos.inversor_dao import InversorDAO
from src.acceso_a_datos.accion_dao import Acciondao
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
import os

class Menu:
    def __init__ (self, base_de_datos, COMISION_BROKER):
        self.__base_de_datos = base_de_datos
        self.__comision_broker = COMISION_BROKER
        self.__usuario_autenticado = None
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
            self.servicio_de_inicio_sesion.iniciar_sesion()
            

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
                self.menu_accion()
            elif opcion == "3":
                self.menu_transaccion()
            elif opcion == "0":
                self.ejecutando = False
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def menu_inversor(self):
            while True:
                self.clear_screen() #clear screen todavia no existe como metodo 
                print("=== Menú Personal === \n") 
                print("1. Mostrar mis datos") #mostrar mis datos (del inversor que inicio sesion)
                print("2. Actualizar mis datos") #actualizar mis datos
                print("0. Volver al menú principal")

                opcion = input("Seleccione una opción: \n")

                if opcion == "0":
                    break
                elif opcion == "1":
                    self.mostrar_mis_datos()
                elif opcion == "2":
                    self.actualizar_datos()
                input("Presione Enter para continuar... \n")



    def menu_accion(self):
            while True:
                self.clear_screen()
                print("=== PORTAFOLIO === \n === GESTIÓN DE ACCIONES === \n") 
                print("1. Mostrar mi portafolio")
                print("2. Operar")
                print("0. Volver al menú principal")

                opcion = input("Seleccione una opción: \n")

                if opcion == "1":
                    self.mostrar_mis_acciones()
                elif opcion == "2":
                    self.cotizacion()
                if opcion == "0":
                    break
                input("Presione Enter para continuar... \n")


    def mostrar_mis_acciones(self):
        while True:
            self.clear_screen()
            print("=== MI PORTAFOLIO === \n")
            print(self.estado_portafolio.id_portafolio)
            print(self.accion.nombre_accion)
            print(self.accion.simbolo_accion)
            print(self.cotizacion_diaria.fecha)
            print(self.cotizacion_diaria.valor_apertura)
            print(self.cotizacion_diaria.valor_cierre)
            print(self.cotizacion_diaria.valor_maximo)
            print(self.cotizacion_diaria.valor_minimo)
            print(self.cotizacion_diaria.ultimo_operado)
            print(self.cotizacion_diaria.cantidad_compra_diaria)
            print(self.cotizacion_diaria.cantidad_venta_diaria)
            print(self.inversor.saldo_cuenta)

            acciones_a_realizar = input("Si desea comprar o vender acciones, presion 1; se desea volver al meniu anterior, presione 0: ")
            if acciones_a_realizar == "1":
                self.cotizacion()
            elif acciones_a_realizar == "0":
                break

        
    def cotizacion(self):
        while True:
            self.clear_screen()
            print(" === OPERAR === \n")
            print(self.accion.nombre_accion)
            print(self.accion.simbolo_accion)
            print(self.cotizacion_diaria.precio_compra_actual)
            print(self.cotizacion_diaria.precio_venta_actual)

            comprar_vender = input("Desea comprar o vender acciones? Seleccion 1 para comprar, 2 para vender, 0 para volver al menú principal: ")
            if comprar_vender == "1":
                cantidad_compra = int(input("Ingrese cantidad de acciones a comprar: "))
                saldo_actual = self.historial.saldo_anterior - (cantidad_compra * self.cotizacion_diaria.precio_compra_actual)
                transaccion_nueva = self.TransaccionDAO.crear()
                return f"Compra realizada con éxito! Transaccion n° {transaccion_nueva}. En este momento su saldo es de {saldo_actual} y la cantidad de acciones actual es de {self.portafolio.cantidad}"
            
            elif comprar_vender == "2":
                 cantidad_venta = int(input("ingrese la cantidad de acciones a vender: "))
                 saldo_actual = self.historial_saldo.saldo_anterior + (cantidad_venta * self.precio_venta_actual)
                 transaccion_nueva = self.TransaccionDAO.crear()
                 return f"Venta realizada con éxito!Transaccion n° {transaccion_nueva}. En este momento su saldo es de {saldo_actual} y la cantidad de acciones actual es de {self.portafolio.cantidad}"
           
            elif comprar_vender == "0":
                break 
           
#cada compra y cada venta genera una transaccion

    def menu_transaccion(self):
        while True:
            self.clear_screen()
            print("=== MIS TRANSACCIONES === \n")
            print("1. Mostrar transacciones")
            print("2. Eliminar transacciones") 
            print("0. Volver al menú principal")
           
            opcion = input("Seleccione una opción: \n")


            if opcion == "1":
                return f'Transacciones realizadas: {self.transaccion.id_transaccion}'
            if opcion == "2":
                 eliminar_transaccion = int(input("Ingrese el ID de la transaccion a eliminar: "))
                 confirmar = input(f"Esta seguro que desea eliminar la transaccion n° {eliminar_transaccion}? (s/n): ")
            if confirmar == "s":
                self.transaccion.id_transaccion.remove(eliminar_transaccion)
                return f"Transaccion eliminada con éxito! Transaccion n° {eliminar_transaccion}."
            else:
                return f"Transaccion n° {eliminar_transaccion} no eliminada."
            
            if opcion == "0":
                break
         
            input("Presione Enter para continuar...\n")


    def mostrar_mis_datos(self): 
        self.clear_screen()
        print("=== OBTENER DATOS DE INVERSOR === \n")
        id_inversor = input("Ingrese ID del inversor: ")
        print("Datos del inversor: \n")
        print("ID:", id_inversor)
        print("Nombre: Juan Ejemplo")
        print("Email: juan@ejemplo.com")

    
    def actualizar_datos(self):
       self.clear_screen()
       print("=== ACTUALIZAR DATOS DE INVERSOR === \n")
       nuevo_correo_elecrtonico = input("Ingrese nuevo email: ")
       self.inversor.email = nuevo_correo_elecrtonico
       

