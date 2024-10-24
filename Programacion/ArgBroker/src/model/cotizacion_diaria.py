class CotizacionDiaria:
    def __init__(self, id_cotizacion=None, id_accion=None, fecha=None, ultimo_operado=None,
                 cantidad_compra_diaria=None, precio_compra_actual=None, precio_venta_actual=None,
                 cantidad_venta_diaria=None, valor_apertura=None, minimo_diario=None, maximo_diario=None, valor_cierre=None):
        
        self._id_cotizacion = id_cotizacion
        self._id_accion = id_accion
        self._fecha = fecha   
        self._ultimo_operado = ultimo_operado
        self._cantidad_compra_diaria = cantidad_compra_diaria
        self._precio_compra_actual = precio_compra_actual
        self._precio_venta_actual = precio_venta_actual
        self._cantidad_venta_diaria = cantidad_venta_diaria
        self._valor_apertura = valor_apertura
        self._minimo_diario = minimo_diario
        self._maximo_diario = maximo_diario
        self._valor_cierre = valor_cierre

    
    @property
    def id_cotizacion(self):
        return self._id_cotizacion 

    @property
    def id_accion(self):
        return self._id_accion 

    @property
    def fecha(self):
        return self._fecha

    @property
    def ultimo_operado(self):
        return self._ultimo_operado

    @property
    def cantidad_compra_diaria(self):
        return self._cantidad_compra_diaria

    @property
    def precio_compra_actual(self):
        return self._precio_compra_actual

    @property
    def precio_venta_actual(self): 
        return self._precio_venta_actual

    @property
    def cantidad_venta_diaria(self):
        return self._cantidad_venta_diaria

    @property
    def valor_apertura(self):
        return self._valor_apertura
   
    @property
    def minimo_diario(self):
        return self._minimo_diario      

    @property
    def maximo_diario(self):
        return self._maximo_diario

    @property
    def valor_cierre(self):
        return self._valor_cierre

    
    @id_cotizacion.setter
    def id_cotizacion(self, value):
        self._id_cotizacion = value

    @id_accion.setter
    def id_accion(self, value):
        self._id_accion = value

    @fecha.setter
    def fecha(self, value):
        self._fecha = value

    @ultimo_operado.setter
    def ultimo_operado(self, value):
        self._ultimo_operado = value

    @cantidad_compra_diaria.setter
    def cantidad_compra_diaria(self, value):
        self._cantidad_compra_diaria = value

    @precio_compra_actual.setter
    def precio_compra_actual(self, value):
        self._precio_compra_actual = value

    @precio_venta_actual.setter
    def precio_venta_actual(self, value):
        self._precio_venta_actual = value

    @cantidad_venta_diaria.setter
    def cantidad_venta_diaria(self, value):
        self._cantidad_venta_diaria = value

    @valor_apertura.setter
    def valor_apertura(self, value):
        self._valor_apertura = value

    @minimo_diario.setter
    def minimo_diario(self, value):
        self._minimo_diario = value

    @maximo_diario.setter
    def maximo_diario(self, value):
        self._maximo_diario = value

    @valor_cierre.setter
    def valor_cierre(self, value):
        self._valor_cierre = value

    def __str__(self):
        return (f'Cotizacion Id: {self.id_cotizacion}\n'
                f'Accion Id: {self.id_accion}\n'
                f'Fecha: {self.fecha}\n'
                f'Ultimo operado: {self.ultimo_operado}\n'
                f'Cantidad de compra diaria: {self.cantidad_compra_diaria}\n'
                f'Precio de compra actual: {self.precio_compra_actual}\n'
                f'Precio de venta actual: {self.precio_venta_actual}\n'
                f'Cantidad de venta diaria: {self.cantidad_venta_diaria}\n'
                f'Valor de apertura: {self.valor_apertura}\n'
                f'Minimo diario: {self.minimo_diario}\n'
                f'Maximo diario: {self.maximo_diario}\n'
                f'Valor de cierre: {self.valor_cierre}')
