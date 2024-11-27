# Base de Datos Documental

## Autor
### Hola, soy Aldana y este es mi tp final para la clase Desarrollo de Sistemas Orientado a Objetos

### Este proyecto es un sistema de gestión documental que permite organizar, buscar, eliminar y listar documentos dentro de colecciones. El programa está desarrollado en Python y utiliza un diseño orientado a objetos.


### Características
- Gestión de colecciones de documentos.
- Importación de documentos desde archivos CSV.
- Funcionalidades de búsqueda, eliminación y listado de documentos.
- Estructura modular que facilita la escalabilidad y mantenimiento.

### Estructura del proyecto
.
├── main.py              # Punto de entrada principal del programa
├── utils/               # Módulos auxiliares
│   ├── coleccion.py     # Clase Coleccion para manejar documentos
│   ├── database.py      # Clase BBDD_Documental para gestionar colecciones
│   ├── documento.py     # Modelo Documento (representación de un documento)
│   ├── str2doc.py       # Herramienta para convertir lineas en documentos
├── files/               # Carpeta opcional para almacenar archivos CSV de entrada
└── README.md            # Comentarios del proyecto


### Uso
_El programa presenta un menú interactivo con las siguientes opciones:_

- Crear colección: Crea una nueva colección con un nombre específico.
- Importar CSV a colección: Importa documentos desde un archivo CSV a una colección.
- Consultar documento en colección: Busca un documento por su ID dentro de una colección.
- Eliminar documento de colección: Elimina un documento específico de una colección.
- Listar todos los documentos en colección: Muestra todos los documentos de una colección.
- Salir: Cierra el programa.

### Mejoras Futuras
- Realizar test 
- Sumar excepciones

