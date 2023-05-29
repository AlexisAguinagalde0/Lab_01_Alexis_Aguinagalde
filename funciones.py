import json
import re
import csv
import os


def cargar_datos():
    """
    Carga los datos de jugadores desde un archivo JSON y devuelve la lista de jugadores.
    Parametros: dt.json (Archivo JSON) - Un archivo json que contiene todos los datos del equipo Dream Team
    Retorna: Una lista de diccionarios que contiene los datos de los jugadores.  
    """
    with open("E:\Programacion\Cursada\ParcialBasquet\Lab_01_Alexis_Aguinagalde\dt.json", "r", encoding = "utf-8") as file:
        datos = json.load(file)
        jugadores = datos["jugadores"]
    return jugadores

#EJ 1
def mostrar_datos(datos_jugadores):
    for jugador in datos_jugadores:
        print(f"{jugador['nombre']} - {jugador['posicion']}")

#EJ 2        
def mostrar_estadisticas_jugador(datos_jugadores):
    """
    Muestra los datos de los jugadores en la lista proporcionada.
    Parámetros: datos_jugadores (list) - Una lista de diccionarios que contiene los datos de los jugadores.
    
    """
    
    for contador, jugador in enumerate(datos_jugadores):
        print(contador, jugador["nombre"])
    indice = int(input("Ingrese el índice del jugador: "))
    if not (indice < 0 or indice >= len(datos_jugadores)):
        jugador_seleccionado = datos_jugadores[indice]
        jugador_estadisticas = jugador_seleccionado["estadisticas"]
        print(jugador_seleccionado["nombre"])
        for clave, valor in jugador_estadisticas.items():
            clave_formateada = (str(clave).replace("_", " ")).capitalize()
            print(f"{clave_formateada}: {valor}")
        estadisticas_seleccionadas = True       
    else:    
        print("¡Índice inválido!")
        jugador_seleccionado = None
        estadisticas_seleccionadas = False
    return jugador_seleccionado, estadisticas_seleccionadas
        
#EJ 3
def guardar_estadisticas_csv(datos_jugadores, estadisticas_seleccionadas):
    
    
    return

#EJ 4
def buscar_jugador_Y_mostrar_logros(datos_jugadores):
    """
    Busca un jugador por su nombre en una lista de datos de jugadores y muestra sus logros.
    Parámetros - datos_jugadores (list): Una lista de diccionarios que contiene los datos de los jugadores.
    """
    
    nombre_a_buscar = input("Ingrese el nombre a buscar : ")
    nombre_encontrado = False
    for jugador in datos_jugadores:
        nombres = jugador["nombre"]
        logros = jugador["logros"]
        if re.search(nombre_a_buscar, nombres, re.IGNORECASE):
            nombre_encontrado = True
            print("Nombre Encontrado: ", jugador["nombre"])
            print("Logros: ")
            for logro in logros:
                print(logro)
            break
    if not nombre_encontrado:
        print("Nombre no encontrado")  
        
#EJ 5
"""
Calcula y muestra el promedio total de puntos por partido de los jugadores en la lista proporcionada.
Parámetros: datos_jugadores (list) - Una lista de diccionarios que contiene los datos de los jugadores.
Retorna: El promedio total de puntos por partido.

"""
def promedio_de_puntos_por_partido(datos_jugadores):
    suma_puntos_por_partido = 0
    cantidad_puntos_por_partido = 0
    promedio_total = 0    
    for jugador in datos_jugadores:
        if jugador["estadisticas"]["promedio_puntos_por_partido"]:
            suma_puntos_por_partido += float(jugador["estadisticas"]["promedio_puntos_por_partido"])
            cantidad_puntos_por_partido += 1
    promedio_total = suma_puntos_por_partido / cantidad_puntos_por_partido
    print("El promedio total de los jugadores es", promedio_total, "cm") 

    return promedio_total
        



