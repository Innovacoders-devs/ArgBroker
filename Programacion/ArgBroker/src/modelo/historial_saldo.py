class HistorialSaldo:
    def __init__(self, id_historial_saldo = None, id_inversor = None, fecha = None, saldo_anterior = None, saldo_nuevo = None, motivo = None):
        self._id_historial_saldo = id_historial_saldo
        self._id_inversor = id_inversor
        self._fecha = fecha
        self._saldo_anterior = saldo_anterior
        self._saldo_nuevo = saldo_nuevo
        self._motivo = motivo

    def __str__(self):
            return (f"HistorialSaldo id_historial_saldo = {self._id_historial_saldo}, "
                    f"id_inversor = {self._id_inversor}, fecha = {self._fecha}, "
                    f"saldo_anterior = {self._saldo_anterior}, saldo_nuevo = {self._saldo_nuevo}, "
                    f"motivo = {self._motivo}")

    @property
    def id_historial_saldo(self):
        return self._id_historial_saldo

    @id_historial_saldo.setter
    def id_historial_saldo(self, value):
        self._id_historial_saldo = value


    @property
    def id_inversor(self):
        return self._id_inversor

    @id_inversor.setter
    def id_inversor(self, value):
        self._id_inversor = value

   
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        self._fecha = value
   
    @property
    def saldo_anterior(self):
        return self._saldo_anterior

    @saldo_anterior.setter
    def saldo_anterior(self, value):
        self._saldo_anterior = value

    @property
    def saldo_nuevo(self):
        return self._saldo_nuevo

    @saldo_nuevo.setter
    def saldo_nuevo(self, value):
        self._saldo_nuevo = value

    @property
    def motivo(self):
        return self._motivo

    @motivo.setter
    def motivo(self, value):
        self._motivo = value

    