class CotizacionDiaria:
    def __init__(self, id_cotizacion, id_accion, fecha, ultimo_operado,
                  cantidad_compra_diaria, precio_compra_actual, precio_venta_actual, 
                  cantidad_venta_diaria,
                  valor_apertura, minimo_diario, maximo_diario, valor_cierre):
        
        self.id_cotizacion  =   id_cotizacion
        self.id_accion  =   id_accion
        self.fecha  =   fecha   
        self.ultimo_operado =   ultimo_operado
        self.cantidad_compra_diaria =   cantidad_compra_diaria
        self.precio_compra_actual   =   precio_compra_actual
        self.precio_venta_actual    =   precio_venta_actual
        self.centidad_venta_diaria  =   cantidad_venta_diaria
        self.valor_apertura =   valor_apertura
        self.minimo_diario  =   minimo_diario
        self.maximo_diario  =   maximo_diario
        self.valor_cierre   =   valor_cierre
        