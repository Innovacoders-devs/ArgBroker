import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.cotizacion_diaria import CotizacionDiaria

def test_cotizacion_diaria_initialization():
    cotizacion = CotizacionDiaria(
        id_cotizacion=1, id_accion=101, fecha="2023-10-01",
        ultimo_operado=150.0, cantidad_compra_diaria=200,
        precio_compra_actual=145.0, precio_venta_actual=155.0,
        cantidad_venta_diaria=180, valor_apertura=140.0,
        minimo_diario=138.0, maximo_diario=160.0, valor_cierre=150.0
    )
    assert cotizacion.id_cotizacion == 1
    assert cotizacion.id_accion == 101
    assert cotizacion.fecha == "2023-10-01"
    assert cotizacion.ultimo_operado == 150.0
    assert cotizacion.cantidad_compra_diaria == 200
    assert cotizacion.precio_compra_actual == 145.0
    assert cotizacion.precio_venta_actual == 155.0
    assert cotizacion.cantidad_venta_diaria == 180
    assert cotizacion.valor_apertura == 140.0
    assert cotizacion.minimo_diario == 138.0
    assert cotizacion.maximo_diario == 160.0
    assert cotizacion.valor_cierre == 150.0

def test_cotizacion_diaria_default_initialization():
    cotizacion = CotizacionDiaria()
    assert cotizacion.id_cotizacion is None
    assert cotizacion.id_accion is None
    assert cotizacion.fecha is None
    assert cotizacion.ultimo_operado is None
    assert cotizacion.cantidad_compra_diaria is None
    assert cotizacion.precio_compra_actual is None
    assert cotizacion.precio_venta_actual is None
    assert cotizacion.cantidad_venta_diaria is None
    assert cotizacion.valor_apertura is None
    assert cotizacion.minimo_diario is None
    assert cotizacion.maximo_diario is None
    assert cotizacion.valor_cierre is None

def test_cotizacion_diaria_partial_initialization():
    cotizacion = CotizacionDiaria(id_accion=101, ultimo_operado=150.0)
    assert cotizacion.id_cotizacion is None
    assert cotizacion.id_accion == 101
    assert cotizacion.ultimo_operado == 150.0

def test_cotizacion_diaria_update_properties():
    cotizacion = CotizacionDiaria()
    cotizacion.id_cotizacion = 2
    cotizacion.id_accion = 102
    cotizacion.fecha = "2023-10-10"
    cotizacion.ultimo_operado = 152.5
    cotizacion.cantidad_compra_diaria = 250
    cotizacion.precio_compra_actual = 148.0
    cotizacion.precio_venta_actual = 158.0
    cotizacion.cantidad_venta_diaria = 220
    cotizacion.valor_apertura = 145.0
    cotizacion.minimo_diario = 140.0
    cotizacion.maximo_diario = 162.0
    cotizacion.valor_cierre = 155.0

    assert cotizacion.id_cotizacion == 2
    assert cotizacion.id_accion == 102
    assert cotizacion.fecha == "2023-10-10"
    assert cotizacion.ultimo_operado == 152.5
    assert cotizacion.cantidad_compra_diaria == 250
    assert cotizacion.precio_compra_actual == 148.0
    assert cotizacion.precio_venta_actual == 158.0
    assert cotizacion.cantidad_venta_diaria == 220
    assert cotizacion.valor_apertura == 145.0
    assert cotizacion.minimo_diario == 140.0
    assert cotizacion.maximo_diario == 162.0
    assert cotizacion.valor_cierre == 155.0

def test_cotizacion_diaria_str():
    cotizacion = CotizacionDiaria(
        id_cotizacion=1, id_accion=101, fecha="2023-10-01",
        ultimo_operado=150.0, cantidad_compra_diaria=200,
        precio_compra_actual=145.0, precio_venta_actual=155.0,
        cantidad_venta_diaria=180, valor_apertura=140.0,
        minimo_diario=138.0, maximo_diario=160.0, valor_cierre=150.0
    )
    expected_str = (
        "Cotizacion Id: 1\n"
        "Accion Id: 101\n"
        "Fecha: 2023-10-01\n"
        "Ultimo operado: 150.0\n"
        "Cantidad de compra diaria: 200\n"
        "Precio de compra actual: 145.0\n"
        "Precio de venta actual: 155.0\n"
        "Cantidad de venta diaria: 180\n"
        "Valor de apertura: 140.0\n"
        "Minimo diario: 138.0\n"
        "Maximo diario: 160.0\n"
        "Valor de cierre: 150.0"
    )
    assert str(cotizacion) == expected_str

def test_cotizacion_diaria_none_properties():
    cotizacion = CotizacionDiaria(id_cotizacion=1, id_accion=None, ultimo_operado=None)
    assert cotizacion.id_cotizacion == 1
    assert cotizacion.id_accion is None
    assert cotizacion.ultimo_operado is None

def test_cotizacion_diaria_empty_string_properties():
    cotizacion = CotizacionDiaria(fecha="", ultimo_operado=0)
    assert cotizacion.fecha == ""
    assert cotizacion.ultimo_operado == 0