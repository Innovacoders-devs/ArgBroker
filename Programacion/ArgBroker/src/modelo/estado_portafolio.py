class EstadoPortafolio:

    def __init__(self, id_estado_portafolio, id_portafolio, id_accion, cantidad, valor_actual):
        self._id_estado_portafolio = id_estado_portafolio
        self._id_portafolio = id_portafolio
        self._id_accion = id_accion
        self._cantidad = cantidad
        self._valor_actual = valor_actual


    @property
    def id_estado_portafolio(self):
        return self._id_estado_portafolio

    @id_estado_portafolio.setter
    def id_estado_portafolio(self, value):
        self._id_estado_portafolio = value


    @property
    def id_portafolio(self):
        return self._id_portafolio

    @id_portafolio.setter
    def id_portafolio(self, value):
        self._id_portafolio = value

    
    @property
    def id_accion(self):
        return self._id_accion

    @id_accion.setter
    def id_accion(self, value):
        self._id_accion = value

  
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

  
    @property
    def valor_actual(self):
        return self._valor_actual

    @valor_actual.setter
    def valor_actual(self, value):
        self._valor_actual = value
