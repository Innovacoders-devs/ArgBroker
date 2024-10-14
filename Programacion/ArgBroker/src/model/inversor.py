import re

class Inversor:
    def __init__(self, nombre, apellido, cuil, email, password, portafolio):
            self._nombre = nombre
            self._apellido = apellido
            self._cuil = cuil
            self._email = email
            self.__password = password
            self._portafolio = portafolio


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
        if len(cuil)<11:
            return f'El cuil ingresado no es válido'
        else:
            if not isinstance (cuil, int):
                return f'El CUIL está conformado por 11 números'


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' not in email:
            raise ValueError('El correo electrónico debe tener un @')
        self._email = email

    @staticmethod
    def validar_correo (email):
        patron_email = r'[a-zA-ZO-9._%+-]+@[a-zA-ZO-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(patron_email, email):
            return "Correo Válido"
        else:
            return "Correo no válido - Debe ser: ejemplo@email.com"


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not self.es_contrasenia_valida(password):
            raise ValueError('Está contraseña no cumple con los requisitos de seguridad.')
        self.__password = password

    @staticmethod
    def es_contrasenia_valida(password):
        if len(password) < 8:
            return False

    @property
    def portafolio(self):
        return self._portafolio

    @portafolio.setter
    def portafolio(self, portafolio):
        if not isinstance(transaccion, portafolio):
           self.portafolio.append(transaccion)
        else:
            raise ValueError('Esta transacción no corresponde en este portafolio. ')


    def autenticar_inversor (self):



    def bloquear(self):



    def desbloquear(self):