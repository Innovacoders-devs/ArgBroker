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
            return True

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
                id_portafolio=transaccion[1],
                id_accion=transaccion[2],
                cantidad=transaccion[3],
                precio=transaccion[4],
                tipo=transaccion[5],
                fecha=transaccion[6],
                comision=transaccion[7])

                instancia_transacciones_obtenidas.append(transaccion_instanciada)

        except Exception as error:
            raise Exception(f"Error al obtener la lista de acciones de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()  
            return instancia_transacciones_obtenidas  

    def actualizar(self, transaccion, id_transaccion):
        consulta = "UPDATE transaccion SET id_accion = %s, tipo = %s, fecha = %s, precio = %s, cantidad = %s, comision = %s, id_portafolio = %s WHERE id_transaccion = %s"
        valores_a_insertar = (transaccion.id_accion, transaccion.tipo, transaccion.fecha, transaccion.precio, transaccion.cantidad, transaccion.comision, transaccion.id_portafolio, id_transaccion)
        try:
            self._base_de_datos.conectar_a_base_datos()
            self._base_de_datos.ejecutar_consulta(consulta, valores_a_insertar)
            
        except Exception as error:
            raise Exception(f"Error al actualizar la transaccion en la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()
            return True

    def eliminar(self, id_a_eliminar):
        consulta = "DELETE FROM transaccion WHERE id_transaccion = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            self._base_de_datos.ejecutar_consulta(consulta, (id_a_eliminar,))


        except Exception as error:
            raise Exception(f"Error al eliminar la transaccion de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()
            return True

    def obtener_uno(self, id_transaccion):
        consulta = "SELECT * FROM transaccion WHERE id_transaccion = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            transaccion_obtenida = self._base_de_datos.traer_solo_uno(consulta, (id_transaccion,))

            if not transaccion_obtenida:
                raise Exception("No existe transaccion con dicho id")
            
            instancia_transaccion = Transaccion(
                id_transaccion=transaccion_obtenida[0],
                id_portafolio=transaccion_obtenida[1],
                id_accion=transaccion_obtenida[2],
                cantidad=transaccion_obtenida[3],
                precio=transaccion_obtenida[4],
                tipo=transaccion_obtenida[5],
                fecha=transaccion_obtenida[6],
                comision=transaccion_obtenida[7]
            )

        except Exception as error:
            raise Exception(f"Error al obtener la transaccion de la base de datos: {error}")

        finally:
            self._base_de_datos.desconectar_de_base_datos()
            return instancia_transaccion

    def obtener_por_portafolio_y_accion(self, id_portafolio, id_accion):
        consulta = "SELECT * FROM transaccion WHERE id_portafolio = %s AND id_accion = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            resultados = self._base_de_datos.traer_todos(consulta, (id_portafolio, id_accion))
            
            transacciones_instanciadas = []
            
            for resultado in resultados:
                transaccion_instanciada = Transaccion(
                id_transaccion =resultado[0],
                id_portafolio =resultado[1],
                id_accion =resultado[2],
                cantidad =resultado[3],
                precio =resultado[4],
                tipo =resultado[5],
                fecha =resultado[6],
                comision =resultado[7])

                transacciones_instanciadas.append(transaccion_instanciada)
            
            return transacciones_instanciadas
        except Exception as error:
            raise Exception(f"Error al obtener las transacciones por portafolio y acción: {error}")
        finally:
            self._base_de_datos.desconectar_de_base_datos()

    def obtener_por_portafolio(self, id_portafolio):
        consulta = "SELECT * FROM transaccion WHERE id_portafolio = %s"
        try:
            self._base_de_datos.conectar_a_base_datos()
            resultados = self._base_de_datos.traer_todos(consulta, (id_portafolio,))
            
            transacciones_instanciadas = []
            
            for resultado in resultados:
                transaccion_instanciada = Transaccion(
                    id_transaccion=resultado[0],
                    id_portafolio=resultado[1],
                    id_accion=resultado[2],
                    cantidad=resultado[3],
                    precio=resultado[4],
                    tipo=resultado[5],
                    fecha=resultado[6],
                    comision=resultado[7]
                )
                transacciones_instanciadas.append(transaccion_instanciada)
            
            return transacciones_instanciadas
        except Exception as error:
            raise Exception(f"Error al obtener las transacciones por portafolio: {error}")
        finally:
            self._base_de_datos.desconectar_de_base_datos()