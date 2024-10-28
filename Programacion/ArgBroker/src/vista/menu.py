from src.modelo.inversor import Inversor

from src.acceso_a_datos.inversor_dao import InversorDAO
from src.acceso_a_datos.accion_dao import AccionDAO
from src.acceso_a_datos.portafolio_dao import PortafolioDAO
from src.acceso_a_datos.transaccion_dao import TransaccionDAO
from src.acceso_a_datos.estado_portafolio_dao import EstadoPortafolioDAO
from src.acceso_a_datos.historial_saldo_dao import HistorialSaldoDAO
from src.acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO

from src.servicios.servicio_de_autenticacion import ServicioDeAutenticacion
from src.servicios.servicio_de_registro import ServicioDeRegistro
from src.servicios.servicio_de_calculo_de_rendimientos import ServiciodeCalculodeRendimientos
from src.servicios.servicio_de_compra import ServiciodeCompra
from src.servicios.servicio_de_venta import ServiciodeVenta

import os

class Menu:
    def __init__ (self, base_de_datos, COMISION_BROKER):
        self.__base_de_datos = base_de_datos
        self.__comision_broker = COMISION_BROKER
        self.__nuevo_inversor = None
        self.__usuario_autenticado = None

        self.inversor_dao = InversorDAO(self.__base_de_datos)
        self.accion_dao = AccionDAO(self.__base_de_datos)
        self.portafolio_dao = PortafolioDAO(self.__base_de_datos)
        self.transaccion_dao = TransaccionDAO(self.__base_de_datos)
        self.estado_portafolio_dao = EstadoPortafolioDAO(self.__base_de_datos)
        self.historial_saldo_dao = HistorialSaldoDAO(self.__base_de_datos)
        self.cotizacion_dao = CotizacionDAO(self.__base_de_datos)

        self.__servicio_de_registro = ServicioDeRegistro(self.inversor_dao)
        self.__servicio_de_autenticacion = ServicioDeAutenticacion(self.inversor_dao)
        self.__servicio_de_calculo_de_rendimientos = ServiciodeCalculodeRendimientos(self.transaccion_dao, self.cotizacion_dao)
        self.__servicio_de_compra = ServiciodeCompra(self.historial_saldo_dao, self.cotizacion_dao, self.estado_portafolio_dao, self.transaccion_dao, self.__comision_broker)
        self.__servicio_de_venta = ServiciodeVenta(self.historial_saldo_dao, self.cotizacion_dao, self.estado_portafolio_dao, self.transaccion_dao, self.__comision_broker)

        self.__ejecutando = True
    

    def __limpiar_consola(self):
        if os.name == 'nt':
            os.system('cls')


    def mostrar_menu_principal(self): 
        while self.__ejecutando: 
            self.__limpiar_consola()
            print("=== ARGBroker ===\n")
            print("1. Iniciar Sesion") 
            print("2. Registrarse") 
            print("0. Salir")
            
            opcion = input("Seleccione una opción: \n")
                
            if opcion == "1":
                self.__mostrar_panel_iniciar_sesion() 
            elif opcion == "2":
                self.__mostrar_panel_de_registro()
            elif opcion == "0":
                self.__ejecutando = False
            else:
                input("Opción inválida. Seleccione una opción para continuar...")


    def __mostrar_panel_de_registro(self):
        self.__limpiar_consola()
        print("=== PANEL DE REGISTRO ===\n")
        print("Ingrese los datos que se le piden a continuacion: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cuil = input("CUIL: ")
        email = input("Email: ")
        contrasenia = input("Contraseña: ")
        self.__nuevo_inversor = Inversor(nombre= nombre, apellido= apellido, cuil= cuil, email= email, contrasena= contrasenia)
        try:
           resultado = self.__servicio_de_registro.registrar_usuario(self.__nuevo_inversor)
           if resultado: 
               self.__limpiar_consola()
               submenu_registro = True
               print(f'Se registro el usuario exitosamente')
               while submenu_registro:
                opcion = input("Seleccione 1 para inicio de sesion, 2 para volver al menu principal \n o 3 para salir: ")

                if opcion == "1":
                        self.__mostrar_panel_iniciar_sesion() 
                        submenu_registro = False
                elif opcion == "2":
                        self.mostrar_menu_principal()
                        submenu_registro = False
                elif opcion == "3":
                        self.__ejecutando = False
                        submenu_registro = False
                else:
                    print("Opcion no valida, por favor ingrese una de las opciones ofrecidas")

        except Exception as e:
            print(f"Error al registrarse: {e}")
            opcion_del_submenu = True
            while opcion_del_submenu:
                eleccion = int(input("Ingrese 1 para intentar nuevamente, 2 para Salir: "))
                if eleccion == 1:
                    self.__mostrar_panel_de_registro()
                    opcion_del_submenu = False
                elif eleccion == 2:
                    self.__ejecutando = False
                    opcion_del_submenu = False
                else:
                    print("Ingrese una opcion valida")
            


    def __mostrar_panel_iniciar_sesion(self):
        self.__limpiar_consola()
        print("=== PANEL DE INICIO DE SESION ===")
        try:
            email = input("Ingrese email del inversor: ")
            contrasena = input("Ingrese su contraseña: ")
            
            self.__usuario_autenticado = self.__servicio_de_autenticacion.iniciar_sesion(email,contrasena)
            if self.__usuario_autenticado:
                self._mostrar_panel_de_inversor()
        except Exception as e:
            print(f'Ocurrio un error: {e}')
            opcion_del_submenu = True
            while opcion_del_submenu:
                eleccion = int(input("Ingrese 1 para intentar nuevamente, 2 para Salir: "))
                if eleccion == 1:
                    self.__mostrar_panel_iniciar_sesion()
                    opcion_del_submenu = False
                elif eleccion == 2:
                    self.__ejecutando = False
                    opcion_del_submenu = False
                else:
                    print("Ingrese una opcion valida")

                 

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
                self.__mostrar_panel_mis_datos()
            elif opcion == "2":
                self._mostrar_portafolio()
            elif opcion == "3":
                self._mostrar_transacciones()
            elif opcion == "0":
                self.__ejecutando = False
                break
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def __mostrar_panel_mis_datos(self):
        self.__limpiar_consola()
        print("=== MIS DATOS === \n")
        try:
            ultimo_saldo = self.historial_saldo_dao.buscar_ultimo_saldo(self.__usuario_autenticado.id_inversor)
            saldo_actual = ultimo_saldo.saldo_nuevo
        except Exception as e:
            saldo_actual = "No disponible"
            print(f"Error al obtener el saldo actual: {e}")

        print(f'id del inversor: {self.__usuario_autenticado.id_inversor}')
        print(f'Nombre: {self.__usuario_autenticado.apellido}, {self.__usuario_autenticado.nombre}')
        print(f'Email: {self.__usuario_autenticado.email}')
        print(f'Saldo actual: {saldo_actual}')
        input("Presione Enter para continuar...")

       
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
            print("3. Listar Activos")
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self._mostrar_acciones()
            elif opcion == "2":
                self._mostrar_historial()
            elif opcion == "3":
                self.__listar_activos_portafolio()
            elif opcion == "0":
                break
            else:
                input("Opción inválida. Presione Enter para continuar...")  


    def _mostrar_acciones(self):
        self.__limpiar_consola()
        print("=== MIS ACCIONES === \n")
        try:
            acciones_en_haber_del_inversor = self.estado_portafolio_dao.obtener_todos(self.__usuario_autenticado.id_inversor)
            if not acciones_en_haber_del_inversor:
                print("No se encontraron acciones en el portafolio.")
            else:
                for accion in acciones_en_haber_del_inversor:
                    print(f" Nombre: {accion._nombre_accion}, Símbolo: {accion._simbolo_accion}, Cantidad: {accion._cantidad}, Valor Actual: {accion._valor_actual}")
        except Exception as e:
            print(f"Error al obtener las acciones: {e}")
        input("Presione Enter para continuar...")

    def _mostrar_historial(self):
        self.__limpiar_consola()
        print("=== HISTORIAL DE TRANSACCIONES === \n")
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            transacciones = self.transaccion_dao.obtener_por_portafolio(portafolio.id_portafolio)
            if not transacciones:
                print("No hay transacciones disponibles.")
            else:
                for transaccion in transacciones:
                    print(f"ID Transacción: {transaccion.id_transaccion}")
                    print(f"Tipo: {transaccion.tipo}")
                    print(f"Fecha: {transaccion.fecha}")
                    print(f"Precio: {transaccion.precio}")
                    print(f"Cantidad: {transaccion.cantidad}")
                    print(f"Comisión: {transaccion.comision}")
                    print(f"ID Portafolio: {transaccion.id_portafolio}")
                    print("-" * 20)
        except Exception as e:
            print(f"Error al obtener el historial de transacciones: {e}")
        input("Presione Enter para continuar...")
        
    def __listar_activos_portafolio(self):
        self.__limpiar_consola()
        print("=== LISTA DE ACTIVOS DEL PORTAFOLIO === \n")
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            activos = self.estado_portafolio_dao.obtener_todos(portafolio.id_portafolio)
            if not activos:
                print("No hay activos en el portafolio.")
            else:
                for activo in activos:
                    print(f"ID Activo: {activo.id_estado_portafolio}")
                    print(f"Nombre: {activo.nombre_accion}")
                    print(f"Símbolo: {activo.simbolo_accion}")
                    print(f"Cantidad: {activo.cantidad}")
                    print(f"Valor Actual: {activo.valor_actual}")
                    print("-" * 20)
        except Exception as e:
            print(f"Error al obtener los activos del portafolio: {e}")
        input("Presione Enter para continuar...")

    def _mostrar_transacciones(self):
        while True:
            self.__limpiar_consola()
            print("=== MENU DE COMPRAVENTA DE ACCIONES ===\n") 
            print("Acciones Disponibles:")
            try:
                acciones = self.accion_dao.obtener_todos()
                if not acciones:
                    print("No hay acciones disponibles.")
                else:
                    for accion in acciones:
                        cotizacion = self.cotizacion_dao.obtener_por_accion(accion.id_accion)
                        precio_compra = cotizacion.precio_compra_actual if cotizacion else "No disponible"
                        precio_venta = cotizacion.precio_venta_actual if cotizacion else "No disponible"
                        cantidad_compra = cotizacion.cantidad_compra_diaria if cotizacion else "No disponible"
                        cantidad_venta = cotizacion.cantidad_venta_diaria if cotizacion else "No disponible"
                        
                        print(f"ID: {accion.id_accion} -- Nombre: {accion.nombre_accion}, - Símbolo: {accion.simbolo_accion} - Precio Compra: {precio_compra} - Precio Venta: {precio_venta} --- Cantidad Compra: {cantidad_compra} - Cantidad Venta: {cantidad_venta}")
            except Exception as e:
                print(f"Error al obtener las acciones disponibles: {e}")

            print("\nOpciones:")
            print("1. Comprar")
            print("2. Vender")
            print("0. Salir")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self.__comprar_acciones()
            elif opcion == "2":
                self.__vender_acciones()
            elif opcion == "0":
                break
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def _ver_comisiones_broker(self):
        self.__limpiar_consola()
        print("=== COMISIONES DEL BROKER ===\n")
        print(f"La comisión actual del broker es: {self.__comision_broker}")
        input("Presione Enter para continuar...")

    def __comprar_acciones(self):
        print("=== COMPRAR ACCIONES ===\n")
        id_accion = input("Ingrese el ID de la acción a comprar: ")
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        try:
            accion = self.accion_dao.obtener_uno(id_accion)
            self.__servicio_de_compra.realizar_compra(self.__usuario_autenticado, accion, cantidad)
            print("Compra realizada con éxito.")
            self._mostrar_transacciones()
        except Exception as e:
            print(f"Error al comprar acciones: {e}")
        input("Presione Enter para continuar...")

    def __vender_acciones(self):
        print("=== VENDER ACCIONES ===\n")
        id_accion = input("Ingrese el ID de la acción a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        try:
            accion = self.accion_dao.obtener_uno(id_accion)
            self.__servicio_de_venta.realizar_venta(self.__usuario_autenticado, accion, cantidad)
            print("Venta realizada con éxito.")
            self._mostrar_transacciones()
        except Exception as e:
            print(f"Error al vender acciones: {e}")
        input("Presione Enter para continuar...")