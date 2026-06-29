from datetime import datetime

def log_operacion(func):
    def wrapper(*args, **kwargs):
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\n[{ahora}] Ejecutando: {func.__name__}")

        resultado = func(*args, **kwargs)

        print(f"[{ahora}] Finalizado: {func.__name__}")
        return resultado

    return wrapper


def validar_isbn(func):
    def wrapper(*args, **kwargs):

        isbn = kwargs.get("isbn")

        if isbn is None:
            for arg in args:
                if isinstance(arg, str):
                    isbn = arg
                    break

        if isbn is None:
            return func(*args, **kwargs)

        if not isbn.isdigit() or len(isbn) != 5:
            print("  Error: El ISBN debe tener 5 digitos.")
            return None

        return func(*args, **kwargs)

    return wrapper
