import os
import shutil

# Carpeta donde llegan los logs sin clasificar
CARPETA_ORIGEN = "logs_entrada"

# Diccionario que asocia cada extension con su carpeta de destino
CARPETAS_DESTINO = {
    ".log_app_1": os.path.join("logs_clasificados", "App1_Web"),
    ".log_app_2": os.path.join("logs_clasificados", "App2_Firewall"),
    ".log_app_3": os.path.join("logs_clasificados", "App3_Auth"),
}


def clasificar_logs(origen, mapa_destinos):
    """Recorre la carpeta de origen y mueve cada archivo segun su extension."""

    if not os.path.exists(origen):
        print(f"[ERROR] La carpeta de origen '{origen}' no existe.")
        return

    archivos = os.listdir(origen)
    if not archivos:
        print("[INFO] No se encontraron archivos para clasificar.")
        return

    contador = {ext: 0 for ext in mapa_destinos}
    no_reconocidos = 0

    print(f"[INFO] Iniciando clasificacion de {len(archivos)} archivo(s)...\n")

    for archivo in archivos:
        ruta_origen = os.path.join(origen, archivo)
        if not os.path.isfile(ruta_origen):
            continue

        _, extension = os.path.splitext(archivo)

        if extension in mapa_destinos:
            carpeta_destino = mapa_destinos[extension]
            os.makedirs(carpeta_destino, exist_ok=True)

            ruta_destino = os.path.join(carpeta_destino, archivo)
            shutil.move(ruta_origen, ruta_destino)

            contador[extension] += 1
            print(f"[OK]      {archivo:40s} -> {carpeta_destino}")
        else:
            no_reconocidos += 1
            print(f"[OMITIDO] {archivo:40s} (extension no reconocida: {extension})")

    print("\n" + "=" * 60)
    print("RESUMEN DE CLASIFICACION - ALLSAFE CYBERSECURITY")
    print("=" * 60)
    for ext, cantidad in contador.items():
        print(f"  {ext:12s} : {cantidad} archivo(s)  ->  {mapa_destinos[ext]}")
    print(f"  {'No reconocidos':12s} : {no_reconocidos} archivo(s)")
    print("=" * 60)


if __name__ == "__main__":
    clasificar_logs(CARPETA_ORIGEN, CARPETAS_DESTINO)