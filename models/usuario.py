from utils.metaclases import ValidadorMeta

class Persona(metaclass=ValidadorMeta):
    _atributos_requeridos = [
    "mostrar_info",
    "tipo" ]

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def mostrar_info(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"

    def tipo(self):
        return "Persona"

    def __str__(self):
        return self.mostrar_info()


class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni)
        self.email = email
        self.activo = True

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"Usuario: {self.nombre} {self.apellido} | DNI: {self.dni} | Email: {self.email} | {estado}"

    def tipo(self):
        return "Usuario"

    def desactivar(self):
        self.activo = False

    def __str__(self):
        return self.mostrar_info()

# Clase preparada para usar a furuto, aunque no se utiliza en el flujo principal del programa.
class Administrador(Persona):
    def __init__(self, nombre, apellido, dni, email, nivel_acceso=1):
        super().__init__(nombre, apellido, dni)
        self.email = email
        self.nivel_acceso = nivel_acceso

    def mostrar_info(self):
        return f"Administrador: {self.nombre} {self.apellido} | DNI: {self.dni} | Nivel: {self.nivel_acceso}"

    def tipo(self):
        return "Administrador"

    def __str__(self):
        return self.mostrar_info()
