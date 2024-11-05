import sys
import os
import pytest
from unittest.mock import MagicMock, create_autospec
from acceso_a_datos.cotizacion_dao import CotizacionDAO
from modelo.cotizacion_diaria import CotizacionDiaria

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))


@pytest.fixture
def mock_conector():
    return MagicMock()

@pytest.fixture
def cotizacion_dao(mock_conector):
    return CotizacionDAO(mock_conector)

@pytest.fixture
def cotizacion_diaria():
    return CotizacionDiaria(
        id_cotizacion=1,
        id_accion=100,
        fecha="2024-11-01",
        ultimo_operado=150.0,
        cantidad_compra_diaria=500,
        precio_compra_actual=155.0,
        precio_venta_actual=160.0,
        cantidad_venta_diaria=450,
        valor_apertura=150.0,
        minimo_diario=145.0,
        maximo_diario=165.0,
        valor_cierre=155.0
    )

def test_crear(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.conectar_a_base_datos = MagicMock()
    mock_conector.ejecutar_consulta = MagicMock()
    mock_conector.desconectar_de_base_datos = MagicMock()

    resultado = cotizacion_dao.crear(cotizacion_diaria)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.ejecutar_consulta.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado is True

def test_obtener_uno(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.traer_solo_uno.return_value = (
        cotizacion_diaria.id_cotizacion,
        cotizacion_diaria.id_accion,
        cotizacion_diaria.fecha,
        cotizacion_diaria.ultimo_operado,
        cotizacion_diaria.cantidad_compra_diaria,
        cotizacion_diaria.precio_compra_actual,
        cotizacion_diaria.precio_venta_actual,
        cotizacion_diaria.cantidad_venta_diaria,
        cotizacion_diaria.valor_apertura,
        cotizacion_diaria.minimo_diario,
        cotizacion_diaria.maximo_diario,
        cotizacion_diaria.valor_cierre,
    )

    resultado = cotizacion_dao.obtener_uno(1)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_solo_uno.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado.id_cotizacion == cotizacion_diaria.id_cotizacion

def test_obtener_todos(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.traer_todos.return_value = [
        (
            cotizacion_diaria.id_cotizacion,
            cotizacion_diaria.id_accion,
            cotizacion_diaria.fecha,
            cotizacion_diaria.ultimo_operado,
            cotizacion_diaria.cantidad_compra_diaria,
            cotizacion_diaria.precio_compra_actual,
            cotizacion_diaria.precio_venta_actual,
            cotizacion_diaria.cantidad_venta_diaria,
            cotizacion_diaria.valor_apertura,
            cotizacion_diaria.minimo_diario,
            cotizacion_diaria.maximo_diario,
            cotizacion_diaria.valor_cierre,
        )
    ]

    resultado = cotizacion_dao.obtener_todos(100)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_todos.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert len(resultado) == 1
    assert resultado[0].id_accion == cotizacion_diaria.id_accion

def test_actualizar(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.ejecutar_consulta = MagicMock()
    resultado = cotizacion_dao.actualizar(cotizacion_diaria, cotizacion_diaria.id_cotizacion)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.ejecutar_consulta.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado is True

def test_eliminar(cotizacion_dao, mock_conector):
    mock_conector.ejecutar_consulta = MagicMock()
    resultado = cotizacion_dao.eliminar(1)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.ejecutar_consulta.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado is True

def test_obtener_ultima_cotizacion(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.traer_solo_uno.return_value = (
        cotizacion_diaria.id_cotizacion,
        cotizacion_diaria.id_accion,
        cotizacion_diaria.fecha,
        cotizacion_diaria.ultimo_operado,
        cotizacion_diaria.cantidad_compra_diaria,
        cotizacion_diaria.precio_compra_actual,
        cotizacion_diaria.precio_venta_actual,
        cotizacion_diaria.cantidad_venta_diaria,
        cotizacion_diaria.valor_apertura,
        cotizacion_diaria.minimo_diario,
        cotizacion_diaria.maximo_diario,
        cotizacion_diaria.valor_cierre,
    )

    resultado = cotizacion_dao.obtener_ultima_cotizacion(100)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_solo_uno.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado.id_cotizacion == cotizacion_diaria.id_cotizacion

def test_obtener_por_accion(cotizacion_dao, mock_conector, cotizacion_diaria):
    mock_conector.traer_solo_uno.return_value = (
        cotizacion_diaria.id_cotizacion,
        cotizacion_diaria.id_accion,
        cotizacion_diaria.fecha,
        cotizacion_diaria.ultimo_operado,
        cotizacion_diaria.cantidad_compra_diaria,
        cotizacion_diaria.precio_compra_actual,
        cotizacion_diaria.precio_venta_actual,
        cotizacion_diaria.cantidad_venta_diaria,
        cotizacion_diaria.valor_apertura,
        cotizacion_diaria.minimo_diario,
        cotizacion_diaria.maximo_diario,
        cotizacion_diaria.valor_cierre,
    )

    resultado = cotizacion_dao.obtener_por_accion(100)

    mock_conector.conectar_a_base_datos.assert_called_once()
    mock_conector.traer_solo_uno.assert_called_once()
    mock_conector.desconectar_de_base_datos.assert_called_once()
    assert resultado.id_accion == cotizacion_diaria.id_accion