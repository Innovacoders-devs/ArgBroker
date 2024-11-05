import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.portafolio import Portafolio
from acceso_a_datos.portafolio_dao import PortafolioDAO


@pytest.fixture
def mock_conector():
    return MagicMock()

@pytest.fixture
def portafolio_dao(mock_conector):
    return PortafolioDAO(mock_conector)

@pytest.fixture
def sample_portafolio():
    return Portafolio(id_portafolio=1, id_inversor=123)

def test_crear_portafolio(portafolio_dao, mock_conector, sample_portafolio):
    with patch.object(mock_conector, "ejecutar_consulta") as mock_ejecutar:
        assert portafolio_dao.crear(sample_portafolio)
        mock_conector.conectar_a_base_datos.assert_called_once()
        mock_ejecutar.assert_called_once_with(
            "INSERT INTO portafolio (id_inversor) VALUES (%s)", (sample_portafolio.id_inversor,)
        )
        mock_conector.desconectar_de_base_datos.assert_called_once()

def test_actualizar_portafolio(portafolio_dao, mock_conector, sample_portafolio):
    with patch.object(mock_conector, "ejecutar_consulta") as mock_ejecutar:
        assert portafolio_dao.actualizar(sample_portafolio)
        mock_conector.conectar_a_base_datos.assert_called_once()
        mock_ejecutar.assert_called_once_with(
            "UPDATE portafolio SET id_inversor = %s WHERE id_portafolio = %s",
            (sample_portafolio.id_inversor, sample_portafolio.id_portafolio)
        )
        mock_conector.desconectar_de_base_datos.assert_called_once()

def test_eliminar_portafolio(portafolio_dao, mock_conector):
    with patch.object(mock_conector, "ejecutar_consulta") as mock_ejecutar:
        assert portafolio_dao.eliminar(1)
        mock_conector.conectar_a_base_datos.assert_called_once()
        mock_ejecutar.assert_called_once_with("DELETE FROM portafolio WHERE id_portafolio = %s", (1,))
        mock_conector.desconectar_de_base_datos.assert_called_once()

def test_obtener_todos(portafolio_dao, mock_conector):
    mock_conector.traer_todos.return_value = [(1, 123), (2, 456)]
    resultado = portafolio_dao.obtener_todos()
    
    assert len(resultado) == 2
    assert resultado[0].id_portafolio == 1
    assert resultado[0].id_inversor == 123
    assert resultado[1].id_portafolio == 2
    assert resultado[1].id_inversor == 456
    
    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_todos.assert_called_once_with("SELECT id_portafolio, id_inversor FROM portafolio")
    mock_conector.desconectar_de_base_datos.assert_called_once()

def test_obtener_uno(portafolio_dao, mock_conector, sample_portafolio):
    mock_conector.traer_solo_uno.return_value = (1, 123)
    resultado = portafolio_dao.obtener_uno(123)
    
    assert resultado.id_portafolio == 1
    assert resultado.id_inversor == 123
    
    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_solo_uno.assert_called_once_with("SELECT id_portafolio, id_inversor FROM portafolio WHERE id_inversor = %s", (123,))
    mock_conector.desconectar_de_base_datos.assert_called_once()