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
        isbn = kwargs.get("isbn", None)
        if isbn is None:
            for arg in args:
                if isinstance(arg, str) and arg.isdigit() and len(arg) == 13:
                    isbn = arg
                    break
        if isbn is not None and (not isbn.isdigit() or len(isbn) != 13):
            print(f"  Error: ISBN '{isbn}' invalido. Debe tener 13 digitos.")
            return None
        return func(*args, **kwargs)
    return wrapper
