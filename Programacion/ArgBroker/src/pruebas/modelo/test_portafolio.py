import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.portafolio import Portafolio

def test_portafolio_creation():
    portafolio = Portafolio(id_portafolio=1, id_inversor=100)
    assert portafolio.id_portafolio == 1
    assert portafolio.id_inversor == 100

def test_portafolio_creation_without_ids():
    portafolio = Portafolio()
    assert portafolio.id_portafolio is None
    assert portafolio.id_inversor is None

def test_portafolio_str():
    portafolio = Portafolio(id_portafolio=2, id_inversor=200)
    expected_str = 'Portafolio ID: 2, Inversor ID: 200'
    assert str(portafolio) == expected_str

def test_set_id_portafolio():
    portafolio = Portafolio()
    portafolio.id_portafolio = 3
    assert portafolio.id_portafolio == 3

def test_set_id_inversor():
    portafolio = Portafolio()
    portafolio.id_inversor = 300
    assert portafolio.id_inversor == 300

def test_set_id_portafolio_none():
    portafolio = Portafolio()
    portafolio.id_portafolio = None
    assert portafolio.id_portafolio is None

def test_set_id_inversor_none():
    portafolio = Portafolio()
    portafolio.id_inversor = None
    assert portafolio.id_inversor is None

def test_set_id_portafolio_with_invalid_type():
    portafolio = Portafolio()
    with pytest.raises(TypeError):
        portafolio.id_portafolio = "string_invalido"  # Debe ser un número

def test_set_id_inversor_with_invalid_type():
    portafolio = Portafolio()
    with pytest.raises(TypeError):
        portafolio.id_inversor = "string_invalido"  # Debe ser un número