from models.biblioteca import Biblioteca

def menu_libros(bib):
    while True:
        print("\n  ── Gestión de Libros ──")
        print("  1. Agregar libro")
        print("  2. Eliminar libro")
        print("  3. Modificar libro")
        print("  4. Listar libros")
        print("  0. Volver")
        op = input("  Opcion: ").strip()

        if op == "1":
            titulo  = input("  Titulo: ")
            autor   = input("  Autor: ")
            isbn    = input("  ISBN (5 digitos): ")
            anio    = input("  Año: ")
            paginas = input("  Paginas: ")
            bib.alta_libro(titulo, autor, isbn, int(anio), int(paginas))

        elif op == "2":
            isbn = input("  ISBN del libro a eliminar: ")
            bib.baja_libro(isbn)

        elif op == "3":
            isbn    = input("  ISBN del libro a modificar: ")
            titulo  = input("  Nuevo titulo (Enter para omitir): ")
            autor   = input("  Nuevo autor (Enter para omitir): ")
            anio    = input("  Nuevo año (Enter para omitir): ")
            paginas = input("  Nuevas paginas (Enter para omitir): ")
            bib.modificar_libro(
                isbn,
                titulo=titulo or None,
                autor=autor or None,
                anio=int(anio) if anio else None,
                paginas=int(paginas) if paginas else None
            )

        elif op == "4":
            bib.listar_libros()

        elif op == "0":
            break


def menu_usuarios(bib):
    while True:
        print("\n  ── Gestión de Usuarios ──")
        print("  1. Agregar usuario")
        print("  2. Eliminar usuario")
        print("  3. Modificar usuario")
        print("  4. Listar usuarios")
        print("  0. Volver")
        op = input("  Opcion: ").strip()

        if op == "1":
            nombre   = input("  Nombre: ")
            apellido = input("  Apellido: ")
            dni      = input("  DNI: ")
            email    = input("  Email: ")
            bib.alta_usuario(nombre, apellido, dni, email)

        elif op == "2":
            dni = input("  DNI del usuario a eliminar: ")
            bib.baja_usuario(dni)

        elif op == "3":
            dni      = input("  DNI del usuario a modificar: ")
            nombre   = input("  Nuevo nombre (Enter para omitir): ")
            apellido = input("  Nuevo apellido (Enter para omitir): ")
            email    = input("  Nuevo email (Enter para omitir): ")
            bib.modificar_usuario(
                dni,
                nombre=nombre or None,
                apellido=apellido or None,
                email=email or None
            )

        elif op == "4":
            bib.listar_usuarios()

        elif op == "0":
            break


def menu_prestamos(bib):
    while True:
        print("\n  ── Gestión de Préstamos ──")
        print("  1. Registrar prestamo")
        print("  2. Registrar devolucion")
        print("  3. Ver prestamos activos")
        print("  0. Volver")
        op = input("  Opcion: ").strip()

        if op == "1":
            isbn = input("  ISBN del libro: ")
            dni  = input("  DNI del usuario: ")
            bib.registrar_prestamo(isbn, dni)

        elif op == "2":
            id_prestamo = input("  ID del prestamo: ")
            bib.registrar_devolucion(id_prestamo)

        elif op == "3":
            bib.listar_prestamos_activos()

        elif op == "0":
            break


def main():
    bib = Biblioteca("Biblioteca Digital UNAB")

    while True:
        print("\n╔══════════════════════════════════╗")
        print("║   SISTEMA DE BIBLIOTECA DIGITAL  ║")
        print("╚══════════════════════════════════╝")
        print("  1. Gestión de Libros")
        print("  2. Gestión de Usuarios")
        print("  3. Gestión de Préstamos")
        print("  0. Salir")
        op = input("  Opcion: ").strip()

        if op == "1":
            menu_libros(bib)
        elif op == "2":
            menu_usuarios(bib)
        elif op == "3":
            menu_prestamos(bib)
        elif op == "0":
            print("\n  Saliste correctamente.\n")
            break


if __name__ == "__main__":
    main()
