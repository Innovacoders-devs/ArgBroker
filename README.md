# ARGBrokers

## Descripción del Proyecto
**ARGBrokers** es una aplicación de consola diseñada para gestionar las inversiones bursátiles de los usuarios, permitiéndoles registrar nuevas cuentas, iniciar sesión, visualizar su portafolio de activos, y realizar operaciones de compra/venta de acciones. El proyecto sigue un enfoque basado en TDD (Test Driven Development) y respeta las 4 reglas de diseño simple propuestas por Kent Beck. Además, se implementa una base de datos para manejar las transacciones y el historial de cotizaciones, respetando el patrón DAO para separar la lógica de acceso a datos.

## Funcionalidades

- **Registro de usuarios**: Permite a nuevos inversores registrarse proporcionando nombre, apellido, cuil, email y contraseña.
- **Inicio de sesión**: Valida credenciales para iniciar sesión.
- **Recuperación de contraseña y bloqueo**: Recuperación de contraseña y bloqueo al tercer intento fallido (opcional).
- **Visualización de cuenta**: Muestra el saldo, total invertido y rendimiento total.
- **Gestión de portafolio**:
  - Listar activos: Muestra nombre del activo, cantidad de acciones, precios actuales de compra/venta y rendimiento.
  - Compra/Venta de acciones: Valida existencias y registra transacciones.
  - Actualiza el saldo, total invertido y portafolio.
  
## Requisitos del Proyecto

### Clases

1. **BaseDeDatos**: Gestiona la conexión con la base de datos.
   
2. **Usuario**:
   - Representa a un usuario registrado.
   - Atributos: `nombre`, `apellido`, `cuil`, `email`, `password`, `portafolio`.
   - Métodos: Registro, inicio de sesión, getters y setters.
   
3. **UsuarioDAO**:
   - Gestiona operaciones CRUD para los usuarios en la base de datos.
   - Métodos: `agregar_usuario`, `obtener_usuario_por_email`, `modificar_usuario`, `eliminar_usuario`.
   
4. **Portafolio**:
   - Representa el portafolio de acciones del usuario.
   - Atributos: `acciones`.
   - Métodos: `agregar_accion`, `remover_accion`, `valor_total`.
   
5. **PortafolioDAO**:
   - Persistencia del portafolio en la base de datos.
   - Métodos: `agregar_accion`, `obtener_portafolio`, `remover_accion`.
   
6. **ElementoPortafolio**:
   - Representa un activo individual en el portafolio.
   - Atributos: `nombre_accion`, `cantidad`, `precio_compra`.
   
### Principios de Diseño Aplicados

- **Abstracción**: Las clases abstraen los comportamientos clave de los inversores y sus portafolios.
- **Encapsulamiento**: Los atributos de las clases están encapsulados, accediendo mediante getters y setters.
- **Modularidad**: Cada componente tiene una responsabilidad clara (e.g., DAO maneja persistencia, clases de negocio manejan lógica de negocio).
- **Bajo Acoplamiento, Alta Cohesión**: Las clases interactúan lo necesario y están cohesionadas en sus responsabilidades.
- **Transparencia Referencial**: Las funciones no modifican los argumentos originales y no tienen efectos secundarios.


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


