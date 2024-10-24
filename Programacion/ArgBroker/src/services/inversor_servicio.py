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