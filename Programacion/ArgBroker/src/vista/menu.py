import os
import time
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

from rich.console import Console
from rich.panel import Panel

class Menu:
    def __init__ (self, base_de_datos, COMISION_BROKER):
        self.__base_de_datos = base_de_datos
        self.__comision_broker = COMISION_BROKER
        self.__nuevo_inversor = None
        self.__usuario_autenticado = None
        self.__console = Console()
       

        self.inversor_dao = InversorDAO(self.__base_de_datos)
        self.accion_dao = AccionDAO(self.__base_de_datos)
        self.portafolio_dao = PortafolioDAO(self.__base_de_datos)
        self.transaccion_dao = TransaccionDAO(self.__base_de_datos)
        self.estado_portafolio_dao = EstadoPortafolioDAO(self.__base_de_datos)
        self.historial_saldo_dao = HistorialSaldoDAO(self.__base_de_datos)
        self.cotizacion_dao = CotizacionDAO(self.__base_de_datos)

        self.__servicio_de_registro = ServicioDeRegistro(self.inversor_dao, self.portafolio_dao)
        self.__servicio_de_autenticacion = ServicioDeAutenticacion(self.inversor_dao)
        self.__servicio_de_calculo_de_rendimientos = ServiciodeCalculodeRendimientos(self.transaccion_dao, self.cotizacion_dao)
        self.__servicio_de_compra = ServiciodeCompra(self.historial_saldo_dao, self.cotizacion_dao, self.estado_portafolio_dao,self.transaccion_dao, self.portafolio_dao, self.__comision_broker)
        self.__servicio_de_venta = ServiciodeVenta(self.historial_saldo_dao, self.cotizacion_dao, self.estado_portafolio_dao, self.transaccion_dao, self.portafolio_dao, self.__comision_broker)

        self.__ejecutando = True
    

    def __limpiar_consola(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def mostrar_menu_principal(self): 
        while self.__ejecutando: 
            self.__limpiar_consola()
            self.__console.print(Panel.fit(" Bienvenido a ARGBroker", title="Menú Principal", style="magenta"))
            print("\n1. Iniciar Sesion") 
            print("2. Registrarse") 
            print("0. Terminar el programa\n")
            
            opcion = input("Seleccione una opción: \n")
                
            if opcion == "1":
                self.__mostrar_panel_iniciar_sesion() 
            elif opcion == "2":
                self.__mostrar_panel_de_registro()
            elif opcion == "0":
                self.__ejecutando = False
                break
            else:
                input("Opción inválida. Seleccione una opción para continuar...")

    def __mostrar_panel_de_registro(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== PANEL DE REGISTRO ===\n", title = "ARGBroker", style="red"))
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
                self.__console.print(f'Se registro el usuario exitosamente',style="bold green")
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
                        self.__console.print("Opcion no valida, por favor ingrese una de las opciones ofrecidas",style="red")


        except Exception as e:
            print(f"Error al registrarse: {e}")
            while True:
                eleccion = input("Ingrese 1 para intentar nuevamente, 2 para Salir: ")
                if eleccion.isdigit() and int(eleccion) in [1, 2]:
                    eleccion = int(eleccion)
                    if eleccion == 1:
                        self.__mostrar_panel_de_registro()
                    elif eleccion == '2':
                        self.__ejecutando = False
                    break
                else:
                   self.__console.print("Ingrese una opción válida.",style="red")
            


    def __mostrar_panel_iniciar_sesion(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== PANEL DE INICIO DE SESION ===", title = "ARGBroker", style="blue"))
        try:
            email = input("Ingrese email del inversor: ")
            contrasena = input("Ingrese su contraseña: ")

            self.__console.print("Verificando credenciales...", style="yellow")
            time.sleep(1)  

            self.__usuario_autenticado = self.__servicio_de_autenticacion.iniciar_sesion(email, contrasena)
            if self.__usuario_autenticado:
                self.__console.print("Credenciales correctas, iniciando sesión...", style="bold green")
                time.sleep(1)  
                self._mostrar_panel_de_inversor()
            else:
                self.__console.print("Credenciales incorrectas. Intente nuevamente.", style="bold red")
        except Exception as e:
            self.__console.print(f'Ocurrió un error: {e}', style="bold red")
            opcion_del_submenu = True
            while opcion_del_submenu:
                eleccion = input("Ingrese 1 para intentar nuevamente, 2 para Salir: ")
                if eleccion == '1':
                    self.__mostrar_panel_iniciar_sesion()
                    opcion_del_submenu = False
                elif eleccion == '2':
                    self.mostrar_menu_principal()
                else:
                    self.__console.print("Ingrese una opción válida", style="red")


    def _mostrar_panel_de_inversor(self): 
        while True:
            self.__limpiar_consola()
            nombre_completo = f"{self.__usuario_autenticado.nombre} {self.__usuario_autenticado.apellido}"
            self.__console.print(Panel.fit(f"Bienvenido {nombre_completo} 😊", title="ARGBroker", style="yellow"))
            print("1. Datos Personales")
            print("2. Mi Portafolio")
            print("3. Transacciones")
            print("0. Cerrar sesión")
            
            opcion = input("Seleccione una opción: \n")
            
            if opcion == "1":
                self.__mostrar_panel_mis_datos()
            elif opcion == "2":
                self._mostrar_portafolio()
            elif opcion == "3":
                self._mostrar_transacciones()
            elif opcion == "0":
                confirmacion = input("¿Está seguro que desea cerrar sesión? (s/n): \n")
                if confirmacion.lower() == 's':
                    self.__usuario_autenticado = None
                    self.__console.print("Sesión cerrada. Presione Enter para continuar...",style="red")
                    input()
                    self.mostrar_menu_principal()
                    break
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def __mostrar_panel_mis_datos(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== MIS DATOS === \n", title = "ARGBroker", style="green"))
        try:
            ultimo_saldo = self.historial_saldo_dao.buscar_ultimo_saldo(self.__usuario_autenticado.id_inversor)
            saldo_actual = ultimo_saldo.saldo_nuevo
        except Exception as e:
            saldo_actual = "No disponible"
            print(f'Aun no hay transacciones su saldo es {self.__usuario_autenticado.saldo_cuenta}')

        print(f'id del inversor: {self.__usuario_autenticado.id_inversor}')
        print(f'Nombre: {self.__usuario_autenticado.apellido}, {self.__usuario_autenticado.nombre}')
        print(f'Email: {self.__usuario_autenticado.email}')
        print(f'Saldo actual: {saldo_actual}')
        input("Presione Enter para continuar...")

       
    def _actualizar_datos(self):
       self.__limpiar_consola()
       self.__console.print(Panel.fit("=== ACTUALIZAR DATOS DE INVERSOR === \n", title = "ARGBroker", style="green"))
       nuevo_correo_elecrtonico = input("Ingrese nuevo email: ")
       self.InversorDAO.email = nuevo_correo_elecrtonico
       
    def _mostrar_portafolio(self): 
        while True:
            self.__limpiar_consola()
            self.__console.print(Panel.fit("=== PORTAFOLIO ===\n", title="ARGBroker", style="magenta"))
            self.__mostrar_estadisticas_portafolio()
            print("1. Mis acciones")
            print("2. Historial")
            print("3. Listar Activos")
            print("0. Volver")

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

    def __mostrar_estadisticas_portafolio(self):
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            total_invertido, rendimiento_total, tiene_inversiones = self.__servicio_de_calculo_de_rendimientos.calcular_rendimiento_total(portafolio.id_portafolio)
            
            if not tiene_inversiones:
                self.__console.print("Actualmente el usuario no tiene inversiones, realiza compras o ventas y se mostrarán aquí los rendimientos.", style="bold yellow")
            else:
                self.__console.print(f"Total invertido: {total_invertido}", style="bold")
                if total_invertido > 0 and rendimiento_total == 0:
                    self.__console.print("Aún no hay cotizaciones nuevas para las acciones, por lo tanto, el rendimiento es 0.", style="bold yellow")
                else:
                    color = "green" if rendimiento_total >= 0 else "red"
                    self.__console.print(f"Rendimiento total: {rendimiento_total}", style=f"bold {color}")
        except Exception as e:
            self.__console.print(f"Error al obtener las estadísticas del portafolio: {e}", style="red")

    def acciones_en_el_portfolio(self):
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            acciones_en_haber_del_inversor = self.estado_portafolio_dao.obtener_todos(portafolio.id_portafolio)
            if not acciones_en_haber_del_inversor:
                self.__console.print("No se encontraron acciones en el portafolio.",sytle="blue")
            else:
                for accion in acciones_en_haber_del_inversor:
                    if accion.cantidad > 0: 
                        print(f"id: {accion.id_accion} Nombre: {accion.nombre_accion}, Símbolo: {accion.simbolo_accion}, Cantidad: {accion.cantidad}, Valor Actual: {accion.valor_actual}")
        except Exception as e:
            self.__console.print(f"Error al obtener las acciones: {e}",style="red")

    def _mostrar_acciones(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== MIS ACCIONES === \n", title = "ARGBroker", style="cyan"))
        self. acciones_en_el_portfolio()
        input("Presione Enter para continuar...")

    def _mostrar_historial(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== HISTORIAL DE TRANSACCIONES === \n", title = "ARGBroker", style="cyan"))
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            transacciones = self.transaccion_dao.obtener_por_portafolio(portafolio.id_portafolio)
            if not transacciones:
                self.__console.print("No hay transacciones disponibles.",style="blue")
            else:
                for transaccion in transacciones:
                    print(f"ID Transacción: {transaccion.id_transaccion} Tipo: {transaccion.tipo}")
                    print(f"Fecha: {transaccion.fecha} Precio: {transaccion.precio} Cantidad: {transaccion.cantidad}")
                    print(f"Comisión: {transaccion.comision} ID Portafolio: {transaccion.id_portafolio}")
                    print("------------------" )
        except Exception as e:
           self.__console.print(f"Error al obtener el historial de transacciones: {e}",style="red")
        input("Presione Enter para continuar...")
        
    def __listar_activos_portafolio(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("=== LISTA DE ACTIVOS DEL PORTAFOLIO === \n", title = "ARGBroker", style="magenta"))
        try:
            portafolio = self.portafolio_dao.obtener_uno(self.__usuario_autenticado.id_inversor)
            activos = self.estado_portafolio_dao.obtener_todos(portafolio.id_portafolio)
            if not activos:
                print("No hay activos en el portafolio.")
            else:
                for activo in activos:
                    rendimiento, hay_cotizaciones_posteriores = self.__servicio_de_calculo_de_rendimientos.calcular_rendimiento_por_accion(portafolio.id_portafolio, activo.id_accion)
                    print(f"ID Activo: {activo.id_estado_portafolio}")
                    print(f"Nombre: {activo.nombre_accion} Simbolo: {activo.simbolo_accion}")
                    print(f"Cantidad: {activo.cantidad} Valor Actual: {activo.valor_actual}")
                    if not hay_cotizaciones_posteriores:
                        print("Aún no hay rendimientos para este activo porque no hay nuevas cotizaciones desde la compra.")
                    else:
                        print("Estado:")
                        print(f"  - Rendimiento Simple Diario: {rendimiento['rendimiento_simple_diario']:.2f}%")
                        print(f"  - Rendimiento Acumulado: {rendimiento['rendimiento_acumulado']:.2f}%")
                    print("------------------")
        except Exception as e:
            print(f"Error al obtener los activos del portafolio: {e}")
        input("Presione Enter para continuar...")

    def _mostrar_transacciones(self):
        while True:
            self.__limpiar_consola()
            self.__console.print(Panel.fit("=== MENU DE COMPRAVENTA DE ACCIONES ===\n", title = "ARGBroker", style="bold red")) 
            print("Acciones Disponibles para comprar:")
            try:
                acciones = self.accion_dao.obtener_todos()
                if not acciones:
                    self.__console.print("No hay acciones disponibles.",style="blue")
                else:
                    for accion in acciones:
                        cotizacion = self.cotizacion_dao.obtener_por_accion(accion.id_accion)
                        precio_compra = cotizacion.precio_compra_actual if cotizacion else "No disponible"
                        precio_venta = cotizacion.precio_venta_actual if cotizacion else "No disponible"
                        cantidad_compra = cotizacion.cantidad_compra_diaria if cotizacion else "No disponible"
                        cantidad_venta = cotizacion.cantidad_venta_diaria if cotizacion else "No disponible"
                        
                        if cantidad_compra != "No disponible" and cantidad_compra > 0:
                            print(f"ID: {accion.id_accion} -- Nombre: {accion.nombre_accion}- $$ Compra: {precio_compra} - $$ Venta: {precio_venta} - Cantidad Compra: {cantidad_compra} - Cantidad Venta: {cantidad_venta}")
            except Exception as e:
                self.__console.print(f"Error al obtener las acciones disponibles: {e}",style="red")

            print("\nOpciones:")
            print("1. Comprar")
            print("2. Vender")
            print("3. Ver comision del Broker")
            print("4. Volver al panel principal")

            opcion = input("Seleccione una opción: \n ")

            if opcion == "1":
                self.__comprar_acciones()
            elif opcion == "2":
                self.__vender_acciones()
            elif opcion == "3":
                self._ver_comisiones_broker()
            elif opcion == "4":
                self._mostrar_panel_de_inversor()
            else:
                input("Opción inválida. Presione Enter para continuar...")

    def _ver_comisiones_broker(self):
        self.__console.print("=== COMISION DEL BROKER POR PERMITIR OPERAR===\n", title = "ARGBroker", style="yellow")

        print(f"La comisión actual del broker es: {self.__comision_broker} % por transaccion")
        input("Presione Enter para continuar...")


    def __comprar_acciones(self):
        self.__console.print(Panel.fit("COMPRAR ACCIONES\n", style="magenta"))
        acciones_disponibles = self.accion_dao.obtener_todos()
        id_acciones = tuple(accion.id_accion for accion in acciones_disponibles)
    
    # Solicitar ID de la acción
        try:
            id_accion = int(input("Ingrese el ID de la acción a comprar: "))
        except ValueError:
            self.__console.print("El ID ingresado no es válido. Ingrese un número.", style="red")
            input("Presione Enter para continuar...")
            return
    
    # Verificar si el ID está en la lista de IDs disponibles
        if id_accion not in id_acciones:
            self.__console.print("El ID ingresado no es válido. Seleccione una de las acciones que están en pantalla.", style="red")
            input("Presione Enter para continuar...")
            return
    
    # Solicitar cantidad a comprar
        try:
            cantidad = int(input("Ingrese la cantidad a comprar: "))
        except ValueError:
            self.__console.print("La cantidad ingresada no es válida. Ingrese un número.", style="red")
            input("Presione Enter para continuar...")
            return

        try:
            accion = self.accion_dao.obtener_uno(id_accion)
            self.__servicio_de_compra.realizar_compra(self.__usuario_autenticado, accion, cantidad)
            self.__console.print("Compra realizada con éxito.",style="bold green")
        except Exception as e:
            self.__console.print(f"Error al comprar acciones: {e}",style="red")
        input("Presione Enter para continuar...")

    def __vender_acciones(self):
        self.__limpiar_consola()
        self.__console.print(Panel.fit("VENDER ACCIONES\n", style="blue"))
        self. acciones_en_el_portfolio()
        id_accion = input("\nIngrese el ID de la acción a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        try:
            accion = self.accion_dao.obtener_uno(id_accion)
            self.__servicio_de_venta.realizar_venta(self.__usuario_autenticado, accion, cantidad)
            self.__console.print("Venta realizada con éxito.",style="bold green")
        except Exception as e:
            self.__console.print(f"Error al vender acciones: {e}",style="red")
        input("Presione Enter para continuar...")