from utils.decoradores import log_operacion, validar_isbn
from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo


class Biblioteca:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, nombre="Biblioteca Digital"):
        if not hasattr(self, "inicializado"):
            self.nombre = nombre
            self.libros = []
            self.usuarios = []
            self.prestamos = []
            self.inicializado = True

    # ─── LIBROS ───

    @log_operacion
    @validar_isbn
    def alta_libro(self, titulo, autor, isbn, anio, paginas):
        if self.buscar_libro(isbn):
            print(f"  Error: Ya existe un libro con ISBN {isbn}")
            return None

        libro = Libro(titulo, autor, isbn, anio, paginas)
        self.libros.append(libro)

        print(f"  Libro '{titulo}' agregado correctamente.")
        return libro

    @log_operacion
    def baja_libro(self, isbn):
        libro = self.buscar_libro(isbn)

        if not libro:
            print(f"  Error: No se encontro libro con ISBN {isbn}")
            return False

        if not libro.disponible:
            print("  Error: No se puede eliminar un libro que esta prestado.")
            return False

        self.libros.remove(libro)

        print(f"  Libro '{libro.titulo}' eliminado correctamente.")
        return True

    @log_operacion
    def modificar_libro(self, isbn, titulo=None, autor=None, anio=None, paginas=None):
        libro = self.buscar_libro(isbn)

        if not libro:
            print(f"  Error: No se encontro libro con ISBN {isbn}")
            return False

        if titulo:
            libro.titulo = titulo

        if autor:
            libro.autor = autor

        if anio:
            libro.anio = anio

        if paginas:
            libro.paginas = paginas

        print(f"  Libro '{libro.titulo}' modificado correctamente.")
        return True

    def listar_libros(self):
        if not self.libros:
            print("  No hay libros registrados.")
            return

        print("\n  ─── LIBROS ───")

        for libro in self.libros:
            print(f"  {libro}")

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    # ─── USUARIOS ───

    @log_operacion
    def alta_usuario(self, nombre, apellido, dni, email):
        if self.buscar_usuario(dni):
            print(f"  Error: Ya existe un usuario con DNI {dni}")
            return None

        usuario = Usuario(nombre, apellido, dni, email)
        self.usuarios.append(usuario)

        print(f"  Usuario '{nombre} {apellido}' agregado correctamente.")
        return usuario

    @log_operacion
    def baja_usuario(self, dni):
        usuario = self.buscar_usuario(dni)

        if not usuario:
            print(f"  Error: No se encontro usuario con DNI {dni}")
            return False

        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.activo:
                print("  Error: El usuario tiene prestamos activos.")
                return False

        self.usuarios.remove(usuario)

        print(f"  Usuario '{usuario.nombre} {usuario.apellido}' eliminado correctamente.")
        return True

    @log_operacion
    def modificar_usuario(self, dni, nombre=None, apellido=None, email=None):
        usuario = self.buscar_usuario(dni)

        if not usuario:
            print(f"  Error: No se encontro usuario con DNI {dni}")
            return False

        if nombre:
            usuario.nombre = nombre

        if apellido:
            usuario.apellido = apellido

        if email:
            usuario.email = email

        print(f"  Usuario '{usuario.nombre} {usuario.apellido}' modificado correctamente.")
        return True

    def listar_usuarios(self):
        if not self.usuarios:
            print("  No hay usuarios registrados.")
            return

        print("\n  ─── USUARIOS ───")

        for usuario in self.usuarios:
            print(f"  {usuario}")

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    # ─── PRESTAMOS ───

    @log_operacion
    def registrar_prestamo(self, isbn, dni):
        libro = self.buscar_libro(isbn)

        if not libro:
            print(f"  Error: No se encontro libro con ISBN {isbn}")
            return None

        if not libro.disponible:
            print(f"  Error: El libro '{libro.titulo}' ya esta prestado.")
            return None

        usuario = self.buscar_usuario(dni)

        if not usuario:
            print(f"  Error: No se encontro usuario con DNI {dni}")
            return None

        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)

        print(f"  Prestamo registrado. ID: {prestamo.id_prestamo}")
        return prestamo

    @log_operacion
    def registrar_devolucion(self, id_prestamo):
        for prestamo in self.prestamos:
            if prestamo.id_prestamo == id_prestamo and prestamo.activo:
                prestamo.devolver()

                print(
                    f"  Devolucion registrada. Duracion: {prestamo.fechas.duracion_dias()} dias."
                )

                return True

        print(f"  Error: No se encontro prestamo activo con ID {id_prestamo}")
        return False

    def listar_prestamos_activos(self):
        activos = []

        for prestamo in self.prestamos:
            if prestamo.activo:
                activos.append(prestamo)

        if not activos:
            print("  No hay prestamos activos.")
            return

        print("\n  ─── PRESTAMOS ACTIVOS ───")

        for prestamo in activos:
            print(f"  {prestamo}")