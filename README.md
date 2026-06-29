# Sistema de Gestión de Biblioteca Digital


### Integrantes

- Joaquin Matias Mora
- Lucia Soto
- Lautaro

---

# Descripción

Es un Sistema de Gestión de Biblioteca Digital realizado en Python utilizando Programación Orientada a Objetos.

El sistema permite administrar libros, usuarios y préstamos mediante un menú interactivo por consola. Se aplican distintos conceptos solicitados, como herencia, polimorfismo, composición, agregación, decoradores, metaclases,  entre otros.

---

# Funcionalidades

## Gestión de Libros

- Alta de libros.
- Modificación de libros.
- Eliminación de libros.
- Listado de libros registrados.
- Validación de ISBN.

## Gestión de Usuarios

- Alta de usuarios.
- Modificación de usuarios.
- Eliminación de usuarios.
- Listado de usuarios registrados.

## Gestión de Préstamos

- Registrar préstamos.
- Registrar devoluciones.
- Consultar préstamos activos.
- Un libro no puede prestarse si ya se encuentra prestado.
- Registro de fecha de préstamo y devolución.

---

# Estructura del proyecto

```
biblioteca-digital/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── biblioteca.py
│   ├── libro.py
│   ├── prestamo.py
│   └── usuario.py
│
├── utils/
│   ├── __init__.py
│   ├── decoradores.py
│   └── metaclases.py
│
├── uml/
│   └── diagrama
│
└── README.md
```

---

# Requisitos

- Python 3.10 o superior.

No es necesario instalar librerías externas, ya que únicamente se utilizan módulos incluidos en Python.

---

# Ejecución

1. Clonar el repositorio.

```bash
git clone https://github.com/lucisotoo/Sistema-de-Gestion-Biblioteca-Digital.git
```

2. Ingresar a la carpeta del proyecto.

```bash
cd biblioteca-digital
```

3. Ejecutar el programa.

```bash
python main.py
```
