from .dao_interface import DAOInterface
from ..modelo.cotizacion_diaria import CotizacionDiaria

class CotizacionDAO(DAOInterface):
    def __init__(self, conector):
        self._conector_mysql = conector

    def crear(self, cotizacion_diaria):
        consulta = """
            INSERT INTO cotizacion_diaria (
                id_accion, 
                fecha, 
                ultimo_operado,
                cantidad_compra_diaria, 
                precio_compra_actual,
                precio_venta_actual,
                cantidad_venta_diaria,
                valor_apertura,
                minimo_diario, 
                maximo_diario,
                valor_cierre
            ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores_a_insertar = (
            cotizacion_diaria.id_accion,
            cotizacion_diaria.fecha,
            cotizacion_diaria.ultimo_operado,
            cotizacion_diaria.cantidad_compra_diaria,
            cotizacion_diaria.precio_compra_actual,
            cotizacion_diaria.precio_venta_actual,
            cotizacion_diaria.cantidad_venta_diaria,
            cotizacion_diaria.valor_apertura,
            cotizacion_diaria.minimo_diario,
            cotizacion_diaria.maximo_diario,
            cotizacion_diaria.valor_cierre
        )

        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_insertar)
            
            
        except Exception as e:
            raise ValueError(f'No se puede realizar la consulta: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return True


    def obtener_uno(self, id_cotizacion):
        consulta = "SELECT * FROM cotizacion_diaria WHERE id_cotizacion = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            cotizaciones_obtenidas = self._conector_mysql.traer_solo_uno(consulta, (id_cotizacion,))

            if not cotizaciones_obtenidas:
                raise Exception("No existe cotizacion con dicho id")

            instancia_cotizacion = CotizacionDiaria(
                id_cotizacion=cotizaciones_obtenidas[0],
                id_accion=cotizaciones_obtenidas[1],
                fecha=cotizaciones_obtenidas[2],
                ultimo_operado=cotizaciones_obtenidas[3],
                cantidad_compra_diaria=cotizaciones_obtenidas[4],
                precio_compra_actual=cotizaciones_obtenidas[5],
                precio_venta_actual=cotizaciones_obtenidas[6],
                cantidad_venta_diaria=cotizaciones_obtenidas[7],
                valor_apertura=cotizaciones_obtenidas[8],
                minimo_diario=cotizaciones_obtenidas[9],
                maximo_diario=cotizaciones_obtenidas[10],
                valor_cierre=cotizaciones_obtenidas[11]
            )
            

        except Exception as e:
            raise ValueError(f'Ocurrió un error al consultar la cotización: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return instancia_cotizacion

    def obtener_todos(self, id_accion):
        consulta = "SELECT * FROM cotizacion_diaria WHERE id_accion = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            cotizaciones_obtenidas = self._conector_mysql.traer_todos(consulta, (id_accion,))

            instancias_de_cotizacion = []

            for cotizacion in cotizaciones_obtenidas:
                iteracion_de_cotizacion = CotizacionDiaria( 
                    id_cotizacion=cotizacion[0],
                 id_accion=cotizacion[1],
                 fecha=cotizacion[2],
                 ultimo_operado=cotizacion[3],
                 cantidad_compra_diaria=cotizacion[4],
                 precio_compra_actual=cotizacion[5],
                 precio_venta_actual=cotizacion[6],
                 cantidad_venta_diaria=cotizacion[7],
                 valor_apertura=cotizacion[8],
                 minimo_diario=cotizacion[9],
                 maximo_diario=cotizacion[10],
                 valor_cierre=cotizacion[11])

                instancias_de_cotizacion.append(iteracion_de_cotizacion)

            
        
        except Exception as e: 
            raise Exception (f'Ocurrio un error {e}' )
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return instancias_de_cotizacion


    def actualizar(self, cotizacion_modificada, id_de_cotizacion_a_modificar):
        consulta = """
            UPDATE cotizacion_diaria SET 
                id_accion = %s,
                fecha = %s,
                ultimo_operado = %s,
                cantidad_compra_diaria = %s,
                precio_compra_actual = %s,
                precio_venta_actual = %s,
                cantidad_venta_diaria = %s,
                valor_apertura = %s,
                minimo_diario = %s,
                maximo_diario = %s,
                valor_cierre = %s
            WHERE id_cotizacion = %s
        """
        valores_a_actualizar = (
            cotizacion_modificada.id_accion,
            cotizacion_modificada.fecha,
            cotizacion_modificada.ultimo_operado,
            cotizacion_modificada.cantidad_compra_diaria,
            cotizacion_modificada.precio_compra_actual,
            cotizacion_modificada.precio_venta_actual,
            cotizacion_modificada.cantidad_venta_diaria,
            cotizacion_modificada.valor_apertura,
            cotizacion_modificada.minimo_diario,
            cotizacion_modificada.maximo_diario,
            cotizacion_modificada.valor_cierre,
            id_de_cotizacion_a_modificar
        )

        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_actualizar)
        
            return True
            
        except Exception as e:
            raise ValueError(f'No se puede actualizar la cotización: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return True
        

    def eliminar(self, id_cotizacion):
        consulta = "DELETE FROM cotizacion_diaria WHERE id_cotizacion = %s"
        try:
            self._conector_mysql.conectar_a_base_datos()
            self._conector_mysql.ejecutar_consulta(consulta, (id_cotizacion,))
            
        except Exception as e:
            raise ValueError(f'Error al eliminar la cotización en la base de datos: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return True
    
    def obtener_ultima_cotizacion(self, id_accion):
        consulta = """
            SELECT * FROM cotizacion_diaria WHERE id_accion = %s 
            ORDER BY fecha DESC LIMIT 1
        """
        try:
            self._conector_mysql.conectar_a_base_datos()
            cotizacion_obtenida = self._conector_mysql.traer_solo_uno(consulta, (id_accion,))

            if not cotizacion_obtenida:
                raise Exception("No existe cotización para dicha acción")

            instancia_cotizacion = CotizacionDiaria(
                id_cotizacion=cotizacion_obtenida[0],
                id_accion=cotizacion_obtenida[1],
                fecha=cotizacion_obtenida[2],
                ultimo_operado=cotizacion_obtenida[3],
                cantidad_compra_diaria=cotizacion_obtenida[4],
                precio_compra_actual=cotizacion_obtenida[5],
                precio_venta_actual=cotizacion_obtenida[6],
                cantidad_venta_diaria=cotizacion_obtenida[7],
                valor_apertura=cotizacion_obtenida[8],
                minimo_diario=cotizacion_obtenida[9],
                maximo_diario=cotizacion_obtenida[10],
                valor_cierre=cotizacion_obtenida[11]
            )
            
        except Exception as e:
            raise ValueError(f'Ocurrió un error al consultar la última cotización: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return instancia_cotizacion
            
    def obtener_por_accion(self, id_accion):
        consulta = "SELECT * FROM cotizacion_diaria WHERE id_accion = %s ORDER BY fecha DESC LIMIT 1"
        try:
            self._conector_mysql.conectar_a_base_datos()
            cotizacion_obtenida = self._conector_mysql.traer_solo_uno(consulta, (id_accion,))
            if not cotizacion_obtenida:
                return None
            cotizacion = CotizacionDiaria(
                id_cotizacion=cotizacion_obtenida[0],
                id_accion=cotizacion_obtenida[1],
                fecha=cotizacion_obtenida[2],
                ultimo_operado=cotizacion_obtenida[3],
                cantidad_compra_diaria=cotizacion_obtenida[4],
                precio_compra_actual=cotizacion_obtenida[5],
                precio_venta_actual=cotizacion_obtenida[6],
                cantidad_venta_diaria=cotizacion_obtenida[7],
                valor_apertura=cotizacion_obtenida[8],
                minimo_diario=cotizacion_obtenida[9],
                maximo_diario=cotizacion_obtenida[10],
                valor_cierre=cotizacion_obtenida[11]
            )
        except Exception as e:
            raise ValueError(f'Ocurrió un error al consultar la cotización por acción: {e}')
        finally:
            self._conector_mysql.desconectar_de_base_datos()
            return cotizacion


