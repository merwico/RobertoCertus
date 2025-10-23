import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import git
import os
from datetime import datetime

# DEFININDO LOS ARCHIVOS
archivo = "data.csv"
carpeta = "Resultados"

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
        
    # IMPRIMO PARA VERIFICAR INFO
    print("\n✅ Primeras filas de los datos:")
    print(df.head())

    print("\n📊 Resumen informacion general:")
    print(df.info())

    # CREO LA CARPETA PARA GUARDAR LA INFO
    os.makedirs(carpeta, exist_ok=True)
    # PONIENDO NOMBRE AL ARCHIVO
    fecha = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ruta = os.path.join(carpeta, f"Grafico_ventas_{fecha}.png")
    
if __name__ == "__main__":
main()

