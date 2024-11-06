from src.herramientas.conector_a_mysql import MySQLConnector

from dotenv import load_dotenv
import os

load_dotenv()

def main():
    COMISION_BROKER = float(os.getenv("COMISION_BROKER"))

    HOST = os.getenv("HOST")
    BASE_DATOS = os.getenv("BASE_DATOS")
    USUARIO = os.getenv("USUARIO")
    CONTRASENA = os.getenv("CONTRASENA")
    PUERTO = int(os.getenv("PUERTO"))

    conector_a_base_datos = MySQLConnector(HOST, BASE_DATOS, USUARIO, CONTRASENA, PUERTO)

    menu = Menu(conector_a_base_datos, COMISION_BROKER)

    menu.mostrar_menu_principal()

if __name__ == "__main__":
    main()
