from .dao_interface import DAOInterface
from src.modelo.transaccion import Transaccion

class TransaccionDAO(DAOInterface):
    
    def __init__(self, conector):
        self._base_de_datos = conector
                
    def crear(self, transaccion):
        consulta = "INSERT INTO transaccion (id_accion, tipo, fecha, precio, cantidad, comision, id_portafolio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores_a_insertar = (transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_portafolio)
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
                transaccion_instanciada = Transaccion(
                    id_transaccion=transaccion[0],
                    id_accion=transaccion[1],
                    tipo=transaccion[2],
                    fecha=transaccion[3],
                    precio=transaccion[4],
                    cantidad=transaccion[5],
                    comision=transaccion[6],
                    id_portafolio=transaccion[7]
                )
                instancia_transacciones_obtenidas.append(transaccion_instanciada)

            return instancia_transacciones_obtenidas

        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()    

    def actualizar(self, transaccion):
        consulta = "UPDATE transaccion SET id_accion = %s, tipo = %s, fecha = %s, precio = %s, cantidad = %s, comision = %s, id_portafolio = %s WHERE id_transaccion = %s"
        valores_a_insertar = (transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_portafolio, transaccion.id_transaccion)
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

    def obtener_uno(self, id_portafolio):
        consulta = "SELECT * FROM transaccion WHERE id_portafolio = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            resultados = self._base_de_datos.traer_todos(consulta, (id_portafolio,))
            if resultados:
                return [Transaccion(
                    id_transaccion=resultado[0],
                    id_accion=resultado[1],
                    tipo=resultado[2],
                    fecha=resultado[3],
                    precio=resultado[4],
                    cantidad=resultado[5],
                    comision=resultado[6],
                    id_portafolio=resultado[7]
                ) for resultado in resultados]
            return []
        except Exception as e:
            print(f"Ocurrio un error al obtener transaccion por portafolio: {e}")
        finally:
            self._base_de_datos.desconectar_de_base_datos()

    def obtener_por_portafolio_y_accion(self, id_portafolio, id_accion):
        consulta = "SELECT * FROM transaccion WHERE id_portafolio = %s AND id_accion = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            resultados = self._base_de_datos.traer_todos(consulta, (id_portafolio, id_accion))
            
            transacciones_instanciadas = []
            
            for resultado in resultados:
                transaccion_instanciada = Transaccion(
                    id_transaccion=resultado[0],
                    id_accion=resultado[1],
                    tipo=resultado[2],
                    fecha=resultado[3],
                    precio=resultado[4],
                    cantidad=resultado[5],
                    comision=resultado[6],
                    id_portafolio=resultado[7]
                )
                transacciones_instanciadas.append(transaccion_instanciada)
            
            return transacciones_instanciadas
        except Exception as error:
            raise Exception(f"Error al obtener las transacciones por portafolio y acción: {error}")
        finally:
            self._base_de_datos.desconectar_de_base_datos()