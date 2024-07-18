# Importar librerias
import random
import csv
import math


# Lista de empleados
Trabajadores = [
    {"Nombre": "Isaac Medina"},
    {"Nombre": "Gabriel Molina"},
    {"Nombre": "Esteban Mora"},
    {"Nombre": "Ivan Figueroa"},
    {"Nombre": "David Salazar"},
    {"Nombre": "Esteban Balague"},
    {"Nombre": "Ariel Ortiz"},
    {"Nombre": "Luciano Alcantara"},
    {"Nombre": "Freddy Rivera"},
    {"Nombre": "Gino Polo"},
]


# Asisnar sueldos 
sueldos = []
def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range (10)]
    print("\nSueldos Asignados")


# Clasificar sueldos
def clasificar_sueldos():
    print("\nSueldos menores a $800.000 TOTAL:", len([s for s in sueldos if s < 800000]))
    for trabajador, sueldo in zip(Trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre trabajador: {trabajador["Nombre"]} Sueldo: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    for trabajador, sueldo in zip(Trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre trabajador: {trabajador["Nombre"]} Sueldo: ${sueldo}")

    print("\nSueldos superiores a $2.000.000 TOTAL:", len([s for s in sueldos if s > 2000000]))
    for trabajador, sueldo in zip(Trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre trabajador: {trabajador["Nombre"]} Sueldo: ${sueldo}")

    print("\nTOTAL SUELDOS:",sum(sueldos))


# Estadisticas
def ver_estadisticas():
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Sueldo Maximo: ${sueldo_maximo}")
    print(f"Sueldo Minimo: ${sueldo_minimo}")
    print(f"Sueldo Promedio: ${sueldo_promedio:.0f}")
    print(f"Media Geometrica: ${media_geometrica:.0f}")


# Reporte de sueldos
def reporte_sueldos():
    with open("reporte de sueldos.csv", "w", newline="") as reporte:
        writer = csv.writer(reporte)
        writer.writerow(["Nombre trabajador", "--" "Sueldo", "--" "Descuento Salud", "--" "Descuento AFP", "--" "Sueldo Liquido"])
        writer.writerow([])
        for trabajador, sueldo in zip(Trabajadores,sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["Nombre"] ,sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"\nNombre trabajador: {trabajador['Nombre']} -- Sueldo: ${sueldo} -- Descuento salud: ${descuento_salud:.0f} -- Descuento afp: ${descuento_afp:.0f} -- Sueldo liquido: ${sueldo_liquido:.0f}")


# Salir del programa
def salir_programa():
    print("Fin del programa vuelva pronto...")
    print("Desarrollado por Isaac Medina")
    print("RUT 21.588.520-8")
    

# Menu
def menu():
    while True:
        print("\nMenu:")
        print("1.Asignar sueldos")
        print("2.Clasificar sueldos")
        print("3.Ver estadisticas")
        print("4.Generar reporte")
        print("5.Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            asignar_sueldos()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opcion no valida, intente nuevamente.")


if __name__=="__main__":
    menu()
