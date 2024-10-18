from .dao_interface import DAOInterface

class AccionDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, nueva_accion):
        consulta = "INSERT INTO accion (nombre_accion, simbolo_accion) VALUES (%s, %s)"
        valores_a_insertar = (nueva_accion.nombre_accion, nueva_accion.simbolo_accion)

        try:
            with self.__base_de_datos:
                self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al crear la accion de la base de datos: {error}")

    def obtener_uno(self, id_accion):
        consulta = "SELECT * FROM accion WHERE id_accion = %s"
        try:
            with self.__base_de_datos:
                accion_obtenida = self.__base_de_datos.traer_solo_uno(consulta, (id_accion,))
                if not accion_obtenida:
                    raise Exception("No existe accion con dicho id")
                return accion_obtenida
        except Exception as error:
            raise Exception(f"Error al obtener la accion de la base de datos: {error}")

    def obtener_todos(self):
        consulta = "SELECT * FROM accion"
        try:
            with self.__base_de_datos:
                acciones_obtenidas = self.__base_de_datos.traer_todos(consulta)
                if not acciones_obtenidas:
                    raise Exception("No se pudo obtener las acciones")
                return acciones_obtenidas
        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")

    def actualizar(self, nuevos_datos, id):
        consulta = "UPDATE accion SET nombre_accion = %s, simbolo_accion = %s WHERE id_accion = %s"
        valores_a_insertar = (nuevos_datos.nombre_accion, nuevos_datos.simbolo_accion, id)
        try:
            with self.__base_de_datos:
                self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al modificar la accion: {error}")

    def eliminar(self, id):
        consulta = "DELETE FROM accion WHERE id_accion = %s"
        try:
            with self.__base_de_datos:
                self.__base_de_datos.ejecutar_consulta(consulta, (id,))
        except Exception as error:
            raise Exception(f"Error al eliminar la accion: {error}")
