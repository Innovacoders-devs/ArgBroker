class ServicioDeRegistro:
    def __init__(self, inversor_dao):
        self.__inversor_dao = inversor_dao

    def registrar_usuario(self, inversor):
        if self.__inversor_dao.buscar_inversor_por_email(inversor.email):
            raise ValueError("El email ya está registrado en la base de datos")
        try:
            self.__inversor_dao.crear(inversor)
            return True
        except Exception as e:
            raise Exception(f'Ocurrio un error al registrar el usuario: {e}')