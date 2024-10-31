import pytest
from unittest.mock import MagicMock, Mock, patch
from src.inversor import Inversor
from src.portafolio import Portafolio
from src.servicios.servicio_de_registro import ServicioDeRegistro

#Test Login

@pytest.fixture
def inversor_prueba():
    return Inversor(
        id_inversor=1,
        email="inversor@test.com",
        nombre="Inversor Prueba",
        apellido="Apellido"
    )
# Configurar los mocks de DAOS Sims
@pytest.fixture
def inversor_dao_mock():
    return Mock()

@pytest.fixture
def portafolio_dao_mock():
    return Mock()

# instanciando serv
@pytest.fixture
def servicio_registro(inversor_dao_mock, portafolio_dao_mock):
    return ServicioDeRegistro(inversor_dao_mock, portafolio_dao_mock)

# test exito registro
def test_registrar_usuario_exitoso(servicio_registro, inversor_dao_mock, portafolio_dao_mock, inversor_prueba):
    # Configurar el mock para simular que el inversor no existe
    inversor_dao_mock.buscar_inversor_por_email.return_value = None
    inversor_dao_mock.obtener_inversor_por_email.return_value = inversor_prueba

    resultado = servicio_registro.registrar_usuario(inversor_prueba)

    inversor_dao_mock.crear.assert_called_once_with(inversor_prueba)
    inversor_dao_mock.obtener_inversor_por_email.assert_called_once_with(inversor_prueba.email)
    portafolio_dao_mock.crear.assert_called_once_with(Portafolio(id_inversor=inversor_prueba.id_inversor))
    assert resultado is True

# Test email repetido
def test_registrar_usuario_email_existente(servicio_registro, inversor_dao_mock, inversor_prueba):
    # Simular que el inversor ya existe
    inversor_dao_mock.buscar_inversor_por_email.return_value = inversor_prueba

    with pytest.raises(ValueError, match="El email ya está registrado en la base de datos"):
        servicio_registro.registrar_usuario(inversor_prueba)

    inversor_dao_mock.crear.assert_not_called()
    inversor_dao_mock.obtener_inversor_por_email.assert_not_called()

# Test Error Registro
def test_registrar_usuario_error(servicio_registro, inversor_dao_mock, portafolio_dao_mock, inversor_prueba):
    inversor_dao_mock.buscar_inversor_por_email.return_value = None
    inversor_dao_mock.crear.side_effect = Exception("Error al crear inversor")

    with pytest.raises(Exception, match="Ocurrio un error al registrar el usuario: Error al crear inversor"):
        servicio_registro.registrar_usuario(inversor_prueba)

    portafolio_dao_mock.crear.assert_not_called()