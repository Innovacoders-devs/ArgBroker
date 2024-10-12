from dao_interface import DAOInterface

class PortafolioDAO(DAOInterface):
    def crear(self, portafolio):
        sql= """ 
        INSERT INTO portafolio (id_inversor,id_accion,cantidad,precio_promedio_compra) 
        VALUES (%s,%s,%s,%s)
        """
        parametro_atributos=(portafolio.id_inversor,portafolio.id_accion,portafolio.cantidad,portafolio.precio_promedio_compra)
        return self.db_connector.execute_query(sql,parametro_atributos)


    def obtener(self, portafolio):
        sql= """ 
        SELECT * FROM portafolio WHERE id_portafolio=%s
        """
        parametro_atributos=(portafolio.id_portafolio,)
        return self.db_connector.fetch_one(sql,parametro_atributos)

    def actualizar(self, objeto):
        sql= """ 
        UPDATE  portafolio 
        SET id_inversor=%s,id_accion=%s,cantidad=%s,precio_promedio_compra=%s
        WHERE id_portafolio= %s
        """
        parametro_atributos=(portafolio.id_inversor,portafolio.id_accion,portafolio.cantidad,portafolio.precio_promedio_compra)
       
        return self.db_connector.execute_query(sql,parametro_atributos)
 
    def eliminar(self, id):
        sql= """ 
        DELETE FROM  portafolio WHERE id_portafolio= %s
        """
        parametro_atributos=(portafolio.id_portafolio,)
        return self.db_connector.execute_query(sql,parametro_atributos)
       
        