import sys
import os
import pytest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from src.modelo.transaccion import Transaccion
from src.dao.transaccion_dao import TransaccionDAO

@pytest.fixture
def mock_conector():
    return MagicMock()

@pytest.fixture
def transaccion_dao(mock_conector):
    return TransaccionDAO(mock_conector)

@pytest.fixture
def transaccion():
    return Transaccion(
        id_transaccion=1,
        id_portafolio=2,
        id_accion=3,
        cantidad=10,
        precio=150.0,
        tipo="compra",
        fecha="2024-11-01",
        comision=5.0
    )

def test_crear_transaccion_exitoso(transaccion_dao, transaccion):
    transaccion_dao._base_de_datos.ejecutar_consulta.return_value = True
    resultado = transaccion_dao.crear(transaccion)
    transaccion_dao._base_de_datos.ejecutar_consulta.assert_called_once()
    assert resultado is True

def test_crear_transaccion_falla(transaccion_dao, transaccion):
    transaccion_dao._base_de_datos.ejecutar_consulta.side_effect = Exception("Error al crear")
    with pytest.raises(Exception, match="Error al crear la transaccion en la base de datos"):
        transaccion_dao.crear(transaccion)

def test_obtener_todos_exitoso(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = [
        (1, 2, 3, 10, 150.0, "compra", "2024-11-01", 5.0)
    ]
    transacciones = transaccion_dao.obtener_todos()
    assert len(transacciones) == 1
    assert transacciones[0].id_transaccion == 1

def test_obtener_todos_vacio(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = []
    with pytest.raises(Exception, match="No se pudo obtener las transacciones"):
        transaccion_dao.obtener_todos()

def test_actualizar_transaccion_exitoso(transaccion_dao, transaccion):
    transaccion_dao._base_de_datos.ejecutar_consulta.return_value = True
    resultado = transaccion_dao.actualizar(transaccion, transaccion.id_transaccion)
    transaccion_dao._base_de_datos.ejecutar_consulta.assert_called_once()
    assert resultado is True

def test_actualizar_transaccion_falla(transaccion_dao, transaccion):
    transaccion_dao._base_de_datos.ejecutar_consulta.side_effect = Exception("Error al actualizar")
    with pytest.raises(Exception, match="Error al actualizar la transaccion en la base de datos"):
        transaccion_dao.actualizar(transaccion, transaccion.id_transaccion)

def test_eliminar_transaccion_exitoso(transaccion_dao):
    transaccion_dao._base_de_datos.ejecutar_consulta.return_value = True
    resultado = transaccion_dao.eliminar(1)
    transaccion_dao._base_de_datos.ejecutar_consulta.assert_called_once()
    assert resultado is True

def test_eliminar_transaccion_falla(transaccion_dao):
    transaccion_dao._base_de_datos.ejecutar_consulta.side_effect = Exception("Error al eliminar")
    with pytest.raises(Exception, match="Error al eliminar la transaccion de la base de datos"):
        transaccion_dao.eliminar(1)

def test_obtener_uno_exitoso(transaccion_dao):
    transaccion_dao._base_de_datos.traer_solo_uno.return_value = (1, 2, 3, 10, 150.0, "compra", "2024-11-01", 5.0)
    transaccion = transaccion_dao.obtener_uno(1)
    assert transaccion.id_transaccion == 1

def test_obtener_uno_no_existe(transaccion_dao):
    transaccion_dao._base_de_datos.traer_solo_uno.return_value = None
    with pytest.raises(Exception, match="No existe transaccion con dicho id"):
        transaccion_dao.obtener_uno(999)

def test_obtener_por_portafolio_y_accion_exitoso(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = [
        (1, 2, 3, 10, 150.0, "compra", "2024-11-01", 5.0)
    ]
    transacciones = transaccion_dao.obtener_por_portafolio_y_accion(2, 3)
    assert len(transacciones) == 1
    assert transacciones[0].id_portafolio == 2

def test_obtener_por_portafolio_y_accion_no_existe(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = []
    transacciones = transaccion_dao.obtener_por_portafolio_y_accion(999, 999)
    assert len(transacciones) == 0

def test_obtener_por_portafolio_exitoso(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = [
        (1, 2, 3, 10, 150.0, "compra", "2024-11-01", 5.0)
    ]
    transacciones = transaccion_dao.obtener_por_portafolio(2)
    assert len(transacciones) == 1
    assert transacciones[0].id_portafolio == 2

def test_obtener_por_portafolio_no_existe(transaccion_dao):
    transaccion_dao._base_de_datos.traer_todos.return_value = []
    transacciones = transaccion_dao.obtener_por_portafolio(999)
    assert len(transacciones) == 0