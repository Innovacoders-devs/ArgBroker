from .dao_interface import DAOInterface
from src.model.transaccion import Transaccion

class TransaccionDAO(DAOInterface):
    
    def __init__(self, conector):
        self._base_de_datos = conector
                
    def crear(self, transaccion):
        consulta = "INSERT INTO transaccion (id_inversor, id_accion, tipo, fecha, precio, cantidad, comision, id_portafolio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (transaccion.id_inversor, transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_portafolio)
        try:
            self._base_de_datos.conectar_a_base_datos()
            self._base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al crear la transaccion en la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()

    def obtener_todos(self):
        consulta = "SELECT * FROM transaccion"
        try:
            self._base_de_datos.conectar_a_base_datos()
            transacciones_obtenidas = self._base_de_datos.traer_todos(consulta)
            
            if not transacciones_obtenidas:
                raise Exception("No se pudo obtener las transacciones")

            instancia_transacciones_obtenidas = []    

            for transaccion in transacciones_obtenidas:
                transaccion_instanciada = Transaccion(transaccion[0], transaccion[1], transaccion[2],transaccion[3], transaccion[4], transaccion[5],transaccion[6], transaccion[7], transaccion[8])
                instancia_transacciones_obtenidas.append(transaccion_instanciada)

            return instancia_transacciones_obtenidas

        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()    

    def actualizar(self, transaccion):
        consulta = "UPDATE transaccion SET id_inversor = %s, id_accion = %s, tipo = %s, fecha = %s, precio = %s, cantidad = %s, comision = %s WHERE id_transaccion = %s"
        valores_a_insertar = (transaccion.id_inversor, transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_transaccion)
        try:
            self._base_de_datos.conectar_a_base_datos()
            self._base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as error:
            raise Exception(f"Error al actualizar la transaccion en la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()

    def eliminar(self, transaccion):
        consulta = "DELETE FROM transaccion WHERE id_transaccion = %s"
        valores_a_eliminar = (transaccion.id_transaccion,)
        try:
            self._base_de_datos.conectar_a_base_datos()
            self._base_de_datos.ejecutar_consulta(consulta, valores_a_eliminar)
        except Exception as error:
            raise Exception(f"Error al eliminar la transaccion de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()

    def obtener_uno(self, id_inversor):
        consulta = "SELECT * FROM transaccion WHERE id_inversor = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            resultados = self._base_de_datos.traer_todos(consulta, (id_inversor,))
            if resultados:
                return [Transaccion(*resultado) for resultado in resultados]
            return []
        except Exception as e:
            print(f"Ocurrio un error al obtener transaccion por inversor: {e}")
        finally:
            self._base_de_datos.desconectar_de_base_datos()