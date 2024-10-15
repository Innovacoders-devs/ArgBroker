class CotizacionDiaria:
    def __init__(self, id_cotizacion, id_accion, fecha, ultimo_operado,
                  cantidad_compra_diaria, precio_compra_actual, precio_venta_actual, 
                  cantidad_venta_diaria,
                  valor_apertura, minimo_diario, maximo_diario, valor_cierre):
        
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
    return self.fecha

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
def  valor_apertura(self):
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
