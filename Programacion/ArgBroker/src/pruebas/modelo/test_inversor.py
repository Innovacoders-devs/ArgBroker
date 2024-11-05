import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.inversor import Inversor

def test_inversor_creacion():
    inversor = Inversor(
        id_inversor=1,
        nombre="Juan",
        apellido="Pérez",
        cuil=20304050607,
        email="juan.perez@ejemplo.com",
        contrasena="pass123"
    )
    assert inversor.id_inversor == 1
    assert inversor.nombre == "Juan"
    assert inversor.apellido == "Pérez"
    assert inversor.cuil == 20304050607
    assert inversor.email == "juan.perez@ejemplo.com"
    assert inversor.saldo_cuenta == 1000000.0
    assert inversor.intentos_fallidos == 0
    assert inversor.bloqueado is False

def test_inversor_str():
    inversor = Inversor(
        id_inversor=2,
        nombre="Maria",
        apellido="Lopez",
        cuil=20304050608,
        email="maria.lopez@ejemplo.com",
        contrasena="pass456",
        saldo_cuenta=300000.0,
        intentos_fallidos=1
    )
    expected_str = ("Inversor:2 Lopez, Maria; Cuil: 20304050608,Email: maria.lopez@ejemplo.com, "
                    "El saldo en cuenta es: 300000.0, contrasena: pass456, intentos fallidos de ingreso: 1")
    assert str(inversor).strip() == expected_str.strip()

def test_inversor_id_invalido():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El ID del inversor debe ser un número entero.'):
        inversor.id_inversor = "no_entero"

def test_inversor_nombre_invalido():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El nombre debe ser una cadena de texto.'):
        inversor.nombre = 123

def test_inversor_apellido_invalido():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El apellido debe ser una cadena de texto.'):
        inversor.apellido = 456

def test_inversor_cuil_invalido():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El CUIL está conformado por números'):
        inversor.cuil = "20304050607"
    
    with pytest.raises(ValueError, match='El CUIL debe contener 11 caracteres'):
        inversor.cuil = 2030405060  # Solo 10 caracteres

def test_inversor_email_valido():
    inversor = Inversor()
    inversor.email = "prueba@ejemplo.com"
    assert inversor.email == "prueba@ejemplo.com"

def test_inversor_email__invalido_sin_arroba():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El correo electrónico debe tener un @'):
        inversor.email = "pruebaejemplo.com"  # Falta el '@'

def test_inversor_formato_email_invalido():
    inversor = Inversor()
    with pytest.raises(ValueError, match='El correo electrónico es inválido'):
        inversor.email = "prueba@ejemplo"  # Dominio inválido

def test_inversor_set_contrasena():
    inversor = Inversor()
    inversor.contrasena = "nueva_contrasena"
    assert inversor.contrasena == "nueva_contrasena"

def test_inversor_set_saldo_cuenta():
    inversor = Inversor()
    inversor.saldo_cuenta = 500000.0
    assert inversor.saldo_cuenta == 500000.0

def test_inversor_set_intentos_fallidos():
    inversor = Inversor()
    inversor.intentos_fallidos = 3
    assert inversor.intentos_fallidos == 3

def test_inversor_bloqueado():
    inversor = Inversor()
    inversor.bloqueado = True
    assert inversor.bloqueado is True
    inversor.bloqueado = False
    assert inversor.bloqueado is False