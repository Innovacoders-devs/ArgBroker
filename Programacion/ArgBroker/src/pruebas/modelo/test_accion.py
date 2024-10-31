import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.accion import Accion

def test_accion_initialization():
    accion = Accion(1, "Accion Test", "AT")
    assert accion.id_accion == 1
    assert accion.nombre_accion == "Accion Test"
    assert accion.simbolo_accion == "AT"

def test_accion_str():
    accion = Accion(1, "Accion Test", "AT")
    assert str(accion) == "Accion(id_accion = 1, nombre_accion = Accion Test, simbolo_accion = AT)"

def test_nombre_accion_property():
    accion = Accion(1, "Accion Test", "AT")
    accion.nombre_accion = "Nuevo Nombre"
    assert accion.nombre_accion == "Nuevo Nombre"

def test_simbolo_accion_property():
    accion = Accion(1, "Accion Test", "AT")
    accion.simbolo_accion = "NN"
    assert accion.simbolo_accion == "NN"

def test_accion_default_initialization():
    accion = Accion()
    assert accion.id_accion is None
    assert accion.nombre_accion is None
    assert accion.simbolo_accion is None

def test_accion_partial_initialization():
    accion = Accion(nombre_accion="Accion Parcial")
    assert accion.id_accion is None
    assert accion.nombre_accion == "Accion Parcial"
    assert accion.simbolo_accion is None

def test_accion_update_properties():
    accion = Accion(1, "Accion Test", "AT")
    accion.nombre_accion = "Updated Name"
    accion.simbolo_accion = "UN"
    assert accion.nombre_accion == "Updated Name"
    assert accion.simbolo_accion == "UN"

def test_accion_id_property():
    accion = Accion(1, "Accion Test", "AT")
    assert accion.id_accion == 1

def test_accion_no_id_change():
    accion = Accion(1, "Accion Test", "AT")
    with pytest.raises(AttributeError):
        accion.id_accion = 2

def test_accion_empty_string_properties():
    accion = Accion(1, "", "")
    assert accion.nombre_accion == ""
    assert accion.simbolo_accion == ""

def test_accion_none_properties():
    accion = Accion(1, None, None)
    assert accion.nombre_accion is None
    assert accion.simbolo_accion is None