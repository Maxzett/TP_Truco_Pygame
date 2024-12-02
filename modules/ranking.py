import csv

# Registrar resultados en el archivo CSV
def registrar_resultado(nombre_jugador, gano):
    ruta_csv = "ranking.csv"
    try:
        # Leer datos existentes
        with open(ruta_csv, "r") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            datos = list(lector_csv)
    except FileNotFoundError:
        datos = []

    # Actualizar o agregar jugador
    for fila in datos:
        if fila[0] == nombre_jugador:
            if gano:
                fila[1] = str(int(fila[1]) + 1)
            else:
                fila[2] = str(int(fila[2]) + 1)
            break
    else:
        # Si el jugador no está en el archivo
        datos.append([nombre_jugador, "1" if gano else "0", "0" if gano else "1"])

    # Guardar los datos actualizados
    with open(ruta_csv, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos)