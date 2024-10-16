import mysql.connector
from mysql.connector import Error

class MySQLConnector:
    def __init__(self, host, base_datos, usuario, contrasena, puerto=3306):
        self.host = host
        self.base_datos = base_datos
        self.usuario = usuario
        self.contrasena = contrasena
        self.puerto = puerto
        self.connection = None

    def conectar_a_base_datos(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.base_datos,  
                user=self.usuario,        
                password=self.contrasena,  
                port=self.puerto          
            )
            if self.connection.is_connected():
                print("Conectado a la base de datos de Arg-Broker")
        except mysql.connector.Error as e:  # Asegúrate de importar mysql.connector.Error
            print(f"Error al conectar a MySQL: {e}")

    def desconectar_de_base_datos(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexion a MySQL cerrada")

    def ejecutar_consulta(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            return cursor
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def traer_todos(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Error al obtener todos los resultados: {e}")
            return []

    def traer_solo_uno(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            print(f"Error al obtener un resultado: {e}")
            return None