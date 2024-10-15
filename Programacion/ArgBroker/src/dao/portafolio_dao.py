from dao_interface import DAOInterface
from Portafolio import Portafolio
from src.utils.mysql_connector import MySQLConnector

class PortafolioDAO(DAOInterface):
    def __init__(self):
        self.db_connector = MySQLConnector()

    def crear(self, portafolio):
        sql = """ 
        INSERT INTO portafolio (id_inversor, id_accion, cantidad, precio_promedio_compra) 
        VALUES (%s, %s, %s, %s)
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra)
        try:
            return self.db_connector.execute_query(sql, parametros)
        except Exception as i:
            print(f"Error al crear portafolio: {str(i)}")
            return None

    def obtener(self, id_portafolio):
        sql = """ 
        SELECT * FROM portafolio WHERE id_portafolio = %s
        """
        parametros = (id_portafolio,)
        try:
            resultado = self.db_connector.fetch_one(sql, parametros)
            if resultado:
                return Portafolio(*resultado)  
            return None
        except Exception as i:
            print(f"Error al obtener portafolio con el id {id_portafolio}: {str(i)}")
            return None

    def actualizar(self, portafolio):
        sql = """ 
        UPDATE portafolio 
        SET id_inversor = %s, id_accion = %s, cantidad = %s, precio_promedio_compra = %s
        WHERE id_portafolio = %s
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra, portafolio.id_portafolio)
        try:
            return self.db_connector.execute_query(sql, parametros)
        except Exception as e:
            print(f"Error al actualizar portafolio con el id {portafolio.id_portafolio}: {str(e)}")
            return None

    def eliminar(self, id_portafolio):
        sql = """ 
        DELETE FROM portafolio WHERE id_portafolio = %s
        """
        parametros = (id_portafolio,)
        try:
            return self.db_connector.execute_query(sql, parametros)
        except Exception as e:
            print(f"Error al eliminar portafolio con id {id_portafolio}: {str(e)}")
            return None
