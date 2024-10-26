from .dao_interface import DAOInterface
from ..modelo.historial_saldo import HistorialSaldo

class HistorialSaldoDAO(DAOInterface):
    def __init__(self, conector):
        self.__base_de_datos = conector

    def crear(self, historial_saldo):
        consulta = """
        INSERT INTO historial_saldo (id_inversor, fecha, saldo_anterior, saldo_nuevo, motivo)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores_a_insertar = (historial_saldo.id_inversor, historial_saldo.fecha, 
                              historial_saldo.saldo_anterior, historial_saldo.saldo_nuevo, 
                              historial_saldo.motivo)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            print(f"Error al crear el historial de saldo en la base de datos: {e}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_uno(self, id_historial_saldo):
        consulta = "SELECT * FROM historial_saldo WHERE id_historial_saldo = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            historial_obtenido = self.__base_de_datos.traer_solo_uno(consulta, (id_historial_saldo,))
            if not historial_obtenido:
                raise Exception("No existe historial de saldo con dicho id")
            return historial_obtenido
        except Exception as error:
            print(f"Error al obtener el historial de saldo de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self):
        consulta = "SELECT * FROM historial_saldo"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            historiales_obtenidos = self.__base_de_datos.traer_todos(consulta)
            if not historiales_obtenidos:
                raise Exception("No se pudo obtener los historiales de saldo")

            objetos = []
            for historial in historiales_obtenidos:
                historial_instanciado = HistorialSaldo(historial[0], historial[1], historial[2], 
                                                        historial[3], historial[4])
                objetos.append(historial_instanciado)
            return objetos
        except Exception as error:
            print(f"Error al obtener la lista de historiales de saldo de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def actualizar(self, historial_saldo):
        consulta = """
        UPDATE historial_saldo
        SET saldo_nuevo = %s, motivo = %s
        WHERE id_historial_saldo = %s
        """
        valores_a_insertar = (historial_saldo.saldo_nuevo, historial_saldo.motivo, historial_saldo.id_historial_saldo)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            print(f"Error al modificar el historial de saldo: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()

    def eliminar(self, id_historial_saldo):
        consulta = "DELETE FROM historial_saldo WHERE id_historial_saldo = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id_historial_saldo,))
            return True
        except Exception as error:
            print(f"Error al eliminar el historial de saldo en la base de datos: {error}")
            return False
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
