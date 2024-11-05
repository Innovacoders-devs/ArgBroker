import sys
import os
import pytest
from unittest.mock import Mock, call

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from estado_portafolio_dao import EstadoPortafolioDAO
from modelo.estado_portafolio import EstadoPortafolio


@pytest.fixture
def mock_conector():
    return Mock()

@pytest.fixture
def estado_portafolio_dao(mock_conector):
    return EstadoPortafolioDAO(mock_conector)

@pytest.fixture
def estado_portafolio():
    return EstadoPortafolio(
        id_estado_portafolio=1,
        id_portafolio=1,
        id_accion=11,
        nombre_accion="YPF",
        simbolo_accion="11",
        cantidad=200,
        valor_actual=150.0
    )

def test_crear_estado_portafolio(estado_portafolio_dao, estado_portafolio, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = estado_portafolio_dao.crear(estado_portafolio)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "INSERT INTO estado_portafolio (id_portafolio, id_accion, nombre_accion, simbolo_accion, cantidad, valor_actual) VALUES (%s, %s, %s, %s, %s, %s)",
        (estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual)
    )

def test_actualizar_estado_portafolio(estado_portafolio_dao, estado_portafolio, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = estado_portafolio_dao.actualizar(estado_portafolio, estado_portafolio.id_estado_portafolio)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "UPDATE estado_portafolio SET id_portafolio = %s, id_accion = %s, nombre_accion = %s, simbolo_accion = %s, cantidad = %s, valor_actual = %s WHERE id_estado_portafolio = %s",
        (estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual, estado_portafolio.id_estado_portafolio)
    )

def test_eliminar_estado_portafolio(estado_portafolio_dao, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = estado_portafolio_dao.eliminar(1)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with("DELETE FROM estado_portafolio WHERE id_estado_portafolio = %s", (1,))

def test_obtener_uno_estado_portafolio(estado_portafolio_dao, mock_conector, estado_portafolio):
    mock_conector.traer_solo_uno.return_value = (1, estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual)
    resultado = estado_portafolio_dao.obtener_uno(1, estado_portafolio.id_accion)
    assert resultado.id_estado_portafolio == estado_portafolio.id_estado_portafolio
    mock_conector.traer_solo_uno.assert_called_once_with(
        "SELECT * FROM estado_portafolio WHERE id_portafolio = %s AND id_accion = %s", (1, estado_portafolio.id_accion)
    )

def test_obtener_todos_estado_portafolio(estado_portafolio_dao, mock_conector, estado_portafolio):
    mock_conector.traer_todos.return_value = [
        (1, estado_portafolio.id_portafolio, estado_portafolio.id_accion, estado_portafolio.nombre_accion, estado_portafolio.simbolo_accion, estado_portafolio.cantidad, estado_portafolio.valor_actual)
    ]
    resultado = estado_portafolio_dao.obtener_todos(estado_portafolio.id_portafolio)
    assert len(resultado) == 1
    assert resultado[0].id_estado_portafolio == estado_portafolio.id_estado_portafolio
    mock_conector.traer_todos.assert_called_once_with(
        "SELECT id_estado_portafolio, id_portafolio, id_accion, nombre_accion, simbolo_accion, cantidad, valor_actual FROM estado_portafolio WHERE id_portafolio = %s", 
        (estado_portafolio.id_portafolio,)
    )