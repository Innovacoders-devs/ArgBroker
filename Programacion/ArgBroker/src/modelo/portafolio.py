class Portafolio:
    def __init__(self, id_portafolio=None, id_inversor=None):
        self._id_portafolio = id_portafolio
        self._id_inversor = id_inversor

    def __str__(self):
        return (f'Portafolio ID: {self._id_portafolio}, Inversor ID: {self._id_inversor}')

    @property
    def id_portafolio(self):
        return self._id_portafolio

    @id_portafolio.setter
    def id_portafolio(self, id_portafolio):
        if not isinstance(id_portafolio, int):
            raise TypeError("id_portafolio must be an integer")
        self._id_portafolio = id_portafolio

    @property
    def id_inversor(self):
        return self._id_inversor

    @id_inversor.setter
    def id_inversor(self, id_inversor):
        if not isinstance(id_inversor, int):
            raise TypeError("id_inversor must be an integer")
        self._id_inversor = id_inversor
