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
        return f'''Inversor:{self._id_inversor} {self._apellido}, {self._nombre}; Cuil: {self._cuil},Email: {self._email} en portafolio {self._portafolio}. 
        El saldo en cuenta es: {self._saldo_cuenta}, contrasena: {self.__contrasena}, intentos fallidos de ingreso: {self._intentos_fallidos}'''


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

    def autenticar(self, email_que_ingreso, contrasena_que_ingreso, conector):
        inversor_en_bdd = inversorDAO(conector)
        try:
            inversor=inversor_en_bdd.obtener_inversor_por_email(email_que_ingreso)
            if not inversor:
                raise Exception ('El usuario no existe en la base de datos')
            if inversor.contrasena !=  contrasena_que_ingreso:
                inversor.intentos_fallidos +=1
                inversor_en_bdd.actualizar_intentos_fallidos(inversor)

                if inversor.intentos_fallidos >3:
                    inversor.bloqueado = True
                    inversor_en_bdd.bloquear_cuenta(inversor)
                    raise Exception ('La cuenta ha sido bloqueada debido a múltiples intentos fallidos')


            inversor.intentos_fallidos=0
            inversor_en_bdd.resetar_intentos_fallidos(inversor)
            return inversor

        except Exception as error: #agregue este bloque para que pueda correr una prueba
            pass
#vamos a cambiar unas cosillas para que sea mas simple desde el punto de vista de la logica:
#primero lo que va a recibir la funcion es por un lado el usuario a autenticar, por otro los valores de los imputs
#quisiera que le cambiemos los nombres a las variables para que sea aun mas simple de leer a primera vista ej 
# def autenticar(self, email_que_ingreso, contrasena_que_ingreso):

# lo segundo que vamos a hacer es negar todas las condiciones por las cuales el usuario no seria correctamente autenticado 
    """
def autenticar(self, email_que_ingreso, contrasena_que_ingreso, connector):

    inversor_de_bdd = InversorDAO(connector) #hay que pasar por parametro el conector
    inversor_de_bdd.obtener_inversor_por_email(email_que_ingreso) #hay que importar al inversor dao 

    esto viola varios principios de la programacion porque esta clase no deberia tener logica de conexion a la bdd
    pero de otra forma no seria posible evaluar si el usuario existe en la bdd en la misma funcion
    o habria que evaluar solo si la contraseña encontrada coincide y luego continuar contando intentos sino, el usuario se evaluaria por fuera en el bucle principal del programa, te dejo esta decision a vos

    if not inversor_de_bdd:
        raise Exception("el usuario no existe en la base de datos")

    if inversor_de_bdd.contrasena != contrasena_que_ingreso:
        raise Exception("credenciales incorrectas")

    voy a dejaro aqui porque esto es solo una pista, a ver si lo podes terminar bb yo se que podes!
    cuando termines de evaluar todo lo que no tiene que pasar para que el usuario inicie sesion vamos a cambiar 
    el tipo de retorno, en lugar de un usuario vamos a entregar un True (lo que debe significar que lo que le mandamos si se pudo autenticar)
  
"""

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
