
from funciones import cargar_datos, mostrar_datos, datos_jugadores, mostrar_estadisticas_jugador, guardar_estadisticas_csv, buscar_jugador_Y_mostrar_logros,promedio_de_puntos_por_partido, buscar_jugador_salon_de_la_fama
from funciones import jugador_con_mayores_rebotes_totales, jugador_con_mayor_porcentaje_de_tiro_de_campo, jugador_con_mayor_cantidad_de_asistencia_totales, jugadores_con_mayor_promedio_de_puntos_por_partido
from funciones import jugador_con_mayor_cantidad_de_robos_totales,jugadores_con_mayor_promedio_de_asistencias_por_partido , jugador_con_mayor_cantidad_de_bloqueos_totales,jugadores_con_mayor_promedio_de_rebotes_por_partido , jugadores_con_mayor_porcentaje_de_tiros_libres,jugador_con_mayores_logros
from funciones import jugadores_con_mayor_porcentaje_de_tiros_triples,promedio_de_puntos_por_partido_sin_el_de_menor_cantidad_de_puntos , jugador_con_mayor_cantidad_de_temporadas, mostrar_menu, obtener_eleccion

datos_jugadores = cargar_datos()
while True:
    mostrar_menu()
    respuesta_usuario = obtener_eleccion()
    match(respuesta_usuario):
        case "1":
            mostrar_datos(datos_jugadores)
            break     
        case "2":
            mostrar_estadisticas_jugador(datos_jugadores)
            break
        case "3":
            guardar_estadisticas_csv(datos_jugadores)
            break
        case "4":
            buscar_jugador_Y_mostrar_logros(datos_jugadores)
            break
        case "5":
            promedio_de_puntos_por_partido(datos_jugadores)
            break
        case "6":
            buscar_jugador_salon_de_la_fama(datos_jugadores)
            break
        case "7":
            jugador_con_mayores_rebotes_totales(datos_jugadores)
            break        
        case "8":
            jugador_con_mayor_porcentaje_de_tiro_de_campo(datos_jugadores)
            break
        case "9":
            jugador_con_mayor_cantidad_de_asistencia_totales(datos_jugadores)
            break
        case "10":
            jugadores_con_mayor_promedio_de_puntos_por_partido(datos_jugadores)
            break
        case "11":
            jugadores_con_mayor_promedio_de_rebotes_por_partido(datos_jugadores)
            break
        case "12":
            jugadores_con_mayor_promedio_de_asistencias_por_partido(datos_jugadores)
            break    
        case "13":
            jugador_con_mayor_cantidad_de_robos_totales(datos_jugadores)
            break
        case "14":
            jugador_con_mayor_cantidad_de_bloqueos_totales(datos_jugadores)
            break
        case "15":
            jugadores_con_mayor_porcentaje_de_tiros_libres(datos_jugadores)
            break
        case "16":
            promedio_de_puntos_por_partido_sin_el_de_menor_cantidad_de_puntos(datos_jugadores)
            break
        case "17":
            jugador_con_mayores_logros(datos_jugadores)
            break
        case "18":
            jugadores_con_mayor_porcentaje_de_tiros_triples(datos_jugadores)
            break
        case "19":
            jugador_con_mayor_cantidad_de_temporadas(datos_jugadores)
            break
        case 0:

            break
