from .dao_interface import DAOInterface
from ..model.accion import Accion
class AccionDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, nueva_accion):
        consulta = "INSERT INTO accion (nombre_accion, simbolo_accion) VALUES (%s, %s)"
        valores_a_insertar = (nueva_accion.nombre_accion, nueva_accion.simbolo_accion)

        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al crear la accion de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_uno(self, id_accion):
        consulta = "SELECT * FROM accion WHERE id_accion = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            accion_obtenida = self.__base_de_datos.traer_solo_uno(consulta, (id_accion,))
            if not accion_obtenida:
                raise Exception("No existe accion con dicho id")
            return accion_obtenida
        except Exception as error:
            raise Exception(f"Error al obtener la accion de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self):
        consulta = "SELECT * FROM accion"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            acciones_obtenidas = self.__base_de_datos.traer_todos(consulta)
            if not acciones_obtenidas:
                raise Exception("No se pudo obtener las acciones")

            objetos = []    

            for accion in acciones_obtenidas:
                accion_instanciada = Accion(accion[0], accion[1], accion[2] )
                objetos.append(accion_instanciada)
            return objetos
        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def actualizar(self, nuevos_datos, id):
        consulta = "UPDATE accion SET nombre_accion = %s, simbolo_accion = %s WHERE id_accion = %s"
        valores_a_insertar = (nuevos_datos.nombre_accion, nuevos_datos.simbolo_accion, id)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al modificar la accion: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def eliminar(self, id):
        consulta = "DELETE FROM accion WHERE id_accion = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id,))
        except Exception as error:
            raise Exception(f"Error al eliminar la accion: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
