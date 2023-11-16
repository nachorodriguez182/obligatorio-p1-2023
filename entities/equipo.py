from exceptions.datosInvalidos import DatosInvalidos

class Equipo:
    def __init__(self, nombre, modelo_auto):
        self._nombre = nombre
        self._modelo_auto = modelo_auto
        self._lista_empleados_equipo = []

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


    def añadir_empleado(self, empleado):
        self._lista_empleados_equipo.append(empleado)
    
    def remover_empleado(self, id_empleado):
        self._lista_empleados_equipo = [emp for emp in self._lista_empleados_equipo if emp.id != id_empleado]
    
    def listar_empleados(self):
        return self._lista_empleados_equipo

    def asociar_auto(self, auto):
        self._modelo_auto = auto