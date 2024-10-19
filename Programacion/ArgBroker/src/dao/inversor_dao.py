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

    def actualizar(self, inversor, nuevos_datos, id):
        consulta = "UPDATE inversor SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s, saldo_cuenta = %s, intentos_fallidos = %s WHERE id = %s"
        valores_a_insertar = (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena,inversor.saldo_cuenta, inversor.intentos_fallidos, inversor.id)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            print(f"Error al modificar el inversor: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def eliminar(self, id_inversor):
        consulta = "DELETE FROM inversor WHERE id = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id_inversor,))
            return True
        except Exception as error:
            print(f"Error al eliminar inversor en la base de datos: {error}")
            return False
        finally:
            self.__base_de_datos.desconectar_de_base_datos()