import json

def cargar_datos():
    with open("E:\Programacion\Cursada\ParcialBasquet\Lab_01_Alexis_Aguinagalde\dt.json", "r") as file:
        datos = json.load(file)
        jugadores = datos["jugadores"]
    return jugadores

def mostrar_datos(datos_jugadores):
    for jugador in datos_jugadores:
        print(f"{jugador['nombre']} - {jugador['posicion']}")
        
def mostrar_estadisticas_jugador(datos):
    for contador, jugador in enumerate(datos_jugadores, start=1):
        print(contador, jugador["nombre"])
    indice = int(input("Ingrese el índice del jugador: "))
    if not (indice < 0 or indice >= len(datos_jugadores)):
        jugador = datos[indice]
        jugadorindice = jugador["estadisticas"]
        for clave, valor in jugadorindice.items():
            clave_formateada = (str(clave).replace("_", " ")).capitalize()
            print(f"{clave_formateada}: {valor}")
    else:    
        print("¡Índice inválido!")
        

def guardar_estadisticas_csv(datos):
    indice = int(input("Ingrese el índice del jugador: "))
    if indice < 0 or indice >= len(datos):
        print("¡Índice inválido!")
        return
    jugador = datos[indice]
