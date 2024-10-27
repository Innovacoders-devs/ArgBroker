from .dao_interface import DAOInterface
from ..modelo.accion import Accion
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
            return True


    def obtener_uno(self, id_accion):
        consulta = "SELECT * FROM accion WHERE id_accion = %s"

        try:
            self.__base_de_datos.conectar_a_base_datos()
            accion_obtenida = self.__base_de_datos.traer_solo_uno(consulta, (id_accion,))

            if not accion_obtenida:
                raise Exception("No existe accion con dicho id")
            instancia_accion = Accion(accion_obtenida[0], accion_obtenida[1],accion_obtenida[2] )
            

        except Exception as error:
            raise Exception(f"Error al obtener la accion de la base de datos: {error}")

        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return instancia_accion


    def obtener_todos(self):
        consulta = "SELECT * FROM accion"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            acciones_obtenidas = self.__base_de_datos.traer_todos(consulta)
            
            if not acciones_obtenidas:
                raise Exception("No se pudo obtener las acciones")

            acciones_obtenidas_y_instanciadas = []    

            for accion in acciones_obtenidas:
                accion_instanciada = Accion(accion[0], accion[1], accion[2] )
                acciones_obtenidas_y_instanciadas.append(accion_instanciada)
                
        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")

        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return acciones_obtenidas_y_instanciadas

    def actualizar(self, nuevos_datos, id_accion_a_modificar):
        consulta = "UPDATE accion SET nombre_accion = %s, simbolo_accion = %s WHERE id_accion = %s"
        valores_a_insertar = (nuevos_datos.nombre_accion, nuevos_datos.simbolo_accion, id_accion_a_modificar)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
            

        except Exception as error:
            raise Exception(f"Error al modificar la accion: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return True

    def eliminar(self, id):
        consulta = "DELETE FROM accion WHERE id_accion = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id,))
            

        except Exception as error:
            raise Exception(f"Error al eliminar la accion: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return True
