import re  

class Inversor:
    def __init__(self, nombre, apellido, cuil, email, contrasena, portafolio, saldo_cuenta, intentos_fallidos=0): #el atributo bloqueado no deberia recibirse como parametro porque no mapea con la base de datos, el error que marca es porque los parametros con valor predeterminado deberian ir al final de la lista de atributos(que de todas formas no es necesario inicializar en cero porque de la base de datos ya viene con ese valor por defecto)
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

#el metodo str debe dar cuenta de todos los atributos del objeto en este caso porque es una clase de dominio
    def __str__(self):
        return f'Inversor: {self._apellido}, {self._nombre}; Cuil: {self._cuil},Email: {self._email} en portafolio {self._portafolio}. El saldo en cuenta es: {self._saldo_cuenta}'


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

#el codigo repite procedimientos al evaluar nuevamente cuestiones del email cuando ya tenes una funcion que valida el correo "validar correo"
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

    def autenticar(self, inversorDAO, email, contrasena):
        try:
            if email == inversorDAO.email:
                if inversorDAO.intentos_fallidos >= 3:
                    inversorDAO.bloqueado = True
                    raise AutenticacionError ("La cuenta ha sido bloqueada debido a múltiples intentos fallidos.")
                elif inversorDAO.contrasena == contrasena:
                    inversorDAO.intentos_fallidos = 0
                    return inversorDAO
                else:
                    inversorDAO.intentos_fallidos += 1
                    raise AutenticacionError("Contraseña incorrecta.")
            else:
                raise AutenticacionError("Email no encontrado.")
            


    def bloquear(self):
        if self._bloqueado == True: #faltaba un doble == para evaluar la xpresion
            raise ValueError('El inversor está bloqueado') #Mepa que en tu version de autenticar, ya agregaste el bloqueo


    def desbloquear_cuenta(self, inversorDAO, email, codigo_desbloqueo):
        if email == inversorDAO.email and inversorDAO.bloqueado:
           if codigo_desbloqueo == inversorDAO.codigo_desbloqueo:
                inversorDAO.bloqueado = False
                inversorDAO.intentos_fallidos = 0
                    return "Cuenta desbloqueada exitosamente."
            else:
              raise DesbloqueoError("Código de desbloqueo incorrecto.")
