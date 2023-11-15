from entities.empleado import Empleado

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)

    # Implementación de los métodos abstractos heredados de Empleado
    def calcular_salario(self):
        # Implementación de ejemplo
        pass

    def mostrar_informacion(self):
        # Implementación de ejemplo
        pass