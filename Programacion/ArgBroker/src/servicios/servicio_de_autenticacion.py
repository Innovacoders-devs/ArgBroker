import uuid
from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO

class ServicioDeAutenticacion:
    def autentificar_usuario(self, email, contrasena, servicio_de_inicio_sesion):
        inversor = servicio_de_inicio_sesion.iniciar_sesion(email, contrasena)
        
        if inversor:
            token = str(uuid.uuid4())
            return token