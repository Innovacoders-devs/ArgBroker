<div align="center">
    ArgBroker
</div>

## Descripción del Proyecto
**ARGBroker** es una aplicación de consola diseñada para gestionar las inversiones bursátiles de sus usuarios, permitiéndoles registrar nuevas cuentas, iniciar sesión, visualizar su portafolio de activos, y realizar operaciones de compra/venta de acciones. En el proyecto aplicamos como guia las 4 reglas de diseño simple propuestas por Kent Beck (1*) y SOLID (2*). 
Además, se implementa una base de datos en MySQL para manejar las transacciones y el historial de cotizaciones, aplicando los principios del patrón de diseño DAO(3*) para separar la lógica de negocio de la de acceso a datos.

## 👥 Equipo de Desarrollo:

<table>
<tr>
    <td align="center">
        <a href="https://github.com/lauzarg">
            <img src="/api/placeholder/100/100" width="100px;" alt="Laura Zarate"/><br />
            <sub><b>Laura Zarate</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/CristianVellio">
            <img src="/api/placeholder/100/100" width="100px;" alt="Cristian Vellio"/><br />
            <sub><b>Cristian Vellio</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/KaryQuinteros">
            <img src="/api/placeholder/100/100" width="100px;" alt="Karina Quinteros"/><br />
            <sub><b>Karina Quinteros</b></sub>
        </a>
    </td>
</tr>
<tr>
    <td align="center">
        <a href="https://github.com/nahir1009">
            <img src="/api/placeholder/100/100" width="100px;" alt="Nahir Ñañez"/><br />
            <sub><b>Nahir Ñañez</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/MirandaFrancoCBA">
            <img src="/api/placeholder/100/100" width="100px;" alt="Franco Miranda"/><br />
            <sub><b>Franco Miranda</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Malvadapapa">
            <img src="/api/placeholder/100/100" width="100px;" alt="Cristian Vargas"/><br />
            <sub><b>Cristian Vargas</b></sub>
        </a>
    </td>
</tr>
</table>

## Funcionalidades

- **Registro de usuarios**: Permite a nuevos inversores registrarse proporcionando nombre, apellido, cuil, email y contraseña.
- **Inicio de sesión**: Valida credenciales para iniciar sesión.
- **Recuperación de contraseña y bloqueo**: Recuperación de contraseña y bloqueo al tercer intento fallido (opcional).
- **Visualización de cuenta**: Muestra el saldo, total invertido y rendimiento total.
- **Gestión de portafolio**:
  - Listar activos: Muestra nombre del activo, cantidad de acciones, precios actuales de compra/venta y rendimiento.
  - Compra/Venta de acciones: Valida existencias y registra transacciones.
  - Actualiza el saldo, total invertido y portafolio.
  



## Convenciones de Nomenclatura

El equipo ha decidido respetar el estándar **snake_case** y **PascalCase** para los nombres de archivos, clases y métodos. Más detalles se pueden encontrar en el archivo `convenciones_nomenclatura.md`.

- **Archivos y directorios**: snake_case en minúsculas.
- **Clases**: PascalCase, ej. `Usuario`, `Portafolio`.
- **Funciones y métodos**: snake_case, comenzando con un verbo en infinitivo, ej. `agregar_accion`.
- **Variables**: snake_case, ej. `nombre_usuario`.
- **Constantes**: MAYÚSCULAS, ej. `MAX_INTENTOS`.


## Estructura de carpetas del proyecto y justificacion

Base-datos/

Aqui se encuentra la documentacion de la base de datos junto una imagen del diagrama relacional, una copia de la base de datos completa con algunas entradas de prueba en formato sql, tambien hay una version modificada para ejecutarse en one compiler (que corre sin errores) tambien en formato sql y finalmente las consultas de tipo DML que se piden en la consigna.

Programacion/

Aqui se encuentra la documentacion del diagrama de clases junto con una imagen del mismo y el directorio principal de la app llamado ArgBroker:
  ```python  
  ArgBroker/
  ├── src/
      ├── acceso_a_datos/
      ├── herramientas/
      ├── modelo/
      ├── servicios/
      └── Vista/
  └── main.py
  ```

`1. acceso_a_datos/`

Esta carpeta agrupa los componentes relacionados con la interacción de la aplicación con la base de datos. Aquí estan las clases de acceso a datos (DAO), separando las consultas y transacciones con la base de datos del resto de la lógica de negocio de la aplicación, promoviendo asi la reutilización de componentes y la separación de responsabilidades.

`2. herramientas/`

Esta carpeta está reservada para utilidades o clases que proporcionan funcionalidades auxiliares, en este caso la conexion a la base de datos.

`3. modelo/`

Aquí se definen los modelos de negocio que representan las entidades del sistema. Tienen una correspondencia 1 - 1 con las entidades de la base de datos y forman la base sobre la cual se realizan las transacciones y cálculos. Este enfoque esta inspirado en el patrón "Modelo vista controlador"(4*) (aunque no lo aplica acabadamente, solo es una aproximacion), donde los modelos están separados de la lógica de la interfaz de usuario y de la lógica de acceso a datos.

`5. servicios/`

Este directorio contiene los servicios, es decir, las clases o funciones que encapsulan la lógica de negocio y operan sobre los modelos. La separación entre los servicios y los DAOs asegura que la lógica de negocio no esté acoplada directamente con el acceso a la base de datos, facilitando el testeo.

`6. Vista/`

Esta carpeta contiene la clase que aloja los distintos menus de consola de nuestra app. 

`7. main.py`
Este archivo es el punto de entrada de la aplicación. 



## Base de Datos

### Modelo Relacional
La base de datos ha sido diseñada para persistir los datos de los inversores y acciones, como asi tambien el historial de saldo del inversor, sus acciones en su portfolio, historial de cotizaciones de acciones y registrar todas las transacciones de compra/venta. El diseño está normalizado a la **3FN**.


## Instrucciones para probar el proyecto

`1.` Clonar el repositorio en una carpeta local.

`2.` Se puede probar con el motor de base de datos online que elegimos pero de no estar disponible se puede importar la version de prueba de la base de datos que esta dentro de la carpeta "`Base-datos`" llamado "`Arg-broker-bdd.sql`" y se deben modificar los siguientes datos en el archivo main hubicado dentro de `Programacion/ArgBroker/main.py`:    
  ```python  
host = "host de mi conexion creada para probar"
base_datos = "base de datos de mi conexion creada para probar"
usuario = "usuario de mi conexion creada para probar"
contrasena = "contraseña de mi conexion creada para probar"
```
`3.` Instalar las dependencias hubicadas en el archivo requirements.txt (instrucciones al final (5*))

`4.` Ejecutar el archivo `main.py` para iniciar la aplicación de consola.








### (1*) Las 4 reglas de diseño simple propuestas por Kent Beck:
1 - el código debe pasar todas las pruebas

2 - el código debe expresar claramente todas las ideas del programador, debe ser legible y autoexplicativo

3 - no debe haber código duplicado

4 - el código debe tener el menor número posible de elementos. 


### (2*) SOLID:
`S` - Principio de Responsabilidad Única (SRP)
Una clase debe tener solo una razón para cambiar.
Una clase debe tener una sola responsabilidad.

`O` - Principio de Abierto/Cerrado (OCP)
Una entidad del software debe estar abierta para su extensión.
Una entidad del software debe estar cerrada para su modificación.

`L` - Principio de Sustitución de Liskov (LSP)
Las clases derivadas deben ser sustituibles por sus clases base.
No se deben poder distinguir las clases derivadas de las clases base.

`I` - Principio de Segregación de Interfaces (ISP)
Una clase no debe estar obligada a implementar interfaces que no utiliza.
Las interfaces deben ser específicas y clientes.

`D` - Principio de Inversión de Dependencias (DIP)
Las clases de alto nivel no deben depender de clases de bajo nivel.
Ambas deben depender de abstracciones.
Las abstracciones no deben depender de detalles.
Los detalles deben depender de abstracciones.


### (3*) Patron de Diseño DAO

El patrón de diseño DAO separa la capa de abstracción de la de acceso a datos, promoviendo alta cohesión y bajo acoplamiento. Su objetivo es proporcionar una interfaz estándar para acceder a los datos, permitiendo cambiar la implementación de la base de datos sin afectar la lógica de negocio.
El DAO se compone de:

Interfaz(clase abstracta en python): define métodos para acceder a los datos

Implementación específica de la base de datos 

Modelo de datos o Daos: representa los datos almacenados


### (4*) MVC
El patrón de diseño Modelo Vista Controlador (MVC) es una estrategia de desarrollo de software que separa una aplicación en tres componentes principales:

Modelo: Representa los datos y la lógica de negocio de la aplicación. Es responsable de gestionar la información, realizar cálculos y comunicarse con la base de datos o APIs externas. No tiene conocimiento de la interfaz de usuario.

Vista: Es la interfaz de usuario que presenta los datos del modelo al usuario. La vista solo muestra la información y no contiene lógica de negocio. Su función es recibir la entrada del usuario y mostrar la salida.

Controlador: Actúa como intermediario entre el modelo y la vista. Recibe las entradas del usuario desde la vista, procesa esas entradas (a menudo llamando al modelo), y actualiza la vista en consecuencia.


### (5*) Pasos para instalar las dependencias:

#### 1. Primero se debe crear un entorno virtual:
Abrir la terminal en el directorio del proyecto.

Abre y ejecuta el siguiente comando en una consola:

`python -m venv venv`

Activar el entorno virtual en Windows:

`venv\Scripts\activate`

Se debe poder ver en consola que el nombre del entorno esta en el prompt de la terminal, dando en cuenta que está activado.

#### 2. Instalar dependencias desde requirements.txt:
Asegurarse de que el entorno virtual está activado

Ejecuta el siguiente comando en la terminal para instalar las dependencias:

`pip install -r requirements.txt`



<div align="center">

### 🌟 ¡Gracias por usar ArgBroker!

Hecho con ❤️ por InnovaCoders

</div>