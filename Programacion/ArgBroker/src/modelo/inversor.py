class Inversor:
    def __init__(self, id_inversor= None, nombre= None, apellido= None, cuil= None, email= None, contrasena= None, saldo_cuenta= 1000000.0, intentos_fallidos= 0):
        self._nombre = nombre
        self._apellido = apellido
        self._cuil = cuil
        self._email = email
        self.__contrasena = contrasena
        self._id_inversor = id_inversor
        self._saldo_cuenta = saldo_cuenta
        self._intentos_fallidos = intentos_fallidos
        self._bloqueado = False

    def __str__(self):
        return f'''Inversor:{self._id_inversor} {self._apellido}, {self._nombre}; Cuil: {self._cuil},Email: {self._email}, El saldo en cuenta es: {self._saldo_cuenta}, contrasena: {self.__contrasena}, intentos fallidos de ingreso: {self._intentos_fallidos}'''

    @property
    def id_inversor(self):
        return self._id_inversor

    @id_inversor.setter
    def id_inversor(self, id_inversor):
        if not isinstance(id_inversor, int):
            raise ValueError('El ID del inversor debe ser un número entero.')
        self._id_inversor = id_inversor

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
        if not isinstance(cuil, int):
            raise ValueError('El CUIL está conformado por números')
        if len(str(cuil)) < 11:
            raise ValueError('El CUIL debe contener 11 caracteres')
        self._cuil = cuil

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email): 
        if '@' not in email:
            raise ValueError('El correo electrónico debe tener un @')
        else:
            if not self.validar_correo(email):
                raise ValueError('El correo electrónico es inválido')
        self._email = email

    def validar_correo(self, email):
        # Simple validation: check if there's a domain part after '@'
        if '.' not in email.split('@')[-1]:
            return False
        return True

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self.__contrasena = contrasena

    @property
    def saldo_cuenta(self):
        return self._saldo_cuenta

    @saldo_cuenta.setter
    def saldo_cuenta(self, saldo_cuenta):
        self._saldo_cuenta = saldo_cuenta

    @property
    def intentos_fallidos(self):
        return self._intentos_fallidos

    @intentos_fallidos.setter
    def intentos_fallidos(self, intentos_fallidos):
        self._intentos_fallidos = intentos_fallidos
    
    @property
    def bloqueado(self):
        return self._bloqueado

    @bloqueado.setter
    def bloqueado(self, bloqueado):
        self._bloqueado = bloqueado