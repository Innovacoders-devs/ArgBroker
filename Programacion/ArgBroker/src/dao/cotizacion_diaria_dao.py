from .dao_interface import DAOInterface
from ..model.cotizacion_diaria import CotizacionDiaria
from src.utils.mysql_connector import MySQLConnector


class CotizacionDAO(DAOInterface):
    def __init__(self):
        self._conector_mysql = MySQLConnector()

    def crear(self, cotizacion_diaria):
        consulta = """
            INSERT INTO cotizacion (
                id_cotizacion, id_accion, fecha, ultimo_operado,
                cantidad_compra_diaria, precio_compra_actual,
                precio_venta_actual, cantidad_venta_diaria,
                valor_apertura, minimo_diario, maximo_diario,
                valor_cierre
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores_a_insertar = (
            cotizacion_diaria.id_cotizacion,
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
            self._conector_mysql.conectar_a_base_de_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_insertar)
        except Exception as e:
            raise ValueError(f'No se puede realizar la consulta: {e}')
        finally:
            self._conector_mysql.desconectar_base_de_datos()


    def obtener(self, id_cotizacion):
        consulta = "SELECT * FROM cotizacion WHERE id_cotizacion = %s"
        try:
            self._conector_mysql.conectar_a_base_de_datos()
            resultado = self._conector_mysql.traer_solo_uno(consulta, (id_cotizacion,))
            if resultado:
                return CotizacionDiaria(*resultado)
            return None
        except Exception as e:
            raise ValueError(f'Ocurrió un error al consultar la cotización: {e}')
        finally:
            self._conector_mysql.desconectar_base_de_datos()

    def actualizar(self, cotizacion_diaria):
        consulta = """
            UPDATE cotizacion SET 
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
            cotizacion_diaria.valor_cierre,
            cotizacion_diaria.id_cotizacion
        )

        try:
            self._conector_mysql.conectar_a_base_de_datos()
            self._conector_mysql.ejecutar_consulta(consulta, valores_a_actualizar)
        except Exception as e:
            raise ValueError(f'No se puede actualizar la cotización: {e}')
        finally:
            self._conector_mysql.desconectar_base_de_datos()

    def eliminar(self, id_cotizacion):
        consulta = "DELETE FROM cotizacion WHERE id_cotizacion = %s"
        try:
            self._conector_mysql.conectar_a_base_de_datos()
            self._conector_mysql.ejecutar_consulta(consulta, (id_cotizacion,))
            return True
        except Exception as e:
            raise ValueError(f'Error al eliminar la cotización en la base de datos: {e}')
        finally:
            self._conector_mysql.desconectar_base_de_datos()
