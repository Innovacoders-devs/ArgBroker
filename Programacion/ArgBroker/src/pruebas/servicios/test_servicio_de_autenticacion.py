import sys
import os
import pytest
from unittest.mock import MagicMock

#Los SERVICIOS tienen el mismo error de acceso a modulos debido a los atributos privados
# que los DAOS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.inversor import Inversor
from servicios.servicio_de_autenticacion import ServicioDeAutenticacion

@pytest.fixture
def servicio_autenticacion():
    return ServicioDeAutenticacion(MagicMock())

def test_iniciar_sesion_exitoso(servicio_autenticacion):
    inversor = Inversor(id_inversor=1, email="test@ejemplo.com", contrasena="password", intentos_fallidos=0, bloqueado=False)
    mock_dao = MagicMock()
    mock_dao.buscar_inversor_por_email.return_value = True
    mock_dao.obtener_inversor_por_email.return_value = inversor
    servicio_autenticacion._ServicioDeAutenticacion__inversor_dao = mock_dao

    resultado = servicio_autenticacion.iniciar_sesion("test@ejemplo.com", "password")

    assert resultado == inversor
    assert inversor.intentos_fallidos == 0
    mock_dao.actualizar.assert_called_once_with(inversor, inversor.id_inversor)

def test_iniciar_sesion_usuario_no_registrado(servicio_autenticacion):
    mock_dao = MagicMock()
    mock_dao.buscar_inversor_por_email.return_value = False
    servicio_autenticacion._ServicioDeAutenticacion__inversor_dao = mock_dao

    with pytest.raises(ValueError, match="El usuario no se encuentra registrado en la base de datos"):
        servicio_autenticacion.iniciar_sesion("no_registrado@ejemplo.com", "password")

def test_iniciar_sesion_cuenta_bloqueada(servicio_autenticacion):
    inversor = Inversor(id_inversor=2, email="bloqueado@ejemplo.com", contrasena="password", intentos_fallidos=0, bloqueado=True)
    mock_dao = MagicMock()
    mock_dao.buscar_inversor_por_email.return_value = True
    mock_dao.obtener_inversor_por_email.return_value = inversor
    servicio_autenticacion._ServicioDeAutenticacion__inversor_dao = mock_dao

    with pytest.raises(ValueError, match="Cuenta bloqueada. Por favor contacte al administrador"):
        servicio_autenticacion.iniciar_sesion("bloqueado@ejemplo.com", "password")

def test_iniciar_sesion_contrasena_incorrecta(servicio_autenticacion):
    inversor = Inversor(id_inversor=3, email="incorrecto@ejemplo.com", contrasena="password", intentos_fallidos=0, bloqueado=False)
    mock_dao = MagicMock()
    mock_dao.buscar_inversor_por_email.return_value = True
    mock_dao.obtener_inversor_por_email.return_value = inversor
    servicio_autenticacion._ServicioDeAutenticacion__inversor_dao = mock_dao

    with pytest.raises(ValueError, match="Contraseña incorrecta. Intentos restantes: 2"):
        servicio_autenticacion.iniciar_sesion("incorrecto@ejemplo.com", "wrong_password")

    assert inversor.intentos_fallidos == 1
    mock_dao.actualizar.assert_called_once_with(inversor, inversor.id_inversor)

def test_iniciar_sesion_cuenta_bloqueada_despues_de_tres_intentos_fallidos(servicio_autenticacion):
    inversor = Inversor(id_inversor=4, email="tres_fallidos@ejemplo.com", contrasena="password", intentos_fallidos=2, bloqueado=False)
    mock_dao = MagicMock()
    mock_dao.buscar_inversor_por_email.return_value = True
    mock_dao.obtener_inversor_por_email.return_value = inversor
    servicio_autenticacion._ServicioDeAutenticacion__inversor_dao = mock_dao

    with pytest.raises(ValueError, match="Cuenta bloqueada. Por favor contacte al administrador"):
        servicio_autenticacion.iniciar_sesion("tres_fallidos@ejemplo.com", "wrong_password")

    assert inversor.intentos_fallidos == 3
    assert inversor.bloqueado is True
    mock_dao.actualizar.assert_called_with(inversor, inversor.id_inversor)