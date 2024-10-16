from dao_interface import DAOInterface
from Portafolio import Portafolio
from src.utils.mysql_connector import MySQLConnector

class PortafolioDAO(DAOInterface):
    def __init__(self):
        self.db_connector = MySQLConnector()

    def crear(self, portafolio): #revisar el mapeo de los valores bro ya que cambie la bdd
        sql = """ 
        INSERT INTO portafolio (id_inversor, id_accion, cantidad, precio_promedio_compra) 
        VALUES (%s, %s, %s, %s) 
        """ #usar nombres descriptivos de las variables, en español para mantener la uniformidad en el codigo 
        parametros = (portafolio.id_inversor, portafolio.id_accion, portafolio.cantidad, portafolio.precio_promedio_compra)
        try:
            return self.db_connector.execute_query(sql, parametros) #verificar porque cambie los metodos del conector
        except Exception as i:
            print(f"Error al crear portafolio: {str(i)}")
            return None #excelente manejo de errores bro lo unico que falta es cerrar la conexion al finalizar la consulta(ver la correccion de cris a crear inversor DAO)

    def obtener(self, id_portafolio): #el dao del portafolio debe poder obtener el portfolio que le pertenezca a un usuario en particular es decir la busqueda se hace sobre la FK(id_inversor) no sobre su respectivo id
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
            return None#cerrar conexion al finalizar el error debe decir explicitamente que no pudo encontrar el portfolio del inversor, no con el id 

    def actualizar(self, portafolio): #actualizar debe permitir reasignar un portfolio a un user, verificar el nuevo mapeo y el cierre de la conexion
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

    def eliminar(self, id_portafolio): #verificar con  correcciones anteriores 
        sql = """ 
        DELETE FROM portafolio WHERE id_portafolio = %s
        """
        parametros = (id_portafolio,)
        try:
            return self.db_connector.execute_query(sql, parametros)
        except Exception as e:
            print(f"Error al eliminar portafolio con id {id_portafolio}: {str(e)}")
            return None
