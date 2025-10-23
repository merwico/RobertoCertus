import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# DEFININDO LOS ARCHIVOS
archivo = "data.csv"
carpeta = "Resultados"

def main():
    print("🚀 Iniciando análisis automático de datos de ventas")
    print(f"📂 Archivo de origen: {archivo}")

     # Verifico que el archivo exista
    if not os.path.exists(archivo):
        print(f"❌ Error: No se encontró el archivo '{archivo}'.")
        return
    # Lectura del archivo
    try:
        df = pd.read_csv(archivo)
    except Exception as e:
        print(f"❌ Error al leer el archivo CSV: {e}")
        return
    # Valido si esta vacio el archivo
    if df.empty:
        print("⚠️ El archivo CSV está vacío. No se generará gráfico.")
        return
