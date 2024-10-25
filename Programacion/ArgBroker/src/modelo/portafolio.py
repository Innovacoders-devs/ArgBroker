class Portafolio:
    def __init__(self, id_portafolio = None, id_inversor  = None, id_accion  = None, cantidad  = None, precio_promedio_compra  = None):
        self._id_portafolio = id_portafolio
        self._id_inversor = id_inversor
        self._id_accion = id_accion
        self._cantidad = cantidad
        self._precio_promedio_compra = precio_promedio_compra

    def __str__(self): 
        return (f'Portafolio ID: {self._id_portafolio}, Inversor ID: {self._id_inversor}, '
                f'Acción: {self._id_accion}, Cantidad: {self._cantidad},'
                f'Precio Promedio Compra: {self._precio_promedio_compra}') 
        
    @property
    def id_portafolio(self):
        return self._id_portafolio
    
    @id_portafolio.setter
    def id_portafolio(self, id_portafolio):
        self._id_portafolio = id_portafolio

    @property
    def id_inversor(self):
        return self._id_inversor
    
    @id_inversor.setter
    def id_inversor(self, id_inversor):
        self._id_inversor = id_inversor

    @property
    def id_accion(self):
        return self._id_accion
    
    @id_accion.setter
    def id_accion(self, id_accion):
        self._id_accion = id_accion

    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def precio_promedio_compra(self):
        return self._precio_promedio_compra
    
    @precio_promedio_compra.setter
    def precio_promedio_compra(self, precio_promedio_compra):
        self._precio_promedio_compra = precio_promedio_compra