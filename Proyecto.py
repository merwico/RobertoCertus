import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
    
    # Valido si es que existen columnas en mi archivo
    columna = df.select_dtypes(include=[np.number])
    if columna.empty:
        print("\n.....No hay columnas para graficar.....")
        return
        
    # PONIENDO NOMBRE AL ARCHIVO
    fecha = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ruta = os.path.join(carpeta, f"Grafico_ventas_{fecha}.png")

    # GENERO LOS GRAFICOS
    try:
        plt.figure(figsize=(10, 6))
        columna.plot(ax=plt.gca())
        plt.title("📈 Análisis de Ventas - Columnas Numéricas")
        plt.xlabel("Registros")
        plt.ylabel("Valores")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(ruta)
        plt.close()
        print(f"\n.....Gráfico generado y guardado en: {ruta}")
    except Exception as e:
        print(f".....Error al generar el gráfico: {e}")
        return

#Llamo la funcion
if __name__ == "__main__":
    main()

