import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# DEFININDO LOS ARCHIVOS
archivo = "data.csv"

def main():
    print("🚀 Iniciando análisis automático de datos de ventas...")
    print(f"📂 Archivo de origen: {archivo}")

    # VERIFICAMOS QUE EXISTA EL ARCHIVO
    if not os.path.exists(archivo):
        print(f"❌ Error: No se encontró el archivo '{archivo}'.")
        return

    # LEER EL ARCHIVO CSV CON LA INFORMACINO
    try:
        df = pd.read_csv(archivo)
    except Exception as e:
        print(f"❌ Error al leer el archivo CSV: {e}")
        return
