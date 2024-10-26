from .dao_interface import DAOInterface
from ..modelo.estado_portafolio import EstadoPortafolio

class EstadoPortafolioDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, estado_portafolio):
        consulta = "INSERT INTO estado_portafolio (id_portafolio, id_accion, cantidad, valor_actual) VALUES (%s, %s, %s, %s)"
        valores_a_insertar = (estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al crear el estado de portafolio en la base de datos: {e}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def actualizar(self, estado_portafolio):
        consulta = "UPDATE estado_portafolio SET id_portafolio = %s, id_accion = %s, cantidad = %s, valor_actual = %s WHERE id_estado_portafolio = %s"
        valores_a_insertar = (estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual, estado_portafolio.id_estado_portafolio)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            print(f"Error al modificar el estado de portafolio: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def eliminar(self, id_estado_portafolio):
        consulta = "DELETE FROM estado_portafolio WHERE id_estado_portafolio = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id_estado_portafolio,))
            return True
        except Exception as error:
            print(f"Error al eliminar estado de portafolio en la base de datos: {error}")
            return False
        finally:
            self.__base_de_datos.desconectar_de_base_datos() 
