class Transaccion:

    def __init__(self, id_transaccion=None, id_accion=None, tipo=None, fecha=None, precio=None, cantidad=None, id_portafolio=None, comision=None):
        self._id_transaccion = id_transaccion
        self._id_accion = id_accion
        self._tipo = tipo
        self._fecha = fecha
        self._precio = precio
        self._cantidad = cantidad
        self._comision = comision
        self._id_portafolio = id_portafolio

    def __str__(self):
            return f"""Detalles de la transaccion: 
                    Transaccion numero: {self._id_transaccion}
                    Accion numero: {self._id_accion}
                    Tipo: {self._tipo}
                    Fecha: {self._fecha}
                    Precio: {self._precio}
                    Cantidad: {self._cantidad}
                    Portafolio: {self._id_portafolio}
                    Comision: {self._comision}"""
        
    @property
    def id_transaccion(self):
        return self._id_transaccion

    @id_transaccion.setter
    def id_transaccion(self, id_transaccion):
        self._id_transaccion = id_transaccion
    
    @property
    def id_accion(self):
        return self._id_accion

    @id_accion.setter
    def id_accion(self, id_accion):
        self._id_accion = id_accion
    
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
    
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
    
    @property
    def comision(self):
        return self._comision

    @comision.setter
    def comision(self, comision):
        self._comision = comision

    @property
    def id_portafolio(self):
        return self._id_portafolio

    @id_portafolio.setter
    def id_portafolio(self, id_portafolio):
        self._id_portafolio = id_portafolio

    def obtener_monto_total(self):
        return self._cantidad * self._precio
