import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.transaccion import Transaccion

def test_transaccion_initialization():
    transaccion = Transaccion(1, 101, "Compra", "2023-10-01", 100.5, 10, 5, 2.5)
    assert transaccion.id_transaccion == 1
    assert transaccion.id_accion == 101
    assert transaccion.tipo == "Compra"
    assert transaccion.fecha == "2023-10-01"
    assert transaccion.precio == 100.5
    assert transaccion.cantidad == 10
    assert transaccion.id_portafolio == 5
    assert transaccion.comision == 2.5

def test_transaccion_str():
    transaccion = Transaccion(1, 101, "Compra", "2023-10-01", 100.5, 10, 5, 2.5)
    assert str(transaccion) == """Detalles de la transaccion: 
                    Transaccion numero: 1
                    Accion numero: 101
                    Tipo: Compra
                    Fecha: 2023-10-01
                    Precio: 100.5
                    Cantidad: 10
                    Portafolio: 5
                    Comision: 2.5"""

def test_transaccion_default_initialization():
    transaccion = Transaccion()
    assert transaccion.id_transaccion is None
    assert transaccion.id_accion is None
    assert transaccion.tipo is None
    assert transaccion.fecha is None
    assert transaccion.precio is None
    assert transaccion.cantidad is None
    assert transaccion.id_portafolio is None
    assert transaccion.comision is None

def test_transaccion_partial_initialization():
    transaccion = Transaccion(id_accion=101, tipo="Venta")
    assert transaccion.id_accion == 101
    assert transaccion.tipo == "Venta"
    assert transaccion.fecha is None
    assert transaccion.precio is None
    assert transaccion.cantidad is None

def test_transaccion_update_properties():
    transaccion = Transaccion()
    transaccion.id_transaccion = 2
    transaccion.id_accion = 102
    transaccion.tipo = "Compra"
    transaccion.fecha = "2023-10-10"
    transaccion.precio = 150.0
    transaccion.cantidad = 5
    transaccion.id_portafolio = 3
    transaccion.comision = 3.0

    assert transaccion.id_transaccion == 2
    assert transaccion.id_accion == 102
    assert transaccion.tipo == "Compra"
    assert transaccion.fecha == "2023-10-10"
    assert transaccion.precio == 150.0
    assert transaccion.cantidad == 5
    assert transaccion.id_portafolio == 3
    assert transaccion.comision == 3.0

def test_transaccion_obtener_monto_total():
    transaccion = Transaccion(precio=200.0, cantidad=3)
    assert transaccion.obtener_monto_total() == 600.0

def test_transaccion_obtener_monto_total_no_cantidad():
    transaccion = Transaccion(precio=200.0, cantidad=0)
    assert transaccion.obtener_monto_total() == 0.0

def test_transaccion_none_properties():
    transaccion = Transaccion(id_transaccion=1, id_accion=None, tipo=None, fecha=None)
    assert transaccion.id_transaccion == 1
    assert transaccion.id_accion is None
    assert transaccion.tipo is None
    assert transaccion.fecha is None

def test_transaccion_empty_string_properties():
    transaccion = Transaccion(tipo="", fecha="", comision=0)
    assert transaccion.tipo == ""
    assert transaccion.fecha == ""
    assert transaccion.comision == 0