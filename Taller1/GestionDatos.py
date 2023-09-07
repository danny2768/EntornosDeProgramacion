import pandas as pd


class GestionDatos:
    def __init__(self):
        # This is the constructor.
        string = "Hi, this is GestionDatos"

    def cargar_datos(self):
        # We add the column names for the dataFrame.
        column_names = ["Codigo", "Sexo", "Nombre", "Edad", "Ciudad"]
        df = pd.read_csv('assets/chicos.csv', header=None, names=column_names, encoding='latin1')

        # The csv comes with numerical info for the cities and sex, we change it to strings.
        city_mapping = {1: "Bucaramanga", 2: "Girón", 3: "Florida", 4: "Piedecuesta"}
        sex_mapping = {"F": "Femenimo", "M": "Masculino"}

        df['Ciudad'] = df['Ciudad'].replace(city_mapping)
        df['Sexo'] = df['Sexo'].replace(sex_mapping)

