import sys
import os
import pytest
from unittest.mock import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from historial_saldo_dao import HistorialSaldoDAO
from modelo.historial_saldo import HistorialSaldo

@pytest.fixture
def mock_conector():
    return Mock()

@pytest.fixture
def historial_saldo_dao(mock_conector):
    return HistorialSaldoDAO(mock_conector)

@pytest.fixture
def historial_saldo():
    return HistorialSaldo(
        id_historial_saldo=1,
        id_inversor=1,
        fecha="2024-11-03",
        saldo_anterior=1000.0,
        saldo_nuevo=1200.0,
        motivo="Depósito"
    )

def test_crear_historial_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = historial_saldo_dao.crear(historial_saldo)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        """
        INSERT INTO historial_saldo (id_inversor, fecha, saldo_anterior, saldo_nuevo, motivo)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (historial_saldo.id_inversor, historial_saldo.fecha, historial_saldo.saldo_anterior, historial_saldo.saldo_nuevo, historial_saldo.motivo)
    )

def test_obtener_uno_historial_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.traer_solo_uno.return_value = (1, historial_saldo.id_inversor, historial_saldo.fecha, historial_saldo.saldo_anterior, historial_saldo.saldo_nuevo, historial_saldo.motivo)
    resultado = historial_saldo_dao.obtener_uno(historial_saldo.id_historial_saldo)
    assert resultado.id_historial_saldo == historial_saldo.id_historial_saldo
    mock_conector.traer_solo_uno.assert_called_once_with(
        "SELECT * FROM historial_saldo WHERE id_historial_saldo = %s", (historial_saldo.id_historial_saldo,)
    )

def test_obtener_todos_historial_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.traer_todos.return_value = [
        (1, historial_saldo.id_inversor, historial_saldo.fecha, historial_saldo.saldo_anterior, historial_saldo.saldo_nuevo, historial_saldo.motivo)
    ]
    resultado = historial_saldo_dao.obtener_todos()
    assert len(resultado) == 1
    assert resultado[0].id_historial_saldo == historial_saldo.id_historial_saldo
    mock_conector.traer_todos.assert_called_once_with("SELECT * FROM historial_saldo")

def test_actualizar_historial_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = historial_saldo_dao.actualizar(historial_saldo, historial_saldo.id_historial_saldo)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        """
        UPDATE historial_saldo
        SET saldo_nuevo = %s, motivo = %s
        WHERE id_historial_saldo = %s
        """,
        (historial_saldo.saldo_nuevo, historial_saldo.motivo, historial_saldo.id_historial_saldo)
    )

def test_eliminar_historial_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = historial_saldo_dao.eliminar(historial_saldo.id_historial_saldo)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "DELETE FROM historial_saldo WHERE id_historial_saldo = %s", (historial_saldo.id_historial_saldo,)
    )

def test_buscar_ultimo_saldo(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.traer_solo_uno.return_value = (1, historial_saldo.id_inversor, historial_saldo.fecha, historial_saldo.saldo_anterior, historial_saldo.saldo_nuevo, historial_saldo.motivo)
    resultado = historial_saldo_dao.buscar_ultimo_saldo(historial_saldo.id_inversor)
    assert resultado.id_historial_saldo == historial_saldo.id_historial_saldo
    mock_conector.traer_solo_uno.assert_called_once_with(
        """
        SELECT * FROM historial_saldo WHERE id_inversor = %s
        ORDER BY fecha DESC LIMIT 1
        """,
        (historial_saldo.id_inversor,)
    )

def test_crear_historial_saldo_error(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Database error")
    with pytest.raises(Exception, match="Error al crear el historial de saldo en la base de datos: Database error"):
        historial_saldo_dao.crear(historial_saldo)

def test_obtener_uno_historial_saldo_error(historial_saldo_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    with pytest.raises(Exception, match="No existe historial de saldo con dicho id"):
        historial_saldo_dao.obtener_uno(99)

def test_obtener_todos_historial_saldo_error(historial_saldo_dao, mock_conector):
    mock_conector.traer_todos.return_value = []
    with pytest.raises(Exception, match="No se pudo obtener los historiales de saldo"):
        historial_saldo_dao.obtener_todos()

def test_actualizar_historial_saldo_error(historial_saldo_dao, historial_saldo, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Update error")
    with pytest.raises(Exception, match="Error al modificar el historial de saldo: Update error"):
        historial_saldo_dao.actualizar(historial_saldo, historial_saldo.id_historial_saldo)

def test_eliminar_historial_saldo_error(historial_saldo_dao, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Delete error")
    with pytest.raises(Exception, match="Error al eliminar el historial de saldo en la base de datos: Delete error"):
        historial_saldo_dao.eliminar(99)

def test_buscar_ultimo_saldo_error(historial_saldo_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    with pytest.raises(Exception, match="No se encontró historial de saldo para el inversor."):
        historial_saldo_dao.buscar_ultimo_saldo(99)