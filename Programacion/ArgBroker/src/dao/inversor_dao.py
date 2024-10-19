from .dao_interface import DAOInterface
from ..model.inversor import Inversor
from src.utils.mysql_connector import conector

class InversorDAO(DAOInterface):
    def __init__(self):
        self.__base_de_datos = conector
    def crear(self, inversor):
        consulta = "INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta, intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al crear el inversor en la base de datos: {e}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()


    def obtener_uno(self, id_inversor):
        consulta = "SELECT * FROM inversor WHERE id = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            inversor_obtenido = self.__base_de_datos.traer_solo_uno(consulta, (id_inversor,))
            if not inversor_obtenido:
                raise Exception("No existe inversor con dicho id")
            return inversor_obtenido
        except Exception as error:
            print(f"Error al obtener el inversor de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self, id_inversor):
        consulta = "SELECT * FROM inversor"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            inversores_obtenidos = self.__base_de_datos.traer_todos(consulta)
            if not inversores_obtenidos:
                raise Exception("No se pudo obtener los inversores")

            objetos = []

            for inversor in inversores_obtenidos:
                inversor_instanciado = Inversor(inversor[0], inversor[1], inversor[2], inversor[3], inversor[4], inversor[5], inversor[6])
                objetos.append(inversor_instanciado)
            return objetos
        except Exception as error:
            print(f"Error al obtener la lista de inversores de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

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