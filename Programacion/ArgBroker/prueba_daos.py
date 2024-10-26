from src.herramientas.conector_a_mysql import MySQLConnector
from src.acceso_a_datos.accion_dao import AccionDAO
from src.modelo.cotizacion_diaria import CotizacionDiaria
from src.modelo.accion import Accion
from src.acceso_a_datos.cotizacion_diaria_dao import CotizacionDAO
from src.modelo.inversor import Inversor
from src.acceso_a_datos.inversor_dao import InversorDAO


def main():
    host = "127.0.0.1"
    base_datos = "arg_broker_bdd"
    usuario = "root"
    contrasena = "redcros62"


    connector = MySQLConnector(host, base_datos, usuario, contrasena)
 
    try:

        accion_dao = AccionDAO(connector)

        resultado = accion_dao.obtener_todos()
        for i in resultado:
            print(i)

    except Exception as e:  
        print(f"Error: {e}")  

if __name__ == "__main__":

    main()
    


    """



    host = "junction.proxy.rlwy.net"
    database = "railway"
    user = "root"
    password = "GhsHCPaNwJHOlpNepUsFVXoAyVZfDnGI"
    port = 47364


  datos_cotizacion = CotizacionDiaria(
    id_accion=2,
    fecha='2024-10-20',
    ultimo_operado=1,
    cantidad_compra_diaria=1.00,
    precio_compra_actual=1.00,
    precio_venta_actual=1,
    cantidad_venta_diaria=1.00,
    valor_apertura=11.00,
    minimo_diario=11.00,
    maximo_diario=1.00,
    valor_cierre=1.00
)
    try:
        cargar_cotizacion = CotizacionDAO(connector)
        cotizacionmodificada = cargar_cotizacion.crear(datos_cotizacion)
        if cotizacionmodificada:
            print('Se creo')


         for e in cotizacion:
            print("\n")
            print(e)
    
    """

