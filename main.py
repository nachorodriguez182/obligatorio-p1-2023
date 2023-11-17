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
                if any(isinstance(e, Piloto) and e.numero_auto == numero_auto for e in empleados_registrados):
                    raise ValueError("Error: Ese número de auto ya fue asignado a otro piloto.")

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

    autos_temporales = []
    empleados_temporales = []

    for i in range(12):
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
            for auto_temp in autos_temporales:
                autos_asignados.remove(auto_temp)
            for emp_temp in empleados_temporales:
                empleados_asignados.remove(emp_temp)
            return

        empleados_temporales.append(empleado_encontrado.id)
        if i == 0:
            autos_temporales.append(modelo_auto)

        if empleado_encontrado.id in empleados_asignados:
            print(f"Error: El empleado con cédula {cedula_empleado} ya está asignado a otro equipo.")
            for auto_temp in autos_temporales:
                autos_asignados.remove(auto_temp)
            for emp_temp in empleados_temporales:
                empleados_asignados.remove(emp_temp)
            return
        
        empleado = empleado_encontrado
       
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

    nuevo_equipo = Equipo(nombre_equipo,modelo_auto, empleados_equipo)
    equipos_registrados.append(nuevo_equipo)

    print(f"Equipo {nombre_equipo} creado con éxito.")

def simular_carrera():

    autos_lesionados = input("Ingrese nro de auto de todos los pilotos lesionados: ").split(',')
    autos_abandonan = input("Ingrese nro auto de todos los pilotos que abandonan separado por coma: ").split(',')
    autos_error_pits = input("Ingrese nro de auto de todos los pilotos que cometen errores en pits: ").split(',')
    autos_penalidad = input("Ingrese nro de auto de todos los pilotos que reciben penalidad: ").split(',')

    resultados = []
    for equipo in equipos_registrados:
        auto_equipo = next((auto for auto in autos_registrados if auto.modelo == equipo.modelo_auto), None)
        if auto_equipo is None:
            print(f"Auto no encontrado para el equipo {equipo.nombre}")
            continue

        suma_score_mecanicos = sum(mecanico.score for mecanico in equipo.empleados if isinstance(mecanico, Mecanico))

        pilotos_titulares = [piloto for piloto in equipo.empleados if isinstance(piloto, Piloto) and not piloto.es_reserva]
        piloto_reserva = next((piloto for piloto in equipo.empleados if isinstance(piloto, Piloto) and piloto.es_reserva), None)

        # Verificar estado de los pilotos titulares y decidir quién corre
        pilotos_activos = []
        for piloto in pilotos_titulares:
            if str(piloto.numero_auto) in autos_lesionados:
                if not pilotos_activos and piloto_reserva and not piloto_reserva.estado_lesion:
                    # Si no hay pilotos activos aún y hay un piloto reserva disponible, se utiliza el reserva
                    pilotos_activos.append(piloto_reserva)
            else:
                pilotos_activos.append(piloto)  # Añadir piloto titular no lesionado

        for piloto in pilotos_activos:
            errores_pits = autos_error_pits.count(str(piloto.numero_auto))
            penalidades = autos_penalidad.count(str(piloto.numero_auto))
            abandona = str(piloto.numero_auto) in autos_abandonan

            if abandona or piloto.estado_lesion:
                score_final = 0
            else:
                score_auto = auto_equipo.score
                score_final = suma_score_mecanicos + score_auto + piloto.score - 5 * errores_pits - 8 * penalidades

            resultados.append((piloto, score_final))

    if resultados:
        resultados.sort(key=lambda x: x[1], reverse=True)
        puntos_asignados = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

        for i, (piloto, score) in enumerate(resultados):
            puntos = puntos_asignados[i] if i < len(puntos_asignados) and score > 0 else 0
            print(f"{i + 1}. Piloto: {piloto.nombre}, Score final: {score}, Puntos: {puntos}")

            if score > 0:
                piloto.puntaje_campeonato += puntos
    else:
        print("No hay resultados para mostrar.")

    for piloto in [empleado for equipo in equipos_registrados for empleado in equipo.empleados if isinstance(empleado, Piloto)]:
        piloto.estado_lesion = False

def consultar_top_10_pilotos():
    pilotos = [empleado for empleado in empleados_registrados if isinstance(empleado, Piloto)]
    pilotos_ordenados = sorted(pilotos, key=lambda x: x.puntaje_campeonato, reverse=True)
    top_10_pilotos = pilotos_ordenados[:10]
    print("Top 10 pilotos con más puntos en el campeonato:")
    for i, piloto in enumerate(top_10_pilotos, start=1):
        print(f"{i}. {piloto.nombre} - Puntos: {piloto.puntaje_campeonato}")

def resumen_campeonato_constructores():
    puntos_por_equipo = {}
    for equipo in equipos_registrados:
        puntos = sum(piloto.puntaje_campeonato for piloto in equipo.empleados if isinstance(piloto, Piloto))
        puntos_por_equipo[equipo.nombre] = puntos
    for equipo, puntos in puntos_por_equipo.items():
        print(f"Equipo: {equipo}, Puntos: {puntos}")

def top_5_pilotos_mejores_pagos():
    pilotos = [empleado for equipo in equipos_registrados for empleado in equipo.empleados if isinstance(empleado, Piloto)]
    pilotos.sort(key=lambda piloto: piloto.salario, reverse=True)
    top_5 = pilotos[:5]
    for piloto in top_5:
        print(f"Piloto: {piloto.nombre}, Salario: {piloto.salario}")

def top_3_pilotos_habilidosos():
    pilotos = [empleado for equipo in equipos_registrados for empleado in equipo.empleados if isinstance(empleado, Piloto)]
    pilotos.sort(key=lambda piloto: piloto.score, reverse=True)
    top_3 = pilotos[:3]
    for piloto in top_3:
        print(f"Piloto: {piloto.nombre}, Score: {piloto.score}")

def listar_jefes_de_equipo():
    jefes = [empleado for equipo in equipos_registrados for empleado in equipo.empleados if isinstance(empleado, DirectorEquipo)]
    for jefe in jefes:
        print(f"Jefe de Equipo: {jefe.nombre}")

def realizar_consultas():
    while True:
        print("""
        1. Top 10 pilotos con más puntos en el campeonato
        2. Resumen campeonato de constructores
        3. Top 5 pilotos mejores pagos
        4. Top 3 pilotos más habilidosos
        5. Retornar jefes de equipo
        6. Volver al menú principal
        """)
        opcion_consulta = input("Seleccione una opción de consulta: ")

        if opcion_consulta == '1':
            consultar_top_10_pilotos()
        elif opcion_consulta == '2':
            resumen_campeonato_constructores()
        elif opcion_consulta == '3':
            top_5_pilotos_mejores_pagos()
        elif opcion_consulta == '4':
            top_3_pilotos_habilidosos()
        elif opcion_consulta == '5':
            listar_jefes_de_equipo()
        elif opcion_consulta == '6':
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    while True:
        
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

        elif opcion == '2':
                alta_auto()

        elif opcion == '3':
            alta_equipo()

        elif opcion == '4':
            simular_carrera()

        elif opcion == '5':
            realizar_consultas()
    
        elif opcion == '6':
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
