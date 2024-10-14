import re  # que es esto?

class Inversor:
    def __init__(self, nombre, apellido, cuil, email, contrasena, portafolio, saldo_cuenta, intentos_fallidos=0):
            self._nombre = nombre
            self._apellido = apellido
            self._cuil = cuil
            self._email = email
            self.__contrasena = contrasena
            self._portafolio = []
            self._id_inversor = None
            self._saldo_cuenta = saldo_cuenta
            self._intentos_fallidos = intentos_fallidos


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
    def cuil(self, cuil):  # hay que manejar los errores uniformemente es decir todos con raise Error, aqui no cambia el cuil el setter(si todo esta bien self.cuil == cuil)
        if len(cuil) < 11:
            raise ValueError('El CUIL debe contener 11 caracteres')
        else:
            if not isinstance(cuil, int):
                raise ValueError('El CUIL está conformado por números')
        self._cuil = cuil


    @property
    def email(self):
        return self._email
    """
   @email.setter
    def email(self, email): 
        if not self.validar_correo(email):  se puede negar la condicion para que quede mas elegante ademas en lugar de validar directamente desde el setter podes llamar a tu funcion validadora de email
            raise ValueError('El correo electrónico es inválido')
        self._email = email

    @staticmethod
    def validar_correo(email):
        patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron_email, email) is not None  
        # de esta forma retornaria directamente True si esta bien el correo o False si no es correcto
    """
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
    #A diferencia de lo que ocurrio con el email aqui lo tenes perfectamente implementado, el evaluador retorna False
    # y en la password negas la condicion luego pasando a la asignacion del valor, Muy bien!!


    @property
    def id_inversor(self):
        return self._id_inversor


    @id_inversor.setter
    def id_inversor(self):
        if not isinstance (self,  str):
            raise ValueError ('El id_inversor no puede estar vacío')


    def autenticar (id_inversor, inversorDAO, contrasena):
        try:
            id_inversor = inversorDAO.obtener_usuario_por_nombre(inversorDAO)
            if id_inversor and id_inversor.contrasena == contrasena:
                return True
            return False
        except BaseDatosError as e:
            raise AutenticacionError(f"Error al autenticar el inversor: {str(e)}")


    def bloquear(self):
        if intentos_fallidos =3:
            return True

    def desbloquear(self):
        pass