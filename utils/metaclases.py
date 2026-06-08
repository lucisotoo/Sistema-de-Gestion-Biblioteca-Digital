class ValidadorMeta(type):
    """
    Metaclase que verifica que las clases tengan
    definidos los atributos obligatorios.
    """
    def __new__(cls, name, bases, dct):
        atributos_requeridos = dct.get("_atributos_requeridos", [])
        for atributo in atributos_requeridos:
            if atributo not in dct and not any(
                atributo in vars(base) for base in bases
            ):
                raise TypeError(
                    f"La clase '{name}' debe definir el atributo '{atributo}'"
                )
        return super().__new__(cls, name, bases, dct)
