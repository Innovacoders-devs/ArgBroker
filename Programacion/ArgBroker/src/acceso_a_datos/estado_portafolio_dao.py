from .dao_interface import DAOInterface
from ..modelo.estado_portafolio import EstadoPortafolio

class EstadoPortafolioDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, estado_portafolio):
        consulta = "INSERT INTO estado_portafolio (id_portafolio, id_accion, nombre_accion, simbolo_accion, cantidad, valor_actual) VALUES (%s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (estado_portafolio.id_portafolio, estado_portafolio.id_accion,
                              estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion,
                              estado_portafolio.cantidad, estado_portafolio.valor_actual)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
            return True
        except Exception as e:
            print(f"Error al crear el estado de portafolio en la base de datos: {e}")
            return False
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def actualizar(self, estado_portafolio, id_estado_a_modificar):
        consulta = "UPDATE estado_portafolio SET id_portafolio = %s, id_accion = %s, nombre_accion = %s, simbolo_accion = %s, cantidad = %s, valor_actual = %s WHERE id_estado_portafolio = %s"
        valores_a_insertar = (estado_portafolio.id_portafolio, estado_portafolio.id_accion,
                              estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion,
                              estado_portafolio.cantidad, estado_portafolio.valor_actual,
                              id_estado_a_modificar)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
            return True
        except Exception as error:
            print(f"Error al modificar el estado de portafolio: {error}")
            return False
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

    def obtener_uno(self, id_estado_portafolio):
        consulta = "SELECT * FROM estado_portafolio WHERE id_estado_portafolio = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            estado_portafolio_obtenido = self.__base_de_datos.traer_solo_uno(consulta, (id_estado_portafolio,))
            if not estado_portafolio_obtenido:
                raise Exception("No existe estado de portafolio con dicho id")
            instancia_estado_portafolio = EstadoPortafolio(
                estado_portafolio_obtenido[0], estado_portafolio_obtenido[1],
                estado_portafolio_obtenido[2], estado_portafolio_obtenido[3],
                estado_portafolio_obtenido[4], estado_portafolio_obtenido[5],
                estado_portafolio_obtenido[6]
            )
            return instancia_estado_portafolio
        except Exception as error:
            raise Exception(f"Error al obtener el estado de portafolio de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self, id_portafolio_inversor):
        consulta = """
        SELECT id_estado_portafolio, id_portafolio, id_accion, nombre_accion, simbolo_accion, cantidad, valor_actual 
        FROM estado_portafolio 
        WHERE id_portafolio = %s
        """
        try:
            self.__base_de_datos.conectar_a_base_datos()
            estados_portafolio_obtenidos = self.__base_de_datos.traer_todos(consulta, (id_portafolio_inversor,))
            if not estados_portafolio_obtenidos:
                return [] 
            estados_portafolio_instanciados = []
            for estado in estados_portafolio_obtenidos:
                estado_instanciado = EstadoPortafolio(
                    estado[0], estado[1], estado[2], estado[3],
                    estado[4], estado[5], estado[6]
                )
                estados_portafolio_instanciados.append(estado_instanciado)
            return estados_portafolio_instanciados
        except Exception as error:
            raise Exception(f"Error al obtener la lista de estados de portafolio de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
