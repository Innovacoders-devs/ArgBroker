from src.herramientas.conector_a_mysql import MySQLConnector
from src.vista.menu import Menu

def main():
    COMISION_BROKER = 3.5

    HOST = "127.0.0.1"
    BASE_DATOS = "arg_broker_bdd"
    USUARIO = "root"
    CONTRASENA = "kari2024"

    conector_a_base_datos = MySQLConnector(HOST, BASE_DATOS, USUARIO , CONTRASENA)
 
    menu = Menu(conector_a_base_datos, COMISION_BROKER)

    menu.mostrar_menu_principal()


if __name__ == "__main__":
    main()
    

