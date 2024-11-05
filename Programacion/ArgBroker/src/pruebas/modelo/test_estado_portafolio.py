import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.estado_portafolio import EstadoPortafolio

def test_estado_portafolio_initialization():
    estado = EstadoPortafolio(
        id_estado_portafolio=1, id_portafolio=10, id_accion=101,
        nombre_accion="Accion Test", simbolo_accion="AT",
        cantidad=50, valor_actual=200.0
    )
    assert estado.id_estado_portafolio == 1
    assert estado.id_portafolio == 10
    assert estado.id_accion == 101
    assert estado.nombre_accion == "Accion Test"
    assert estado.simbolo_accion == "AT"
    assert estado.cantidad == 50
    assert estado.valor_actual == 200.0

def test_estado_portafolio_default_initialization():
    estado = EstadoPortafolio()
    assert estado.id_estado_portafolio is None
    assert estado.id_portafolio is None
    assert estado.id_accion is None
    assert estado.nombre_accion is None
    assert estado.simbolo_accion is None
    assert estado.cantidad is None
    assert estado.valor_actual is None

def test_estado_portafolio_partial_initialization():
    estado = EstadoPortafolio(id_portafolio=10, nombre_accion="Accion Test")
    assert estado.id_estado_portafolio is None
    assert estado.id_portafolio == 10
    assert estado.nombre_accion == "Accion Test"

def test_estado_portafolio_update_properties():
    estado = EstadoPortafolio()
    estado.id_estado_portafolio = 2
    estado.id_portafolio = 20
    estado.id_accion = 102
    estado.nombre_accion = "Nueva Accion"
    estado.simbolo_accion = "NA"
    estado.cantidad = 100
    estado.valor_actual = 250.0

    assert estado.id_estado_portafolio == 2
    assert estado.id_portafolio == 20
    assert estado.id_accion == 102
    assert estado.nombre_accion == "Nueva Accion"
    assert estado.simbolo_accion == "NA"
    assert estado.cantidad == 100
    assert estado.valor_actual == 250.0

def test_estado_portafolio_str():
    estado = EstadoPortafolio(
        id_estado_portafolio=1, id_portafolio=10, id_accion=101,
        nombre_accion="Accion Test", simbolo_accion="AT",
        cantidad=50, valor_actual=200.0
    )
    expected_str = ("EstadoPortafolio = id_estado_portafolio = 1, id_portafolio = 10, "
                    "id_accion = 101, cantidad = 50, valor_actual = 200.0, "
                    "nombre_accion = Accion Test, simbolo_accion = AT")
    assert str(estado) == expected_str

def test_estado_portafolio_none_properties():
    estado = EstadoPortafolio(id_estado_portafolio=1, id_portafolio=None, valor_actual=None)
    assert estado.id_estado_portafolio == 1
    assert estado.id_portafolio is None
    assert estado.valor_actual is None

def test_estado_portafolio_empty_string_properties():
    estado = EstadoPortafolio(nombre_accion="", simbolo_accion="")
    assert estado.nombre_accion == ""
    assert estado.simbolo_accion == ""