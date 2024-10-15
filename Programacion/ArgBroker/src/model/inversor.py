import re  # que es esto?

class Inversor:
    def __init__(self, nombre, apellido, cuil, email, contrasena, portafolio, saldo_cuenta, intentos_fallidos=0, bloqueado):
            self._nombre = nombre
            self._apellido = apellido
            self._cuil = cuil
            self._email = email
            self.__contrasena = contrasena
            self._portafolio = []
            self._id_inversor = None
            self._saldo_cuenta = saldo_cuenta
            self._intentos_fallidos = intentos_fallidos
            self._bloqueado = False


    def __str__(self):
        return f'Inversor: {self._apellido}, {self._nombre} en portafolio {self._portafolio} .'


    @property
    def nombre(self):
        return self._nombre


    @nombre.setter
    def nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError('El nombre debe ser una cadena de texto.')
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido


    @apellido.setter
    def apellido(self, apellido):
        if not isinstance(apellido, str):
            raise ValueError('El apellido debe ser una cadena de texto.')
        self._apellido = apellido


    @property
    def cuil(self):
        return self._cuil


    @cuil.setter
    def cuil(self, cuil):
        if len(cuil) < 11:
            raise ValueError('El CUIL debe contener 11 caracteres')
        else:
            if not isinstance(cuil, int):
                raise ValueError('El CUIL está conformado por números')
        self._cuil = cuil


    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, email): 
        if '@' not in email:
            raise ValueError('El correo electrónico debe tener un @')
        else:
            if not self.validar_correo (email):
                raise ValueError ('El correo electrónico es inválido')
        self._email = email


    @staticmethod
    def validar_correo (email):
        patron_email = r'[a-zA-ZO-9._%+-]+@[a-zA-ZO-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron_email, email) is not None


    @property
    def contrasena(self):
        return self.__contrasena


    @contrasena.setter
    def contrasena(self, contrasena):
        if not self.es_contrasenia_valida(contrasena):
            raise ValueError('Está contraseña no cumple con los requisitos de seguridad.')
        self.__contrasena = contrasena


    @staticmethod
    def es_contrasenia_valida(contrasena):
        if len(contrasena) < 8:
            return False


    @property
    def id_inversor(self):
        return self._id_inversor


    @id_inversor.setter
    def id_inversor(self, str):
        if not isinstance (self,  str):
            raise ValueError ('El id_inversor no puede estar vacío')


    def autenticar (self, id_inversor, inversorDAO, contrasena):
        try:
            self.id_inversor = inversorDAO.obtener_usuario_por_nombre(inversorDAO)
            if id_inversor and id_inversor.contrasena == contrasena:
                return True
            return False
        except BaseDatosError as e:
            raise AutenticacionError(f"Error al autenticar el inversor: {str(e)}")


    @property
    def bloqueado(self):
        if contrasena == self.__contrasena:
            self._intentos_fallidos = 0
            return True
        else:
            self._intentos_fallidos += 1
            if self._intentos_fallidos >= 3:
                self.bloquear()
            return False


    def bloquear(self):
        if self._bloqueado = True
        raise ValueError('El inversor está bloqueado')


    def desbloquear(self):
        pass