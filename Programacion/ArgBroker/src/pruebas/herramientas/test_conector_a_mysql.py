import sys
import os
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

from herramientas.conector_a_mysql import MySQLConnector


import mysql.connector
from mysql.connector import Error, IntegrityError

@pytest.fixture
def conector():
    return MySQLConnector(HOST="localhost", BASE_DATOS="test_db", USUARIO="root", CONTRASENA="password")

def test_mysqlconnector_conectar_y_desconectar(conector):
    with patch("mysql.connector.connect") as mock_connect:
        conector.conectar_a_base_datos()
        mock_connect.assert_called_once()
    conector.desconectar_de_base_datos()
    assert conector.conexion is None

def test_mysqlconnector_ejecutar_consulta(conector):
    with patch("mysql.connector.connect") as mock_connect:
        conector.conectar_a_base_datos()
        mock_cursor = mock_connect.return_value.cursor.return_value
        conector.ejecutar_consulta("INSERT INTO test_table (col1) VALUES (%s)", (1,))
        mock_cursor.execute.assert_called_once()
        conector.desconectar_de_base_datos()

def test_mysqlconnector_traer_todos(conector):
    with patch("mysql.connector.connect") as mock_connect:
        conector.conectar_a_base_datos()
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [(1,), (2,)]
        result = conector.traer_todos("SELECT * FROM test_table")
        assert len(result) == 2
        conector.desconectar_de_base_datos()

def test_mysqlconnector_traer_solo_uno(conector):
    with patch("mysql.connector.connect") as mock_connect:
        conector.conectar_a_base_datos()
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = (1,)
        result = conector.traer_solo_uno("SELECT * FROM test_table WHERE id=%s", (1,))
        assert result == (1,)
        conector.desconectar_de_base_datos()