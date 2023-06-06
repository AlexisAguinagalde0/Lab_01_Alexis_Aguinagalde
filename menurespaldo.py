from funcionessimplificadas import mostrar_menu, obtener_eleccion, datos_jugadores, mostrar_datos, mostrar_estadisticas_jugador, guardar_estadisticas_csv, estadisticas_seleccionadas, jugador_estadisticas
from funcionessimplificadas import buscar_jugador_Y_mostrar_logros, buscar_jugador_salon_de_la_fama, promedio_de_puntos_por_partido, jugador_con_mayor_puntos_por_estadistica, jugadores_con_mayor_promedio_de_stats
from funcionessimplificadas import promedio_de_puntos_por_partido_sin_el_de_menor_cantidad_de_puntos,jugador_con_mayores_logros,mostrar_jugadores_ordenados_por_posicion_de_cancha, cantidad_de_jugadores_por_posicion_en_la_cancha,mostrar_jugadores_allstar_descendentes, imprimir_mejores_jugadores_de_su_categoria, muestra_mejor_jugador_estadistica


while True:
    mostrar_menu()
    respuesta_usuario = obtener_eleccion()
    match(respuesta_usuario):
        case "1":
            mostrar_datos(datos_jugadores)
            break     
        case "2":
            mostrar_estadisticas_jugador(datos_jugadores)
        case "3":
            guardar_estadisticas_csv(estadisticas_seleccionadas, jugador_estadisticas)
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
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "rebotes_totales")
            break        
        case "8":
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "porcentaje_tiros_de_campo")
            break
        case "9":
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "asistencias_totales")
            break
        case "10":
            jugadores_con_mayor_promedio_de_stats(datos_jugadores, "promedio_puntos_por_partido")
            break
        case "11":
            jugadores_con_mayor_promedio_de_stats(datos_jugadores, "promedio_rebotes_por_partido")
            break
        case "12":
            jugadores_con_mayor_promedio_de_stats(datos_jugadores, "promedio_asistencias_por_partido")
            break    
        case "13":
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "robos_totales")
            break
        case "14":
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "bloqueos_totales")
            break
        case "15":
            jugadores_con_mayor_promedio_de_stats(datos_jugadores, "porcentaje_tiros_libres")
            break
        case "16":
            promedio_de_puntos_por_partido_sin_el_de_menor_cantidad_de_puntos(datos_jugadores)
            break
        case "17":
            jugador_con_mayores_logros(datos_jugadores)
            break
        case "18":
            jugadores_con_mayor_promedio_de_stats(datos_jugadores, "porcentaje_tiros_triples")
            break
        case "19":
            jugador_con_mayor_puntos_por_estadistica(datos_jugadores, "temporadas")
            break
        case "20":
            mostrar_jugadores_ordenados_por_posicion_de_cancha(datos_jugadores)
            break
        case "21":
            cantidad_de_jugadores_por_posicion_en_la_cancha(datos_jugadores)
            break
        case "22":
            mostrar_jugadores_allstar_descendentes(datos_jugadores)
            break
        case "23":
            imprimir_mejores_jugadores_de_su_categoria(datos_jugadores)
            break
        case "24":
            muestra_mejor_jugador_estadistica(datos_jugadores)
            break