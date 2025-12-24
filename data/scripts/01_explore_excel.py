import pandas as pd

file_path = "data/raw/Adidas-ventas.xlsx"

# Leer la hoja VENTAS
df_ventas = pd.read_excel(file_path, sheet_name="VENTAS")

print("Columnas de VENTAS:")
print(df_ventas.columns)

print("\nPrimeras filas:")
print(df_ventas.head())

print("\nInfo general:")
print(df_ventas.info())
