class ValidadorMeta(type):
    """
    Metaclase que verifica que las clases definan
    los atributos obligatorios.
    """

    def __new__(cls, name, bases, dct):
        atributos = dct.get("_atributos_requeridos", [])

        for atributo in atributos:
            if atributo not in dct:
                raise TypeError(
                    f"La clase '{name}' debe definir el atributo '{atributo}'"
                )

        return super().__new__(cls, name, bases, dct)
