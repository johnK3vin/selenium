import pandas as pd
import os

def lector_perfume():
    ruta_csv = os.path.abspath("data/perfumes_men_eliteperfumes.csv")
    producto = pd.read_csv(ruta_csv)
    print(producto.head())

def lector_precio():
    ruta_csv = os.path.abspath("data/perfumes_men_eliteperfumes.csv")
    producto = pd.read_csv(ruta_csv)

    price = producto['price']
    print(price.head())

lector_precio()