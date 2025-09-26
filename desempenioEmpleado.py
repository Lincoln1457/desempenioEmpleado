sistemYes = True
rinicio = "Presione Enter para continuar al sistema."

menuPrincipal = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                     |
|      Bienvenidx al sistema que organiza a los       |
|        empleados que se tiene en la empresa         |
|             según su desempeño en esta              |
|                                                     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                     |
| 1. Agregar nuevo empleado.                          |
| 2. Ver desempeño individual.                        |
| 3. Ver promedio de desempeño de trabajadores.       |
| 4. Mostrar top 3 de mejores trabajadores.           |
| 5. Reporte general.                                 |
| 6. Retirarse del sistema.                           |
|                                                     |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

trabajadores = [
    {'identidad': "Miguel Tapiero", 'calid': 9, 'puntu': 10, 'colab': 9, 'efici': 10},
    {'identidad': "Rosalía Vila", 'calid': 10, 'puntu': 7.5, 'colab': 9.5, 'efici': 7},
    {'identidad': "Jensy Mendez", 'calid': 9, 'puntu': 3, 'colab': 4.5, 'efici': 10},
    {'identidad': "Natalia Peluso", 'calid': 6.5, 'puntu': 1, 'colab': 7, 'efici': 10},
    {'identidad': "Pedro Peralta", 'calid': 1, 'puntu': 1, 'colab': 1, 'efici': 1}
]

def ponerDatos(trabajadores):
    print("\nAGREGAR NUEVO EMPLEADO\n")
    who = input("¿Cuál es el nombre y apellido del empleado?: ")
    nivCal = float(input("Nivel de calidad (0 a 10): "))
    nivPun = float(input("Nivel de puntualidad (0 a 10): "))
    nivCol = float(input("Nivel de colaboración (0 a 10): "))
    nivEfi = float(input("Nivel de eficiencia (0 a 10): "))
    trabajadores.append({'identidad': who, 'calid': nivCal, 'puntu': nivPun, 'colab': nivCol, 'efici': nivEfi})
    print("El empleado fue agregado exitosamente.\n")


def operarPromedios():
    print("\nCONSULTAR PROMEDIO DE EMPLEADO\n")
    nombre = input("Ingrese el nombre o parte del nombre del empleado: ").lower()
    encontrado = False
    for persona in trabajadores:
        if nombre in persona['identidad'].lower():
            promedio = (persona['calid'] + persona['puntu'] + persona['colab'] + persona['efici']) / 4
            print(f"El promedio de {persona['identidad']} es: {promedio:.1f}\n")
            encontrado = True
    if not encontrado:
        print("No se encontró un empleado con ese nombre.\n")

def verPromediosGenerales():
    print("\nPROMEDIO DE TODOS LOS EMPLEADOS\n")
    for persona in trabajadores:
        promedio = (persona['calid'] + persona['puntu'] + persona['colab'] + persona['efici']) / 4
        print(f"{persona['identidad']}: {promedio:.1f}")
    print()

def mostrarTop3():
    print("\n🏆 TOP 3 MEJORES EMPLEADOS\n")
    lista_ordenada = sorted(trabajadores, key=lambda x: (x['calid'] + x['puntu'] + x['colab'] + x['efici']) / 4, reverse=True)
    for i, persona in enumerate(lista_ordenada[:3]):
        promedio = (persona['calid'] + persona['puntu'] + persona['colab'] + persona['efici']) / 4
        print(f"{i+1}. {persona['identidad']} - Promedio: {promedio:.1f}")
    print()

def verReporte():
    print("\n📋 REPORTE GENERAL DE EMPLEADOS\n")
    for persona in trabajadores:
        promedio = (persona['calid'] + persona['puntu'] + persona['colab'] + persona['efici']) / 4
        if promedio >= 8.5:
            estado = "Sobresaliente"
        elif promedio < 5:
            estado = "Bajo"
        else:
            estado = "Aceptable"
        print(f"{persona['identidad']} | Promedio: {promedio:.1f} | Estado: {estado}")
    print()

while sistemYes:
    print(menuPrincipal)
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        ponerDatos(trabajadores)
        input(f"{rinicio}")
        
    elif opcion == "2":
        operarPromedios()
        input(f"{rinicio}")
        
    elif opcion == "3":
        verPromediosGenerales()
        input(f"{rinicio}")
        
    elif opcion == "4":
        mostrarTop3()
        input(f"{rinicio}")
        
    elif opcion == "5":
        verReporte()
        input(f"{rinicio}")
        
    elif opcion == "6":
        print("\nGracias por usar el sistema. ¡Nos vemos!")
        sistemYes = False
    else:
        print("Opción no válida. Intente de nuevo.\n")
