import pandas as pd

file_path = "data/raw/Adidas-ventas.xlsx"

ventas = pd.read_excel(file_path, sheet_name="VENTAS")
minoristas = pd.read_excel(file_path, sheet_name="MINORISTAS")
ciudades = pd.read_excel(file_path, sheet_name="CIUDADES")
estados = pd.read_excel(file_path, sheet_name="ESTADOS")
regiones = pd.read_excel(file_path, sheet_name="REGIONES")
metodos = pd.read_excel(file_path, sheet_name="METODOS VENTA")
categorias = pd.read_excel(file_path, sheet_name="CATEGORIAS PRODUCTO")

print("\nVENTAS columnas:\n", list(ventas.columns))
print("\nMINORISTAS columnas:\n", list(minoristas.columns))
print("\nCIUDADES columnas:\n", list(ciudades.columns))
print("\nESTADOS columnas:\n", list(estados.columns))
print("\nREGIONES columnas:\n", list(regiones.columns))
print("\nMETODOS VENTA columnas:\n", list(metodos.columns))
print("\nCATEGORIAS PRODUCTO columnas:\n", list(categorias.columns))

# Chequeo rápido: qué columnas con 'Ciudad' existen
print("\nPosibles columnas relacionadas a ciudad en MINORISTAS:")
print([c for c in minoristas.columns if "ciud" in c.lower()])

print("\nPosibles columnas relacionadas a ciudad en VENTAS:")
print([c for c in ventas.columns if "ciud" in c.lower()])
