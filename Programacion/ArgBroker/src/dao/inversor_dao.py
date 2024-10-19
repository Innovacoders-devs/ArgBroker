from dao_interface import DAOInterface
from Inversor import Inversor
from src.utils.mysql_connector import MySQLConnector

class InversorDAO(DAOInterface):
    def __init__(self):
        self._db = MySQLConnector()
    def crear(self, inversor):
        consulta = "INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta, intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
        try:
            self._db.conectar_a_base_datos()
            self._db.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al crear el inversor en la base de datos: {e}")
        finally:
            self._db.desconectar_de_base_datos()


    def obtener(self, id_inversor):
        consulta = "SELECT * FROM inversor WHERE id = %s"
        result = self._db.fetch_one(query, (id_inversor,)) #verificar nuevo nombre del metodo
        if result:
            return Inversor(*result)
        return None #seria mejor retornar una excepcion si no se pudo encontrar, debe cerrar la conexion al finalizar la consulta 

    def actualizar(self, inversor):#verificar mapeo, nombres de variables y descoenctar la base de datos luego de la consulta
        query = """
        UPDATE inversores SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s 
        WHERE id = %s
        """ 
        values = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.id)
        with self._db as db:
            db.execute(query, values)

    def eliminar(self, id_inversor):
        query = "DELETE FROM inversores WHERE id = %s"
        with self._db as db:
            db.execute(query, (id_inversor,))

    def obtener_inversor_por_email(self, email): #este metodo y buscar por id hacen exactamente lo mismo solo que uno busca por id y el otro por email, quizaconvenga mantener este para buscar el usuario por email al iniciar sesion y luego si volvemos a necesitar un usuario lo buscamos directamente por su email (no creo que sea necesario buscar id ya que una vez que el user inicio sesion este persiste en la app hasta que cierra entonces ya tendriamos su respectivo id)
        query = "SELECT * FROM inversores WHERE email = %s"
        result = self._db.fetch_one(query, (email,))
        if result:
            return Inversor(*result)
        return None

    def autenticar(self, email, contrasena): #autenticar es un metodo de la logica de negocio no tendria que estar aqui 
        query = "SELECT * FROM inversores WHERE email = %s AND contrasena = %s"
        result = self._db.fetch_one(query, (email, contrasena))
        return result is not None