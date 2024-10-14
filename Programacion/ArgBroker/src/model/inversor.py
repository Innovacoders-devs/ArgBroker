import re


class Inversor:
    def __init__(self):
        def __init__(self, nombre, apellido, email, password, portafolio):
            self._nombre = nombre
            self._apellido = apellido
            self._email = email
            self.__password = password
            self._portafolio = portafolio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nom):
        if not isinstance(nom, str):
            raise ValueError('El nombre debe ser una cadena de texto.')
        self._nombre = nom

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apell):
        if not isinstance(apell, str):
            raise ValueError('El apellido debe ser una cadena de texto.')
        self._apellido = apell

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, mail):
        if '@' not in mail:
            raise ValueError('El correo electrónico debe tener un @')
        self._email = mail

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passw):
        if not self.es_contrasenia_valida(passw):
            raise ValueError('Está contraseña no cumple con los requisitos de seguridad.')
        self.__password = passw

    @property
    def portafolio(self):
        return self._portafolio

    @portafolio.setter
    def portafolio(self, portfolio):
        if not isinstance(transaccion, portfolio):
           self.portafolio.append(transaccion)
        else:
            raise ValueError('Esta transacción no corresponde en este portafolio. ')





