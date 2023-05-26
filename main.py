import json
import csv

def cargar_jugadores():
    with open("dt.json") as file:
        jugadores = json.load(file)
    return jugadores

def mostrar_jugadores(jugadores):
    for jugador in jugadores:
        print(f"{jugador['nombre']} - {jugador['posicion']}")

def mostrar_estadisticas_jugador(jugadores):
    indice = int(input("Ingrese el índice del jugador: "))
    if indice < 0 or indice >= len(jugadores):
        print("¡Índice inválido!")
        return
    jugador = jugadores[indice]

def guardar_estadisticas_csv(jugadores):
    indice = int(input("Ingrese el índice del jugador: "))
    if indice < 0 or indice >= len(jugadores):
        print("¡Índice inválido!")
        return
    jugador = jugadores[indice]


def buscar_jugador_por_nombre(jugadores):

    nombre = input("Ingrese el nombre del jugador: ")
    encontrado = False
    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre.lower():

            encontrado = True
            break
    if not encontrado:
        print("Jugador no encontrado")



def main():
    jugadores = cargar_jugadores()
    
    while True:
        print("===== Menú =====")
        print("1. Mostrar la lista de jugadores")
        print("2. Mostrar estadísticas completas de un jugador")
        print("3. Guardar estadísticas de un jugador en un archivo CSV")
        print("4. Buscar jugador por nombre y mostrar logros")
        print("0. Salir")
        
        opcion = int(input("Ingrese la opción deseada: "))
        
        if opcion == 0:
            break
        elif opcion == 1:
            mostrar_jugadores(jugadores)
        elif opcion == 2:
            mostrar_estadisticas_jugador(jugadores)
        elif opcion == 3:
            guardar_estadisticas_csv(jugadores)
        elif opcion == 4:
            buscar_jugador_por_nombre(jugadores)
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()


