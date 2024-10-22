from dao_interface import DAOInterface
from model.cotizacion_diaria import CotizacionDiaria
from src.utils.mysql_connector import MySQLConnector


class CotizacionDAO(DAOInterface):
    def __init__(self):
        self._conector_mysql = MySQLConnector()

    def crear(self, cotizacion_diaria):



    def crear(self, nueva_cotizacion):
        pass

    def obtener(self, id):
        pass

    def actualizar(self, objeto):
        pass

    def eliminar(self, id):
        pass