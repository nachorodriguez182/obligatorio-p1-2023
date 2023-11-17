from exceptions.datosInvalidos import DatosInvalidos

class Equipo:
    def __init__(self, nombre, modelo_auto):
        self._nombre = nombre
        self._modelo_auto = modelo_auto


    @property
    def nombre(self):
        return self._nombre

    @property
    def modelo_auto(self):
        return self._modelo_auto

    @property
    def lista_empleados(self):
        return self._lista_empleados_equipo.copy()

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise DatosInvalidos("El nombre del equipo no puede estar vacío.")
        self._nombre = value

    @modelo_auto.setter
    def modelo_auto(self, value):
        if not isinstance(value, str) or not value.strip():
            raise DatosInvalidos("El modelo del auto no puede estar vacío.")
        self._modelo_auto = value
