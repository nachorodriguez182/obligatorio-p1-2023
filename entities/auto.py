from exceptions.datosInvalidos import DatosInvalidos

class Auto:
    def __init__(self, modelo, año, score):
        self._modelo = modelo
        self._año = año
        self._score = score

    @property
    def modelo(self):
        return self._modelo

    @property
    def año(self):
        return self._año

    @property
    def score(self):
        return self._score

    @modelo.setter
    def modelo(self, value):
        if not isinstance(value, str):
            raise DatosInvalidos("El modelo debe ser una cadena de texto.")
        self._modelo = value

    @año.setter
    def año(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El año debe ser un número entero positivo.")
        self._año = value

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El score debe ser un número positivo.")
        self._score = value