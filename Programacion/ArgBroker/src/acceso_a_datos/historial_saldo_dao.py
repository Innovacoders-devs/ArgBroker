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
            raise Exception(f"Error al crear el historial de saldo en la base de datos: {e}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return True

    def obtener_uno(self, id_historial_saldo):
        consulta = "SELECT * FROM historial_saldo WHERE id_historial_saldo = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            historial_obtenido = self.__base_de_datos.traer_solo_uno(consulta, (id_historial_saldo,))
            if not historial_obtenido:
                raise Exception("No existe historial de saldo con dicho id")
            
            historial_instanciado = HistorialSaldo(historial_obtenido[0], historial_obtenido[1], historial_obtenido[2], 
                                                historial_obtenido[3], historial_obtenido[4], historial_obtenido[5])
            
            
        except Exception as error:
            raise Exception(f"Error al obtener el historial de saldo de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return historial_instanciado

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
                
            
        except Exception as error:
            raise Exception(f"Error al obtener la lista de historiales de saldo de la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return objetos

    def actualizar(self, historial_saldo, id_historial_saldo_a_modificar):
        consulta = """
        UPDATE historial_saldo
        SET saldo_nuevo = %s, motivo = %s
        WHERE id_historial_saldo = %s
        """
        valores_a_insertar = (historial_saldo.saldo_nuevo, historial_saldo.motivo, id_historial_saldo_a_modificar)
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
            
            
        except Exception as error:
            raise Exception(f"Error al modificar el historial de saldo: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return True

    def eliminar(self, id_historial_saldo):
        consulta = "DELETE FROM historial_saldo WHERE id_historial_saldo = %s"
        try:
            self.__base_de_datos.conectar_a_base_datos()
            self.__base_de_datos.ejecutar_consulta(consulta, (id_historial_saldo,))
            
        except Exception as error:
            raise Exception(f"Error al eliminar el historial de saldo en la base de datos: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return True

    def buscar_ultimo_saldo(self, id_inversor):
        consulta = """
        SELECT * FROM historial_saldo WHERE id_inversor = %s
        ORDER BY fecha DESC LIMIT 1
        """
        try:
            self.__base_de_datos.conectar_a_base_datos()
            resultado = self.__base_de_datos.traer_solo_uno(consulta, (id_inversor,))
            if not resultado:
                raise Exception("No se encontró historial de saldo para el inversor con el ID proporcionado.")
            
            ultimo_historial = HistorialSaldo(resultado[0], resultado[1], resultado[2], 
                                            resultado[3], resultado[4], resultado[5])
        except Exception as error:
            raise Exception(f"Error al buscar el último saldo del inversor: {error}")
        finally:
            self.__base_de_datos.desconectar_de_base_datos()
            return ultimo_historial