import pandas as pd

# =========================
# CONFIG
# =========================
FILE_PATH = "data/raw/Adidas-ventas.xlsx"
OUT_PATH = "data/processed/adidas_ventas_tabla_plana.csv"

# =========================
# LOAD
# =========================
ventas = pd.read_excel(FILE_PATH, sheet_name="VENTAS")
minoristas = pd.read_excel(FILE_PATH, sheet_name="MINORISTAS")
ciudades = pd.read_excel(FILE_PATH, sheet_name="CIUDADES")
estados = pd.read_excel(FILE_PATH, sheet_name="ESTADOS")
regiones = pd.read_excel(FILE_PATH, sheet_name="REGIONES")
metodos = pd.read_excel(FILE_PATH, sheet_name="METODOS VENTA")
categorias = pd.read_excel(FILE_PATH, sheet_name="CATEGORIAS PRODUCTO")

# =========================
# CHECK KEYS (rápido)
# =========================
required_cols = {
    "ventas": ["Minorista_ID", "Ciudad_ID", "Cat_Producto_ID", "Metodo_venta_ID", "Fecha_facturacion",
               "Total_ventas", "Ganancia", "Margen", "Unidades_vendidas", "Precio_unitario"],
    "minoristas": ["Minorista_ID", "Ciudad_ID"],
    "ciudades": ["Ciudad_ID", "Estado_ID", "Region_ID"],
    "estados": ["Estado_ID"],
    "regiones": ["Region_ID"],
    "metodos": ["Metodo_venta_ID"],
    "categorias": ["Cat_Producto_ID"],
}

dfs = {
    "ventas": ventas,
    "minoristas": minoristas,
    "ciudades": ciudades,
    "estados": estados,
    "regiones": regiones,
    "metodos": metodos,
    "categorias": categorias,
}

for name, cols in required_cols.items():
    missing = [c for c in cols if c not in dfs[name].columns]
    if missing:
        raise KeyError(f"Faltan columnas en {name}: {missing}. Columnas disponibles: {list(dfs[name].columns)}")

# =========================
# MERGE (modelo estrella)
# =========================
df = ventas.merge(minoristas, on="Minorista_ID", how="left", suffixes=("", "_minorista"))
df = df.merge(ciudades, on="Ciudad_ID", how="left", suffixes=("", "_ciudad"))
df = df.merge(estados, on="Estado_ID", how="left", suffixes=("", "_estado"))
df = df.merge(regiones, on="Region_ID", how="left", suffixes=("", "_region"))
df = df.merge(metodos, on="Metodo_venta_ID", how="left", suffixes=("", "_metodo"))
df = df.merge(categorias, on="Cat_Producto_ID", how="left", suffixes=("", "_categoria"))

# =========================
# FEATURES PARA DASHBOARD
# =========================
df["Fecha_facturacion"] = pd.to_datetime(df["Fecha_facturacion"])
df["Año"] = df["Fecha_facturacion"].dt.year
df["Mes"] = df["Fecha_facturacion"].dt.month
df["MesNombre"] = df["Fecha_facturacion"].dt.strftime("%Y-%m")

# Orden recomendado (negocio)
preferred = [
    "Venta_ID", "Fecha_facturacion", "Año", "Mes", "MesNombre",
    "Total_ventas", "Ganancia", "Margen", "Unidades_vendidas", "Precio_unitario",
]

# El resto de columnas (dimensiones) al final
rest = [c for c in df.columns if c not in preferred]
df = df[preferred + rest]

# =========================
# EXPORT
# =========================
df.to_csv(OUT_PATH, index=False, encoding="utf-8")

print("Exportado:", OUT_PATH)
print("Filas:", len(df), "| Columnas:", len(df.columns))
print("\nPrimeras filas:")
print(df.head())

print("\nInfo:")
print(df.info())
