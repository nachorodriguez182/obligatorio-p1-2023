from abc import ABC
from datetime import datetime
from exceptions.datosInvalidos import DatosInvalidos

class Empleado(ABC):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @property
    def salario(self):
        return self._salario
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise DatosInvalidos("El ID debe ser una cadena de texto.")
        self._id = value

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise DatosInvalidos("El nombre debe ser una cadena de texto.")
        self._nombre = value

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        if not isinstance(value, datetime):
            raise DatosInvalidos("La fecha de nacimiento debe ser de tipo datetime.")
        self._fecha_nacimiento = value

    @nacionalidad.setter
    def nacionalidad(self, value):
        if not isinstance(value, str):
            raise DatosInvalidos("La nacionalidad debe ser una cadena de texto.")
        self._nacionalidad = value

    @salario.setter
    def salario(self, value):
        if not isinstance(value, (int, float)):
            raise DatosInvalidos("El salario debe ser un número.")
        if value < 0:
            raise DatosInvalidos("El salario no puede ser negativo.")
        self._salario = value
    
