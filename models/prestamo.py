from datetime import date
import uuid
from models.libro import Libro
from models.usuario import Usuario

class FechaPrestamo:
    def __init__(self):
        self.fecha_inicio = date.today()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_devolucion = date.today()

    def duracion_dias(self):
        if self.fecha_devolucion:
            return (self.fecha_devolucion - self.fecha_inicio).days
        return (date.today() - self.fecha_inicio).days

    def __str__(self):
        inicio = self.fecha_inicio.strftime("%d/%m/%Y")
        fin = self.fecha_devolucion.strftime("%d/%m/%Y") if self.fecha_devolucion else "En curso"
        return f"Inicio: {inicio} | Devolucion: {fin}"


class Prestamo:
    def __init__(self, libro, usuario):
        self.id_prestamo = str(uuid.uuid4())[:8].upper()
        self.libro = libro
        self.usuario = usuario
        self.activo = True
        self.fechas = FechaPrestamo()  # COMPOSICION
        self.libro.marcar_prestado()

    def devolver(self):
        self.activo = False
        self.fechas.registrar_devolucion()
        self.libro.marcar_disponible()

    def esta_activo(self):
        return self.activo

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Devuelto"
        return (f"Prestamo ID: {self.id_prestamo} | "
                f"Libro: {self.libro.titulo} | "
                f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
                f"{self.fechas} | Estado: {estado}")

    def __str__(self):
        return self.mostrar_info()
