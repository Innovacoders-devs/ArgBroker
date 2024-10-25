import uuid
from ..modelo.inversor import Inversor
from ..acceso_a_datos.inversor_dao import InversorDAO

class InversorServicio:
    def __init__(self, inversorDAO):
        self.__inversor_dao = inversorDAO

    def registrar_usuario(self, inversor):
        self.__inversor_dao.crear(self, nombre, apellido, cuil, email, contrasena):
        if self.inversorDAO.obtener_por_email(email):
            raise ValueError("El email ya está registrado")
        
        nuevo_inversor = Inversor(nombre=nombre, apellido=apellido, cuil=cuil, email=email, contrasena=contrasena)

        self.__inversor_dao.crear(nuevo_inversor)
        return nuevo_inversor
    
    def iniciar_sesion(self, email, contrasena):
        inversor = self.__inversor_dao.obtener_por_email(email)
        if not inversor:
            raise ValueError("Usuario no encontrado!")
        
        if inversor.bloqueado:
            raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")
        
        if inversor.contrasena != contrasena:
            inversor.intentos_fallidos += 1
            self.__inversor_dao.actualizar(inversor, intentos_fallidos=inversor.intentos_fallidos)
            if inversor.intentos_fallidos == 3:
                inversor.bloqueado = True
                self.__inversorDAO.actualizar(inversor, bloqueado=True)
                raise ValueError("Cuenta bloqueada. Por favor contacte al administrador")
            else:
                raise ValueError(f"Contraseña incorrecta. Intentos restantes: {3 - inversor.intentos_fallidos}")
        else:
            inversor.intentos_fallidos = 0
            self.__inversorDAO.actualizar(inversor, intentos_fallidos=0)
            return True
        
    def autentificar_usuario(self, email, contrasena):
        inversor = self.iniciar_sesion(email, contrasena)
        if inversor:
            token = str(uuid.uuid4())
            return token

            