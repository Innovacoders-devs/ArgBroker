from src.modelo.accion import Accion
from src.modelo.inversor import Inversor

class ComprarAccion:
    def __init__(self, inversor, accion, cantidad, precio):
        self.inversor = inversor
        self.accion = accion
        self.cantidad = cantidad
        self.precio = precio
        self.costo_total = self.cantidad * self.precio

    def ejecutar(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")

        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")

        if self.inversor.saldo_cuenta >= self.costo_total:
            self.inversor.saldo_cuenta -= self.costo_total
            self.registrar_transaccion() 
            self.mostrar_resultado()
        else:
            raise ValueError("Saldo insuficiente para realizar la compra.")

