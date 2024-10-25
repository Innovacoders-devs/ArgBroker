# ARGBrokers

## Descripción del Proyecto
**ARGBrokers** es una aplicación de consola diseñada para gestionar las inversiones bursátiles de sus usuarios, permitiéndoles registrar nuevas cuentas, iniciar sesión, visualizar su portafolio de activos, y realizar operaciones de compra/venta de acciones. En el proyecto aplicamos como guia las 4 reglas de diseño simple propuestas por Kent Beck (1*) y SOLID (2*). 
Además, se implementa una base de datos en MySQL para manejar las transacciones y el historial de cotizaciones, aplicando los principios del patrón de diseño DAO(3*) para separar la lógica de negocio de la de acceso a datos.



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

## Base de Datos

### Modelo Relacional
La base de datos ha sido diseñada para mantener el historial de cotizaciones y registrar todas las transacciones de compra/venta, incluyendo las comisiones de los brokers. El diseño está normalizado a la **3FN**.

### Scripts SQL
Se incluyen scripts para la creación (DDL) y manipulación (DML) de las tablas.

## Instrucciones

1. Clonar el repositorio.
2. Ejecutar el archivo `main.py` para iniciar la aplicación de consola.
3. Consultar el directorio `BaseDeDatos/` para el manejo de la base de datos.

## Autores

- **Cristian Vargas** (BaseDeDatos)
- **Laura Zarate** (Usuario)
- **Cristian Vellio** (UsuarioDAO)
- **Karina Quinteros** (Portafolio)
- **Nahir Ñañez** (PortafolioDAO)
- **Franco Miranda** (ElementoPortafolio)


(1*)las 4 reglas de diseño simple propuestas por Kent Beck:
1 - el código debe pasar todas las pruebas
2 - el código debe expresar claramente todas las ideas del programador, debe ser legible y autoexplicativo
3 - no debe haber código duplicado
4 - el código debe tener el menor número posible de elementos. 

(2*) SOLID:
S - Principio de Responsabilidad Única (SRP)
Una clase debe tener solo una razón para cambiar.
Una clase debe tener una sola responsabilidad.

O - Principio de Abierto/Cerrado (OCP)
Una entidad del software debe estar abierta para su extensión.
Una entidad del software debe estar cerrada para su modificación.

L - Principio de Sustitución de Liskov (LSP)
Las clases derivadas deben ser sustituibles por sus clases base.
No se deben poder distinguir las clases derivadas de las clases base.

I - Principio de Segregación de Interfaces (ISP)
Una clase no debe estar obligada a implementar interfaces que no utiliza.
Las interfaces deben ser específicas y clientes.

D - Principio de Inversión de Dependencias (DIP)
Las clases de alto nivel no deben depender de clases de bajo nivel.
Ambas deben depender de abstracciones.
Las abstracciones no deben depender de detalles.
Los detalles deben depender de abstracciones.

(2*) Patron de Diseño DAO

El patrón de diseño DAO consiste en una capa de abstracción que desacopla la lógica de negocio de la lógica de acceso a datos. Su objetivo es proporcionar una interfaz estándar para acceder a los datos, permitiendo cambiar la implementación de la base de datos sin afectar la lógica de negocio. El DAO se compone de una interfaz que define los métodos para acceder a los datos, una implementación específica de la base de datos y un modelo de datos que representa los datos almacenados. Esto ofrece varias ventajas, como desacoplamiento, flexibilidad y reutilización, facilitando la mantenibilidad, escalabilidad y flexibilidad en el acceso a datos en aplicaciones complejas.