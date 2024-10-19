from dao_interface import DAOInterface
from Portafolio import Portafolio
from src.utils.mysql_connector import MySQLConnector

class PortafolioDAO(DAOInterface):
    def __init__(self):
        self.conector_bd = MySQLConnector()

    def crear(self, portafolio):
        sql = """ 
        INSERT INTO portafolio (id_inversor, id_accion, cantidad, precio_promedio_compra) 
        VALUES (%s, %s, %s, %s) 
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra)
        try:
            resultado = self.conector_bd.ejecutar_consulta(sql, parametros)
            return resultado
        except Exception as error:
            print(f"Error al crear portafolio: {str(error)}")
            return None
        finally:
            self.conector_bd.cerrar_conexion()

    def obtener_portafolio_inversor(self, id_inversor):
        sql = """ 
        SELECT * FROM portafolio WHERE id_inversor = %s
        """
        parametros = (id_inversor,)
        try:
            resultado = self.conector_bd.consultar_un_registro(sql, parametros)
            if resultado:
                return Portafolio(*resultado)
            return None
        except Exception as error:
            print(f"No se pudo encontrar el portafolio del inversor con id {id_inversor}: {str(error)}")
            return None
        finally:
            self.conector_bd.cerrar_conexion()

    def actualizar(self, portafolio):
        sql = """ 
        UPDATE portafolio 
        SET id_inversor = %s, id_accion = %s, cantidad = %s, precio_promedio_compra = %s
        WHERE id_portafolio = %s
        """
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra, portafolio.id_portafolio)
        try:
            resultado = self.conector_bd.ejecutar_consulta(sql, parametros)
            return resultado
        except Exception as error:
            print(f"Error al actualizar portafolio con id {portafolio.id_portafolio}: {str(error)}")
            return None
        finally:
            self.conector_bd.cerrar_conexion()

    def eliminar(self, id_portafolio):
        sql = """ 
        DELETE FROM portafolio WHERE id_portafolio = %s
        """
        parametros = (id_portafolio,)
        try:
            resultado = self.conector_bd.ejecutar_consulta(sql, parametros)
            return resultado
        except Exception as error:
            print(f"Error al eliminar portafolio con id {id_portafolio}: {str(error)}")
            return None
        finally:
            self.conector_bd.cerrar_conexion()
