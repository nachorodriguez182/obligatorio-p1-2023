from entities import Empleado, Piloto, Mecanico, DirectorEquipo, Equipo, Auto
from datetime import datetime
from exceptions.datosInvalidos import DatosInvalidos

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

empleados_registrados = []
lista_id =[]

def alta_empleado():

    while True:
        entrada = input("Ingrese cédula (8 dígitos): ")
        try:
            id = int(entrada)
            if id in lista_id:
                print('La cédula ya esta registrada.')
                return None
            lista_id.append(id)

            if len(entrada) != 8:
                print("Error: La cédula debe ser un número entero de 8 dígitos.")
            else:
                break
        except ValueError:
            print("Error: La entrada debe ser numérica.")
       
        return None

    while True:
        nombre = input("Ingrese nombre: ").strip()
        if nombre and nombre.replace(" ", "").isalpha():
            break
        else:
            print("Error: El nombre no puede estar vacío y debe contener solo letras.")

    while True:
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        if validar_fecha(fecha_nacimiento):
            break
        else:
            print("Error: Formato de fecha incorrecto o fecha no válida.")
    
    while True:
        nacionalidad = input("Ingrese nacionalidad: ").strip()
        if nacionalidad and nacionalidad.replace(" ", "").isalpha():
            break
        else:
            print("Error: La nacionalidad no puede estar vacío y debe contener solo letras.")
    
    while True:
        try:
            salario_input = input("Ingrese salario: ")
            if not salario_input:
                raise ValueError("El salario no puede estar vacío.")
            salario = int(salario_input)
            if salario <= 0:
                raise ValueError("El salario debe ser un número entero positivo.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    while True:
        print("Ingrese cargo: \n1- Alta Piloto \n2- Alta Piloto de Reserva \n3- Alta Mecánico \n4- Alta Jefe de Equipo")
        cargo = input()

        if cargo in ['1', '2', '3', '4']:
            break
        else:
            print("Error: Ingrese un número válido para el cargo (1, 2, 3 o 4).")

    if cargo in ['1', '2', '3']:
        while True:
            try:
                score = int(input("Ingrese score: "))
                if 1 <= score <= 99:
                    break
                print("Error: El score debe estar entre 1 y 99.")
            except ValueError:
                print("No se permite ingresar letras, ingrese un número del 1 al 99.")

    if cargo in ['1', '2']:
        while True:
            try:
                numero_auto_input = input("Ingrese número de auto: ")
                if not numero_auto_input:
                    raise ValueError("El número de auto no puede estar vacío.")
                numero_auto = int(numero_auto_input)
                if numero_auto <= 0:
                    raise ValueError("El número de auto debe ser un número entero positivo.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        es_reserva = cargo == '2'
        empleado = Piloto(id, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto, 0, False, es_reserva)

    elif cargo == '3':
        empleado = Mecanico(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
    elif cargo == '4':
        empleado = DirectorEquipo(id, nombre, fecha_nacimiento, nacionalidad, salario)
   
    empleados_registrados.append(empleado)
    print(f'Empleado {empleado.nombre} ha sido creado con éxito.')

    return empleado
   
autos_registrados = []
lista_autos_creados= []

def alta_auto():
    modelo = input("Ingrese modelo: ").strip()

    if modelo in lista_autos_creados:
        print("Error: Ese modelo de auto ya fue registrado.")
        return None
    lista_autos_creados.append(modelo)

    if not modelo:
        raise DatosInvalidos("El modelo no puede estar vacío.")

    while True:
        try:
            año_input = input("Ingrese año: ")
            año = int(año_input)
            if not (1000 <= año <= datetime.now().year):
                raise ValueError("El año debe ser un número entero positivo de 4 dígitos y no mayor al año actual.")
            break
        except ValueError:
            print("Error: El año debe ser un número válido de 4 dígitos.")

    while True:
        try:
            score_input = input("Ingrese score: ")
            score = int(score_input)
            if 1 <= score <= 99:
                break
            else:
                raise ValueError("El score debe estar entre 1 y 99.")
        except ValueError:
            print("Error: El score debe ser un número válido.")

    auto = Auto(modelo, año, score)
    autos_registrados.append(auto)
    print(f"Auto {modelo} registrado exitosamente.")
    return auto

autos_asignados = []
empleados_asignados = []
equipos_registrados = []

def alta_equipo():
    nombre_equipo = input("Ingrese nombre del equipo: ").strip()
    modelo_auto = input("Ingrese modelo de auto: ").strip()

    auto = next((a for a in autos_registrados if a.modelo == modelo_auto), None)
    if not auto:
        print("Error: El modelo de auto ingresado no existe.")
        return
    if modelo_auto in autos_asignados:
        print("Error: El auto ya está asignado a otro equipo.")
        return
    autos_asignados.append(modelo_auto)

    empleados_equipo = []
    contador_pilotos = 0
    contador_pilotos_reserva = 0
    contador_directores = 0
    contador_mecanicos = 0

    for i in range(11):
        entrada_cedula = input("Ingrese cédula del empleado numero" + str(i+1) + ':')
        try:
            cedula_empleado = int(entrada_cedula)
        except ValueError:
            print("Error: La cédula debe ser un número.")
            return

        empleado_encontrado = None
        for e in empleados_registrados:
            if e.id == cedula_empleado:
                empleado_encontrado = e
            break

        if not empleado_encontrado:
            print(f"Error: No se encontró un empleado con la cédula {cedula_empleado}.")
            return
        else:
            empleado = empleado_encontrado
            if empleado.id in empleados_asignados:
                print(f"Error: El empleado con cédula {cedula_empleado} ya está asignado a otro equipo.")
                return

        if isinstance(empleado, Piloto):
            if empleado.es_reserva:
                contador_pilotos_reserva += 1
                if contador_pilotos_reserva > 1:
                    print("Error: Ya hay un piloto reserva en el equipo.")
                    return
            else:
                contador_pilotos += 1
                if contador_pilotos > 2:
                    print("Error: Ya hay dos pilotos en el equipo.")
                    return
        elif isinstance(empleado, Mecanico):
            contador_mecanicos += 1
            if contador_mecanicos > 8:
                print("Error: Ya hay ocho mecánicos en el equipo.")
                return
        elif isinstance(empleado, DirectorEquipo):
            contador_directores += 1
            if contador_directores > 1:
                print("Error: Ya hay un director de equipo en el equipo.")
                return
        else:
            print("Error: Tipo de empleado no reconocido o no permitido en el equipo.")
            return

        empleados_asignados.append(empleado.id)
        empleados_equipo.append(empleado)

    nuevo_equipo = Equipo(nombre_equipo, auto, empleados_equipo)
    equipos_registrados.append(nuevo_equipo)

    print(f"Equipo {nombre_equipo} creado con éxito.")

def main():
    while True:
        # Mostrar el menú de opciones
        print("""
        1. Alta de empleado
        2. Alta de auto
        3. Alta de equipo
        4. Simular carrera
        5. Realizar consultas
        6. Finalizar programa
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alta_empleado()
            print (empleados_registrados)
        elif opcion == '2':
            try:
                alta_auto()
                print(autos_registrados)
            except DatosInvalidos as e:
                print(e)

        elif opcion == '3':
            alta_equipo()
            print(equipos_registrados)

        elif opcion == '4':
            # Lógica para simular carrera
            pass
        elif opcion == '5':
            # Lógica para realizar consultas
            pass
        elif opcion == '6':
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
