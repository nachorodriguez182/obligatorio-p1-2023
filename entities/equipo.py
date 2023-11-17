from exceptions.datosInvalidos import DatosInvalidos

class Equipo:
    def __init__(self, nombre, modelo_auto, empleados):
        self._nombre = nombre
        self._modelo_auto = modelo_auto
        self._empleados = empleados


    @property
    def nombre(self):
        return self._nombre

    @property
    def modelo_auto(self):
        return self._modelo_auto
    
    @property
    def empleados(self):
        return self._empleados

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

    @empleados.setter
    def empleados(self, value):
        self._empleados = value