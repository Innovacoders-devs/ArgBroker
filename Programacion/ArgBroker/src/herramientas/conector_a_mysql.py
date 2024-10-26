import mysql.connector
from mysql.connector import Error, IntegrityError

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
                    host=self.HOST,
                    database=self.BASE_DATOS,
                    user=self.USUARIO,
                    password=self.CONTRASENA,
                    port=self.PUERTO
                )
            except Error as e:
                raise Exception(f"Error al conectar a MySQL: {e}")

    def desconectar_de_base_datos(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            self.conexion = None

    def ejecutar_consulta(self, consulta, parametros=None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            self.conexion.commit()
            cursor.close()
            return cursor
        except IntegrityError as e:
            raise Exception(f"Error al ejecutar la consulta: {e}")
        except Error as e:
            raise Exception(f"Error al ejecutar la consulta: {e}")
        return None

    def traer_todos(self, consulta, parametros=None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            raise Exception(f"Error al obtener los resultados: {e}")
            return []

    def traer_solo_uno(self, consulta, parametros=None):
        try:
            cursor = self.conexion.cursor()
            if parametros:
                cursor.execute(consulta, parametros)
            else:
                cursor.execute(consulta)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            raise Exception(f"Error al obtener el resultado: {e}")
            return None