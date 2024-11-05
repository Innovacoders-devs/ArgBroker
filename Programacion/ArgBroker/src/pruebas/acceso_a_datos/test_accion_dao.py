import sys
import os
import pytest
from unittest.mock import MagicMock, create_autospec

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from acceso_a_datos.accion_dao import AccionDAO
from modelo.accion import Accion
from acceso_a_datos.dao_interface import DAOInterface



@pytest.fixture
def mock_conector():
    conector = MagicMock()
    return conector


@pytest.fixture
def accion_dao(mock_conector):
    return AccionDAO(mock_conector)


@pytest.fixture
def accion():
    return Accion(id_accion=1, nombre_accion="Test Accion", simbolo_accion="TEST")


def test_crear_accion(accion_dao, accion):
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.return_value = None
    
    resultado = accion_dao.crear(accion)
    assert resultado is True
    
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.assert_called_once_with(
        "INSERT INTO accion (nombre_accion, simbolo_accion) VALUES (%s, %s)", 
        (accion.nombre_accion, accion.simbolo_accion)
    )


def test_obtener_uno_accion(accion_dao, mock_conector, accion):
    mock_conector.traer_solo_uno.return_value = (accion.id_accion, accion.nombre_accion, accion.simbolo_accion)
    
    resultado = accion_dao.obtener_uno(1)
    assert resultado.id_accion == accion.id_accion
    assert resultado.nombre_accion == accion.nombre_accion
    assert resultado.simbolo_accion == accion.simbolo_accion
    
    mock_conector.traer_solo_uno.assert_called_once_with(
        "SELECT * FROM accion WHERE id_accion = %s", (1,)
    )


def test_obtener_uno_accion_no_existente(accion_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    
    with pytest.raises(Exception, match="No existe accion con dicho id"):
        accion_dao.obtener_uno(999)


def test_obtener_todos_acciones(accion_dao, mock_conector, accion):
    mock_conector.traer_todos.return_value = [
        (accion.id_accion, accion.nombre_accion, accion.simbolo_accion)
    ]
    
    resultados = accion_dao.obtener_todos()
    assert len(resultados) == 1
    assert resultados[0].id_accion == accion.id_accion
    assert resultados[0].nombre_accion == accion.nombre_accion
    assert resultados[0].simbolo_accion == accion.simbolo_accion
    
    mock_conector.traer_todos.assert_called_once_with("SELECT * FROM accion")


def test_actualizar_accion(accion_dao, accion):
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.return_value = None
    
    resultado = accion_dao.actualizar(accion, 1)
    assert resultado is True
    
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.assert_called_once_with(
        "UPDATE accion SET nombre_accion = %s, simbolo_accion = %s WHERE id_accion = %s", 
        (accion.nombre_accion, accion.simbolo_accion, 1)
    )


def test_eliminar_accion(accion_dao):
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.return_value = None
    
    resultado = accion_dao.eliminar(1)
    assert resultado is True
    
    accion_dao._AccionDAO__base_de_datos.ejecutar_consulta.assert_called_once_with(
        "DELETE FROM accion WHERE id_accion = %s", (1,)
    )