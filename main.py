import json

def cargar_datos():
    with open("E:\Programacion\Cursada\ParcialBasquet\Lab_01_Alexis_Aguinagalde\dt.json", "r") as file:
        datos = json.load(file)
        jugadores = datos["jugadores"]
    return jugadores

