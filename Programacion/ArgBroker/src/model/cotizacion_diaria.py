class CotizacionDiaria:
    def __init__(self, _id_cotizacion, _id_accion, _fecha, _ultimo_operado,
                  _cantidad_compra_diaria, _precio_compra_actual, _precio_venta_actual, 
                  _cantidad_venta_diaria,
                  _valor_apertura, _minimo_diario, _maximo_diario, _valor_cierre):
        
        self._id_cotizacion = _id_cotizacion
        self._id_accion = _id_accion
        self._fecha = _fecha   
        self._ultimo_operado = _ultimo_operado
        self._cantidad_compra_diaria = _cantidad_compra_diaria
        self._precio_compra_actual = _precio_compra_actual
        self._precio_venta_actual = _precio_venta_actual
        self._cantidad_venta_diaria = _cantidad_venta_diaria
        self._valor_apertura = _valor_apertura
        self._minimo_diario = _minimo_diario
        self._maximo_diario = _maximo_diario
        self._valor_cierre = _valor_cierre
    
           
        