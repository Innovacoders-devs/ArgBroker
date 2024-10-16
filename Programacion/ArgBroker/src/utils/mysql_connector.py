import mysql.connector
from mysql.connector import Error
"""
para usar el conector primero se debe descomprimir el requirements.txt:
python -m venv venv (para crear una carpeta venv con el entorno adentro tiene que tener 2 veces venv)
venv\Scripts\ activate(se debe navegar hasta dentro del entorno y activarlo)
pip install -r requirements.txt (luego se ejecuta el siguiente comando y se instala el conector de mysql)

los metodos del conector son:

conectar_a_base_datos()  --para conectar a la base de datos

desconectar_de_base_datos()  --para desconectar (se debe hacer siempre que se termine de ejecutar una consulta)

ejecutar_consulta(self, query, params=None) --para ejecutar consultas sobre la base de datos
ej:
    consulta_para_crear_inversor = "INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta, intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    usuario_nuevo = ("Juan","Perez","20-12345678-9","juan.perez@example.com","12345",10000, 0)
    connector.ejecutar_consulta(consulta_para_crear_inversor, usuario_nuevo)

traer_todos(self, query, params=None) --para traer todas las filas de una tabla
ej:

    consulta_para_traer_recibos = "SELECT * FROM transaccion WHERE id_inversor = %s"
    id_inversor = 1
    recibos = conector.traer_todos(consulta_para_traer_recibos, (id_inversor,))

"""
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