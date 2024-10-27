from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO

class ServicioDeAutenticacion:
    def __init__(self, inversor_dao):
        self.__inversor_dao = inversor_dao

    def iniciar_sesion(self, email, contrasena):
        if not self.__inversor_dao.buscar_inversor_por_email(email):
            raise ValueError("El usuario no se encuentra registrado en la base de datos")

        inversor = self.__inversor_dao.obtener_inversor_por_email(email)

        if inversor.bloqueado:
            raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")

        if inversor.contrasena != contrasena:
            inversor.intentos_fallidos += 1
            self.__inversor_dao.actualizar(inversor, inversor.id_inversor)
            
            if inversor.intentos_fallidos >= 3:
                inversor.bloqueado = True
                self.__inversor_dao.actualizar(inversor, inversor.id_inversor)
                raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")
            else:
                raise ValueError(f"Contraseña incorrecta. Intentos restantes: {3 - inversor.intentos_fallidos}")

        inversor.intentos_fallidos = 0
        self.__inversor_dao.actualizar(inversor, inversor.id_inversor)
        
        return inversor