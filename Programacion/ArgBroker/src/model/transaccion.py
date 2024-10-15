class Transaccion:

    def __init__(self, id_transaccion, id_inversor, id_accion, tipo, fecha, precio, cantidad, comision):
        self._id_transaccion = id_transaccion
        self._id_inversor = id_inversor
        self._id_accion = id_accion
        self._tipo = tipo
        self._fecha = fecha
        self._precio = precio
        self._cantidad = cantidad
        self._comision = comision

    def __str__(self):
        return f""" Detalles de la transaccion: 
                    Transaccion numero: {self._id_transaccion}
                    Inversor: {self._id_inversor}
                    Accion numero: {self._id_accion}
                    Tipo: {self._tipo}
                    Fecha: {self._fecha}
                    Precio: {self._precio}
                    Cantidad: {self._cantidad}
                    Comision: {self._comision}"""
        

    @property
    def id_transaccion(self):
        return self._id_transaccion

    @id_transaccion.setter
    def id_transaccion(self, id_transaccion):
        self._id_transaccion = id_transaccion
    
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