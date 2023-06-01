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
estadisticas_seleccionadas = None
jugador_estadisticas = None
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
    return jugador_estadisticas, estadisticas_seleccionadas
        
#EJ 3
def guardar_estadisticas_csv(estadisticas_seleccionadas, jugador_estadisticas):
    if estadisticas_seleccionadas:
        nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            for key, value in jugador_estadisticas.items():
                writer.writerow([key, value])
        print("Archivo csv creado")
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
        
#EJ 6
def buscar_jugador_salon_de_la_fama(datos_jugadores):
    """
    Busca un jugador por su nombre en una lista de datos de jugadores y muestra si es miembro del Salón de la Fama del Baloncesto.
    Parámetros: datos_jugadores (list) - Una lista de diccionarios que contiene los datos de los jugadores.
    """
    nombre_a_buscar = input("Ingrese el nombre a buscar : ")
    for jugador in datos_jugadores:
        nombres = jugador["nombre"]
        logros = jugador["logros"]
        bandera = True
        if re.search(nombre_a_buscar, nombres, re.IGNORECASE):
            for logro in logros:
                if logro == "Miembro del Salon de la Fama del Baloncesto":
                    print("El jugador",jugador["nombre"], "es miembro del Salon de la Fama del Baloncesto")
                    bandera = False
            if bandera:
                    print("El jugador", jugador["nombre"] ,"no es miembro del Salon de la Fama del Baloncesto")
#EJ 7
def jugador_con_mayores_rebotes_totales(datos_jugadores):
    """
    Encuentra y muestra el jugador con la mayor cantidad de rebotes totales en la lista proporcionada.
    Parámetros: datos_jugadores (list) - Una lista de diccionarios que contiene los datos de los jugadores.
    """
    rebotes_totales_maximos = 0
    nombre_rebotes_maximos = None
    for jugador in datos_jugadores:
        cantidad_rebotes = jugador["estadisticas"]["rebotes_totales"]
        if cantidad_rebotes > rebotes_totales_maximos :
            rebotes_totales_maximos = cantidad_rebotes   
            nombre_rebotes_maximos = jugador["nombre"]

    print(nombre_rebotes_maximos, rebotes_totales_maximos)

#EJ 8
def jugador_con_mayor_porcentaje_de_tiro_de_campo(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con el mayor porcentaje de tiros de campo.
    Parametros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    
    """
    porcentaje_maximo = 0
    nombre_porcentaje_maximo = None
    for jugador in datos_jugadores:
        cantidad_porcentajes = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if cantidad_porcentajes > porcentaje_maximo :
            porcentaje_maximo = cantidad_porcentajes   
            nombre_porcentaje_maximo = jugador["nombre"]

    print(nombre_porcentaje_maximo, porcentaje_maximo)

#EJ 9
def jugador_con_mayor_cantidad_de_asistencia_totales(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con la mayor cantidad de asistencias totales.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    asistencias_maximas = 0
    nombre_asistencias_maximas = None
    for jugador in datos_jugadores:
        cantidad_asistencias = jugador["estadisticas"]["asistencias_totales"]
        if cantidad_asistencias > asistencias_maximas :
            asistencias_maximas = cantidad_asistencias   
            nombre_asistencias_maximas = jugador["nombre"]

    print(nombre_asistencias_maximas, asistencias_maximas)

#EJ 10 
def jugadores_con_mayor_promedio_de_puntos_por_partido(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y solicita al usuario ingresar un valor a comparar. Luego, encuentra a los jugadores cuyo promedio de puntos por partido es mayor que el valor ingresado.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    valor_a_ingresar = int(input("Ingrese un valor a comparar: "))
    lista_aux = {}
    for jugador in datos_jugadores:
        if valor_a_ingresar < jugador["estadisticas"]["promedio_puntos_por_partido"]:
            lista_aux[jugador["nombre"]] = jugador["estadisticas"]["promedio_puntos_por_partido"]
    print(lista_aux)
#EJ 11
def jugadores_con_mayor_promedio_de_rebotes_por_partido(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y solicita al usuario ingresar un valor a comparar. Luego, encuentra a los jugadores cuyo promedio de rebotes por partido es mayor que el valor ingresado.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    valor_a_ingresar = int(input("Ingrese un valor a comparar: "))
    lista_aux = {}
    for jugador in datos_jugadores:
        if valor_a_ingresar < jugador["estadisticas"]["promedio_rebotes_por_partido"]:
            lista_aux[jugador["nombre"]] = jugador["estadisticas"]["promedio_rebotes_por_partido"]
    print(lista_aux)
#EJ 12
def jugadores_con_mayor_promedio_de_asistencias_por_partido(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y solicita al usuario ingresar un valor a comparar. Luego, encuentra a los jugadores cuyo promedio de asistencias por partido es mayor que el valor ingresado.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    valor_a_ingresar = int(input("Ingrese un valor a comparar: "))
    lista_aux = {}
    for jugador in datos_jugadores:
        if valor_a_ingresar < jugador["estadisticas"]["promedio_asistencias_por_partido"]:
            lista_aux[jugador["nombre"]] = jugador["estadisticas"]["promedio_asistencias_por_partido"]
    print(lista_aux)
#EJ 13 
def jugador_con_mayor_cantidad_de_robos_totales(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con la mayor cantidad de robos totales.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    robos_maximos = 0
    nombre_robos_maximos = None
    for jugador in datos_jugadores:
        cantidad_robos_totales = jugador["estadisticas"]["robos_totales"]
        if cantidad_robos_totales > robos_maximos :
            robos_maximos = cantidad_robos_totales   
            nombre_robos_maximos = jugador["nombre"]

    print(nombre_robos_maximos, robos_maximos)
#EJ 14
def jugador_con_mayor_cantidad_de_bloqueos_totales(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con la mayor cantidad de bloqueos totales.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    bloqueos_maximos = 0
    nombre_bloqueos_maximos = None
    for jugador in datos_jugadores:
        cantidad_bloqueos_totales = jugador["estadisticas"]["bloqueos_totales"]
        if cantidad_bloqueos_totales > bloqueos_maximos :
            bloqueos_maximos = cantidad_bloqueos_totales   
            nombre_bloqueos_maximos = jugador["nombre"]

    print(nombre_bloqueos_maximos, bloqueos_maximos)
    
#EJ 15
def jugadores_con_mayor_porcentaje_de_tiros_libres(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y solicita al usuario ingresar un valor a comparar. Luego, encuentra a los jugadores cuyo porcentaje de tiros libres es mayor que el valor ingresado.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    valor_a_ingresar = int(input("Ingrese un valor a comparar: "))
    lista_aux = {}
    for jugador in datos_jugadores:
        if valor_a_ingresar < jugador["estadisticas"]["porcentaje_tiros_libres"]:
            lista_aux[jugador["nombre"]] = jugador["estadisticas"]["porcentaje_tiros_libres"]
    print(lista_aux)
#EJ 16
def promedio_de_puntos_por_partido_sin_el_de_menor_cantidad_de_puntos(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y calcula el promedio de puntos por partido del equipo excluyendo al jugador que tiene la menor cantidad de puntos por partido.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    menor_promedio = float('inf')
    nombre_menor = None

    for jugador in datos_jugadores:
        promedio_puntos = float(jugador["estadisticas"]["promedio_puntos_por_partido"])
        if promedio_puntos < menor_promedio:
            menor_promedio = promedio_puntos
            nombre_menor = jugador["nombre"]
    total_puntos = 0
    num_jugadores = 0

    for jugador in datos_jugadores:
        if jugador["nombre"] != nombre_menor:
            total_puntos += float(jugador["estadisticas"]["promedio_puntos_por_partido"])
            num_jugadores += 1

    promedio_equipo = total_puntos / num_jugadores

    
    print(f"Promedio de puntos por partido del equipo (excluyendo a {nombre_menor}): {promedio_equipo}")
#EJ 17
def jugador_con_mayores_logros(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con la mayor cantidad de logros.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y los logros de cada jugador.
    """
    logros_maximos = 0
    nombre_logros_maximos = None
    for jugador in datos_jugadores:
        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > logros_maximos :
            logros_maximos = cantidad_logros   
            nombre_logros_maximos = jugador["nombre"]

    print(nombre_logros_maximos, logros_maximos)
#EJ 18
def jugadores_con_mayor_porcentaje_de_tiros_triples(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y solicita al usuario ingresar un valor a comparar. Luego, encuentra a los jugadores cuyo porcentaje de tiros triples es mayor que el valor ingresado.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    valor_a_ingresar = int(input("Ingrese un valor a comparar: "))
    lista_aux = {}
    for jugador in datos_jugadores:
        if valor_a_ingresar < jugador["estadisticas"]["porcentaje_tiros_triples"]:
            lista_aux[jugador["nombre"]] = jugador["estadisticas"]["porcentaje_tiros_triples"]
    print(lista_aux)
#EJ 19
def jugador_con_mayor_cantidad_de_temporadas(datos_jugadores):
    """
    Esta función recibe una lista de datos de jugadores y encuentra al jugador con la mayor cantidad de temporadas.
    Parámetros: datos_jugadores: Una lista de datos de jugadores que contiene información sobre el nombre y las estadísticas de cada jugador.
    """
    temporadas_maximos = 0
    nombre_temporadas_maximos = None
    for jugador in datos_jugadores:
        cantidad_temporadas = jugador["estadisticas"]["temporadas"]
        if cantidad_temporadas > temporadas_maximos :
            temporadas_maximos = cantidad_temporadas   
            nombre_temporadas_maximos = jugador["nombre"]
    print(nombre_temporadas_maximos, temporadas_maximos)

#EJ 20
def mostrar_jugadores_ordenados_por_posicion_de_cancha():





    return



    
##################################################################ParcialExtra##############################################################################################
#EJ 1
def cantidad_de_jugadores_por_posicion_en_la_cancha(datos_jugadores):    
    dic_aux = {}
    for jugador in datos_jugadores:
        if jugador["posicion"] in dic_aux:
            dic_aux[jugador["posicion"]] = dic_aux[jugador["posicion"]] + 1
        else:
            dic_aux[jugador["posicion"]] = 1
    for clave, valor in dic_aux.items():
        print("{0}: {1}".format(clave, valor))
    return

#EJ 3
def obtener_mejor_jugador(datos_jugadores, clave_a_buscar):
    mejor_jugador = ""
    mejor_estadistica = 0
    for jugador in datos_jugadores:
        estadistica = jugador["estadisticas"][clave_a_buscar]
        if estadistica > mejor_estadistica:
            mejor_jugador = jugador["nombre"]
            mejor_estadistica = jugador["estadisticas"][clave_a_buscar]
            formato_de_estadistica = (str(clave_a_buscar).replace("_", " ")).capitalize()
    # print("Mejor",formato_de_estadistica,":" ,mejor_jugador, mejor_estadistica)
    return mejor_jugador, mejor_estadistica, formato_de_estadistica


def imprimir_mejores_jugadores_de_su_categoria(datos_jugadores):
    categorias = [
        "temporadas",
        "puntos_totales",
        "promedio_puntos_por_partido",
        "rebotes_totales",
        "promedio_rebotes_por_partido",
        "asistencias_totales",
        "promedio_asistencias_por_partido",
        "robos_totales",
        "bloqueos_totales",
        "porcentaje_tiros_de_campo",
        "porcentaje_tiros_libres",
        "porcentaje_tiros_triples"
    ]
    for categoria in categorias:
        mejor_jugador, mejor_estadistica, formato_de_estadistica = obtener_mejor_jugador(datos_jugadores, categoria)
        print("Mejor", formato_de_estadistica + ":", mejor_jugador, "({})".format(mejor_estadistica))
###########################################################################################################################################################



datos_jugadores = cargar_datos()

def mostrar_menu():
    """
    Esta función imprime en pantalla el menú de opciones para el programa.
    """
    print("============================================================ MENÚ ======================================================")
    print("1. Mostrar la lista de todos los jugadores. \n2. Mostrar estadisticas de un jugador. \n3. Exportar estadisticas de jugador anterior a CSV. \n4. Buscar jugador por nombre y mostrar sus logros")
    print("5. Mostrar Promedio de puntos por partido de todo el equipo Dream Team, Ordenado por nombre de Manera ascendente. \n6. Ingrese un jugador para saber si esta en el salon de la fama del baloncesto")
    print("7. Mostrar jugador con mayor cantidad de Rebotes Totales. \n8. Mostrar jugador con mayor porcentaje de tiros de campo. \n9. Mostrar jugador con mayor cantidad de asistencias Totales")
    print("10. Ingresa un valor para comparar que jugadores promediaron mas puntos por partido que el valor ingresado. \n11. Ingresa un valor para comparar que jugadores promediaron mas rebotes por partido que el valor ingresado")
    print("12. Ingresa un valor para comparar que jugadores promediaron mas asistencias por partido que el valor ingresado. \n13. Mostrar jugador con mayor cantidad de Robos Totales. \n14. Mostrar jugador con mayor cantidad de Bloqueos Totales")
    print("15. Ingresa un valor para comparar que jugadores que tienen un porcentaje de tiros libres mayor que el valor ingresado. \n16. Mostrar promedio de puntos por partido excluyendo al jugador con menor cantidad de puntos por partido")
    print("17. Mostrar jugador con mayor cantidad de Logros obtenidos. \n18. Ingresa un valor para comparar que jugadores que tienen un porcentaje de tiros triples mayor que el valor ingresado.\n19. Mostrar jugador con mayor cantidad de Temporadas Jugadas")
    print("20. Ingresar un valor para ordenar jugadores por su posicion en la cancha, que tienen un porcentaje de tiros de campo superior a el valor ingresado")
    print("=======================================================================================================================")
    
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')



def obtener_eleccion():
    """
    Esta función solicita al usuario ingresar su opción del menú y verifica que sea una cadena de texto.
    Retorna la opción ingresada por el usuario como una cadena de texto.
    """
    respuesta = None
    while respuesta is None or not isinstance(respuesta, str):
        respuesta = input("Ingrese su opción: ")
    return respuesta


