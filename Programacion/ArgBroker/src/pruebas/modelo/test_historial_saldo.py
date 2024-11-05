import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from modelo.historial_saldo import HistorialSaldo

def test_historial_saldo_initialization():
    historial = HistorialSaldo(
        id_historial_saldo=1, id_inversor=101, fecha="2024-11-01",
        saldo_anterior=1000.0, saldo_nuevo=1200.0, motivo="Depósito"
    )
    assert historial.id_historial_saldo == 1
    assert historial.id_inversor == 101
    assert historial.fecha == "2024-11-01"
    assert historial.saldo_anterior == 1000.0
    assert historial.saldo_nuevo == 1200.0
    assert historial.motivo == "Depósito"

def test_historial_saldo_default_initialization():
    historial = HistorialSaldo()
    assert historial.id_historial_saldo is None
    assert historial.id_inversor is None
    assert historial.fecha is None
    assert historial.saldo_anterior is None
    assert historial.saldo_nuevo is None
    assert historial.motivo is None

def test_historial_saldo_partial_initialization():
    historial = HistorialSaldo(id_inversor=102, saldo_anterior=500.0)
    assert historial.id_historial_saldo is None
    assert historial.id_inversor == 102
    assert historial.saldo_anterior == 500.0
    assert historial.saldo_nuevo is None

def test_historial_saldo_update_properties():
    historial = HistorialSaldo()
    historial.id_historial_saldo = 2
    historial.id_inversor = 103
    historial.fecha = "2024-12-01"
    historial.saldo_anterior = 1500.0
    historial.saldo_nuevo = 1700.0
    historial.motivo = "Interés"

    assert historial.id_historial_saldo == 2
    assert historial.id_inversor == 103
    assert historial.fecha == "2024-12-01"
    assert historial.saldo_anterior == 1500.0
    assert historial.saldo_nuevo == 1700.0
    assert historial.motivo == "Interés"

def test_historial_saldo_str():
    historial = HistorialSaldo(
        id_historial_saldo=3, id_inversor=104, fecha="2024-10-15",
        saldo_anterior=2000.0, saldo_nuevo=2200.0, motivo="Dividendos"
    )
    expected_str = ("HistorialSaldo id_historial_saldo = 3, id_inversor = 104, "
                    "fecha = 2024-10-15, saldo_anterior = 2000.0, saldo_nuevo = 2200.0, "
                    "motivo = Dividendos")
    assert str(historial) == expected_str

def test_historial_saldo_none_properties():
    historial = HistorialSaldo(id_historial_saldo=4, saldo_nuevo=None, motivo=None)
    assert historial.id_historial_saldo == 4
    assert historial.saldo_nuevo is None
    assert historial.motivo is None

def test_historial_saldo_empty_string_properties():
    historial = HistorialSaldo(fecha="", motivo="")
    assert historial.fecha == ""
    assert historial.motivo == ""