from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO
class ServicioDeRegistro:
    def __init__(self, inversorDAO):
        self.__inversor_dao = inversorDAO

    def registrar_usuario(self, nombre, apellido, cuil, email, contrasena):
        if self.__inversor_dao.obtener_por_email(email):
            raise ValueError("El email ya está registrado")
        
        nuevo_inversor = Inversor(nombre=nombre, apellido=apellido, cuil=cuil, email=email, contrasena=contrasena)
        
        self.__inversor_dao.crear(nuevo_inversor)
        return nuevo_inversor