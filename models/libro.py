from utils.metaclases import ValidadorMeta

class ItemBiblioteca(metaclass=ValidadorMeta):
    _atributos_requeridos = [
    "mostrar_info",
    "tipo_item" ]

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_info(self):
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn})"

    def tipo_item(self):
        return "Item"

    def __str__(self):
        return self.mostrar_info()


class Libro(ItemBiblioteca):
    def __init__(self, titulo, autor, isbn, anio, paginas):
        super().__init__(titulo, autor, isbn)
        self.anio = anio
        self.paginas = paginas
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return (f"Libro: {self.titulo} | Autor: {self.autor} | "
                f"ISBN: {self.isbn} | Año: {self.anio} | "
                f"Paginas: {self.paginas} | {estado}")

    def tipo_item(self):
        return "Libro"

    def marcar_prestado(self):
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True

    def __str__(self):
        return self.mostrar_info()
