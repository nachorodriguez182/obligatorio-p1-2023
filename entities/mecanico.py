from entities.empleado import Empleado
from exceptions.datosInvalidos import DatosInvalidos

class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score
        
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El score debe ser un entero positivo.")
        self._score = value
