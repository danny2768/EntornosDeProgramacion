import pandas as pd
import csv

# Funcion para cargar datos desde el archivo chicos.csv
def upload_data():
    try:
        column_names = ["Codigo", "Sexo", "Nombre", "Edad", "Ciudad"]
        df = pd.read_csv('chicos.csv', header=None, names=column_names, encoding='latin1')

        # Cambiamos los valores numericos de ciudad a string.
        city_mapping = {1: "Bucaramanga", 2: "Girón", 3: "Florida", 4: "Piedecuesta"}
        df['Ciudad'] = df['Ciudad'].replace(city_mapping)

        # Cambiamos las iniciales de sexo a string.
        sex_mapping = {"F": "Femenino", "M": "Masculino"}
        df['Sexo'] = df['Sexo'].replace(sex_mapping)

        print("Datos cargados con éxito desde chicos.csv")
    except FileNotFoundError:
        print("El archivo chicos.csv no existe.")
