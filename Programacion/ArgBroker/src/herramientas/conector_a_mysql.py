import mysql.connector
from mysql.connector import Error
 
# para usar el conector primero se debe descomprimir el requirements.txt:
# python -m venv venv (para crear una carpeta venv con el entorno adentro tiene que tener 2 veces venv)
# venv\ Scripts\ activate (se debe navegar hasta dentro del entorno y activarlo)
# pip install -r requirements.txt (luego se ejecuta el siguiente comando y se instala el conector de mysql)


class MySQLConnector:
    def __init__(self, HOST, BASE_DATOS, USUARIO, CONTRASENA, PUERTO=3306):
        self.HOST = HOST
        self.BASE_DATOS = BASE_DATOS
        self.USUARIO = USUARIO
        self.CONTRASENA = CONTRASENA
        self.PUERTO = PUERTO
        self.conexion = None

    def conectar_a_base_datos(self):
        if self.conexion is None or not self.conexion.is_connected():
            try:
                self.conexion = mysql.connector.connect(
                    host = self.HOST,
                    database = self.BASE_DATOS,  
                    user = self.USUARIO,        
                    password = self.CONTRASENA,  
                    port = self.PUERTO          
                )

            except mysql.connector.Error as error:  
                raise Exception(f"Error al conectar a MySQL: {error}")

    def desconectar_de_base_datos(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            self.conexion = None


    def ejecutar_consulta(self, consulta, parametros = None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            self.conexion.commit()
            cursor.close()
            return cursor
        except Error as e:
            raise Exception(f"Error al ejecutar la consulta: {error}")
            return None

    def traer_todos(self, consulta, parametros = None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as error:
            raise Exception(f"Error al obtener los resultados: {error}")
            return []

    def traer_solo_uno(self, consulta, parametros = None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as error:
            raise Exception(f"Error al obtener el resultado: {error}")
            return None