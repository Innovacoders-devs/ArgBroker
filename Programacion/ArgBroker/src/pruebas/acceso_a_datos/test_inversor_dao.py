import sys
import os
import pytest
from unittest.mock import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from dao.inversor_dao import InversorDAO
from modelo.inversor import Inversor

@pytest.fixture
def mock_conector():
    return Mock()

@pytest.fixture
def inversor_dao(mock_conector):
    return InversorDAO(mock_conector)

@pytest.fixture
def inversor():
    return Inversor(
        id_inversor=1,
        nombre="Cosme",
        apellido="Fulanito",
        cuil="20-12345678-9",
        email="cosme.fulanito@example.com",
        contrasena="clave123",
        saldo_cuenta=1000.0,
        intentos_fallidos=0
    )

def test_crear_inversor(inversor_dao, inversor, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = inversor_dao.crear(inversor)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "INSERT INTO inversor (nombre, apellido, cuil, email, contrasena, saldo_cuenta, intentos_fallidos) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
    )

def test_obtener_uno_inversor(inversor_dao, inversor, mock_conector):
    mock_conector.traer_solo_uno.return_value = (1, inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
    resultado = inversor_dao.obtener_uno(inversor.id_inversor)
    assert resultado.id_inversor == inversor.id_inversor
    mock_conector.traer_solo_uno.assert_called_once_with("SELECT * FROM inversor WHERE id_inversor = %s", (inversor.id_inversor,))

def test_obtener_todos_inversores(inversor_dao, inversor, mock_conector):
    mock_conector.traer_todos.return_value = [
        (1, inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
    ]
    resultado = inversor_dao.obtener_todos()
    assert len(resultado) == 1
    assert resultado[0].id_inversor == inversor.id_inversor
    mock_conector.traer_todos.assert_called_once_with("SELECT * FROM inversor")

def test_actualizar_inversor(inversor_dao, inversor, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = inversor_dao.actualizar(inversor, inversor.id_inversor)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "UPDATE inversor SET nombre = %s, apellido = %s, cuil = %s, email = %s, contrasena = %s, saldo_cuenta = %s, intentos_fallidos = %s WHERE id_inversor = %s",
        (inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos, inversor.id_inversor)
    )

def test_eliminar_inversor(inversor_dao, inversor, mock_conector):
    mock_conector.ejecutar_consulta.return_value = True
    resultado = inversor_dao.eliminar(inversor.id_inversor)
    assert resultado is True
    mock_conector.ejecutar_consulta.assert_called_once_with(
        "DELETE FROM inversor WHERE id_inversor = %s", (inversor.id_inversor,)
    )

def test_buscar_inversor_por_email(inversor_dao, inversor, mock_conector):
    mock_conector.traer_solo_uno.return_value = (1, inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
    resultado = inversor_dao.buscar_inversor_por_email(inversor.email)
    assert resultado is True
    mock_conector.traer_solo_uno.assert_called_once_with("SELECT * FROM inversor WHERE email = %s", (inversor.email,))

def test_obtener_inversor_por_email(inversor_dao, inversor, mock_conector):
    mock_conector.traer_solo_uno.return_value = (1, inversor.nombre, inversor.apellido, inversor.cuil, inversor.email, inversor.contrasena, inversor.saldo_cuenta, inversor.intentos_fallidos)
    resultado = inversor_dao.obtener_inversor_por_email(inversor.email)
    assert resultado.email == inversor.email
    mock_conector.traer_solo_uno.assert_called_once_with("SELECT * FROM inversor WHERE email = %s", (inversor.email,))


def test_crear_inversor_error(inversor_dao, inversor, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Database error")
    with pytest.raises(Exception):
        inversor_dao.crear(inversor)

def test_obtener_uno_inversor_no_encontrado(inversor_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    with pytest.raises(Exception, match="No existe inversor con dicho id"):
        inversor_dao.obtener_uno(99)

def test_obtener_todos_inversores_vacio(inversor_dao, mock_conector):
    mock_conector.traer_todos.return_value = []
    with pytest.raises(Exception, match="No se pudo obtener los inversores"):
        inversor_dao.obtener_todos()

def test_actualizar_inversor_error(inversor_dao, inversor, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Update error")
    with pytest.raises(Exception):
        inversor_dao.actualizar(inversor, inversor.id_inversor)

def test_eliminar_inversor_error(inversor_dao, mock_conector):
    mock_conector.ejecutar_consulta.side_effect = Exception("Delete error")
    resultado = inversor_dao.eliminar(99)
    assert resultado is False

def test_buscar_inversor_por_email_no_encontrado(inversor_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    resultado = inversor_dao.buscar_inversor_por_email("no-existe@example.com")
    assert resultado is False

def test_obtener_inversor_por_email_no_encontrado(inversor_dao, mock_conector):
    mock_conector.traer_solo_uno.return_value = None
    with pytest.raises(Exception, match="No existe inversor con dicho email"):
        inversor_dao.obtener_inversor_por_email("no-existe@example.com")