from .dao_interface import DAOInterface
from ..modelo.portafolio import Portafolio
#from src.utils.mysql_connector import conector

class PortafolioDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, portafolio):
        consulta = """ 
        INSERT INTO portafolio (id_inversor, id_accion, cantidad, precio_promedio_compra) 
        VALUES (%s, %s, %s, %s) 
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, parametros)
        except Exception as error:
            print(f"Error al crear el portafolio en la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def actualizar(self, portafolio):
        sql = """ 
        UPDATE portafolio 
        SET id_inversor = %s, id_accion = %s, cantidad = %s, precio_promedio_compra = %s
        WHERE id_portafolio = %s
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra, portafolio.id_portafolio)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(sql, parametros)
        except Exception as error:
            print(f"Error al modificar el portafolio con id {portafolio.id_portafolio}: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def eliminar(self, id_portafolio):
        sql = """ 
        DELETE FROM portafolio WHERE id_portafolio = %s
        """
        parametros = (id_portafolio,)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(sql, parametros)
            return True
        except Exception as error:
            print(f"Error al eliminar el portafolio en la base de datos: {error}")
            return False
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self):
        consulta = "SELECT id_portafolio, id_inversor FROM portafolio"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            portafolios_obtenidos = self.__base_de_datos.traer_todos(consulta)

            instancias_de_portafolio = []

            for portafolio in portafolios_obtenidos:
                iteracion_de_portafolio = Portafolio(
                    id_portafolio=portafolio[0],
                    id_inversor=portafolio[1]
                )
                instancias_de_portafolio.append(iteracion_de_portafolio)

            return instancias_de_portafolio

        except Exception as e:
            raise Exception(f'Ocurrió un error {e}')
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_uno(self, id_inversor):
        sql = "SELECT id_portafolio, id_inversor FROM portafolio WHERE id_inversor = %s"
        parametros = (id_inversor,)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            portafolios_obtenidos = self.__base_de_datos.traer_todos(sql, parametros)
            if not portafolios_obtenidos:
                raise Exception("No existe el portafolio para este inversor.")
            
            objetos = []
            for fila in portafolios_obtenidos:
                portafolio_instanciado = Portafolio(
                    id_portafolio=fila[0],
                    id_inversor=fila[1]
                )
                objetos.append(portafolio_instanciado)
            return objetos
        except Exception as error:
            print(f"Error al obtener el portafolio del inversor: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
