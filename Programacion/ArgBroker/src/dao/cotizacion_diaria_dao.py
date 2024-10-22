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


    def crear(self, nueva_cotizacion):
        pass

    def obtener(self, id):
        pass

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass