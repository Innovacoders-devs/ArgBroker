class CompraAccion:
    def __init__(self, inversor, accion, cantidad):
        self.inversor = inversor
        self.accion = accion
        self.cantidad = cantidad

    def realizar_compra(self):
        precio_accion = self.accion.precio
        monto_total = precio_accion * self.cantidad

        if self.inversor.saldo_cuenta >= monto_total:
            self.inversor.saldo_cuenta -= monto_total

            fecha_compra = datetime.now()
            historial = HistorialSaldo(
                id_historial_saldo=None,
                id_inversor=self.inversor.id_inversor,
                fecha=fecha_compra,
                saldo_anterior=self.inversor.saldo_cuenta + monto_total,
                saldo_nuevo=self.inversor.saldo_cuenta,
                motivo=f'Compra de {self.cantidad} acciones de {
                    self.accion.nombre_accion}'
            )

            transaccion = Transaccion(
                id_transaccion=None,
                id_accion=self.accion.id_accion,
                tipo='Compra',
                fecha=fecha_compra,
                precio=precio_accion,
                cantidad=self.cantidad,
                comision=self.calcular_comision(monto_total),
                id_portafolio=self.inversor.portafolio.id_portafolio
            )

            print(f'Compra realizada: {self.cantidad} acciones de {
                  self.accion.nombre_accion} a ${precio_accion} cada una.')
        else:
            raise ValueError('Saldo insuficiente para realizar la compra.')

    def calcular_comision(self, monto_total):
        comision = monto_total * 0.02
        return comision
