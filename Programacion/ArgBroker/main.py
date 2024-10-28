from src.herramientas.conector_a_mysql import MySQLConnector
from src.vista.menu import Menu

def main():
    COMISION_BROKER = 3.5

    HOST = "autorack.proxy.rlwy.net"
    BASE_DATOS = "railway"
    USUARIO = "root"
    CONTRASENA = "UMoiNIiTxJZCkhxzKbweHsBVohDwRpEx"
    PUERTO = 42407

    conector_a_base_datos = MySQLConnector(HOST, BASE_DATOS, USUARIO , CONTRASENA, PUERTO)
 
    menu = Menu(conector_a_base_datos, COMISION_BROKER)

    menu.mostrar_menu_principal()


if __name__ == "__main__":
    main()
    

