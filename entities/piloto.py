from entities.empleado import Empleado
from exceptions.datosInvalidos import DatosInvalidos

class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, puntaje_campeonato, estado_lesion, es_reserva):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self._score = score
        self._numero_auto = numero_auto
        self._puntaje_campeonato = puntaje_campeonato
        self._estado_lesion = estado_lesion
        self._es_reserva = es_reserva
    

    @property
    def score(self):
        return self._score

    @property
    def numero_auto(self):
        return self._numero_auto

    @property
    def puntaje_campeonato(self):
        return self._puntaje_campeonato

    @property
    def estado_lesion(self):
        return self._estado_lesion
    
    @property
    def es_reserva(self):
        return self._es_reserva

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El score debe ser un valor entero positivo.")
        self._score = value

    @numero_auto.setter
    def numero_auto(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El numero de auto debe ser un entero positivo.")
        self._numero_auto = value

    @puntaje_campeonato.setter
    def puntjaje_campeonato(self, value):
        if not isinstance(value, int) or value < 0:
            raise DatosInvalidos("El puntaje de campeonato debe ser un entero positivo.")
        self._puntaje_campeonato = value

    @estado_lesion.setter
    def estado_lesion(self, value):
        if not isinstance(value, bool):
            raise DatosInvalidos("El estado de lesión debe ser un valor booleano.")
        self._estado_lesion = value

    @es_reserva.setter
    def es_reserva(self, value):
        if not isinstance(value, bool):
            raise DatosInvalidos("El  es_reserva debe ser un valor booleano.")
        self._es_reserva = value