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