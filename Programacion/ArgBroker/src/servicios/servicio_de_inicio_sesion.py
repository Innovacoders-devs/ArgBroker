from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO

class ServicioDeInicioSesion:
    def __init__(self, inversorDAO):
        self.__inversor_dao = inversorDAO

    def iniciar_sesion(self, email, contrasena):
        inversor = self.__inversor_dao.obtener_por_email(email)
        
        if not inversor:
            raise ValueError("Usuario no encontrado!")
        
        if inversor.bloqueado:
            raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")
        
        if inversor.contrasena != contrasena:
            inversor.intentos_fallidos += 1
            self.__inversor_dao.actualizar(inversor, intentos_fallidos=inversor.intentos_fallidos)
            
            if inversor.intentos_fallidos >= 3:
                inversor.bloqueado = True
                self.__inversor_dao.actualizar(inversor, bloqueado=True)
                raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")
            else:
                raise ValueError(f"Contraseña incorrecta. Intentos restantes: {3 - inversor.intentos_fallidos}")
        
        inversor.intentos_fallidos = 0
        self.__inversor_dao.actualizar(inversor, intentos_fallidos=0)
        
        return inversor