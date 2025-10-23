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
