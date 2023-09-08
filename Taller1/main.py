import pandas as pd
import csv


# Función para cargar datos desde un archivo CSV a una lista
    def cargar_datos():
        try:
            column_names = ["Codigo", "Sexo", "Nombre", "Edad", "Ciudad"]
            df = pd.read_csv('chicos.csv', header=None, names=column_names, encoding='latin1')

            # Mapeo de ciudades y sexos
            city_mapping = {1: "Bucaramanga", 2: "Girón", 3: "Florida", 4: "Piedecuesta"}
            sex_mapping = {"F": "Femenino", "M": "Masculino"}

            df['Ciudad'] = df['Ciudad'].replace(city_mapping)
            df['Sexo'] = df['Sexo'].replace(sex_mapping)

            datos = df.values.tolist()
            print("Datos cargados con éxito desde chicos.csv")
            return datos
        except FileNotFoundError:
            print("El archivo chicos.csv no existe.")
            return []


# Función para mostrar los datos y realizar el informe especial
def informe_especial(datos):
    ciudades = {'Bucaramanga', 'Girón', 'Florida', 'Piedecuesta'}
    sexos = {'Femenino', 'Masculino'}
    edades_grupos = {
        'Grupo 1 (menores e iguales a 5 años)': lambda x: int(x) <= 5,
        'Grupo 2 (mayor a 5 y menor e igual a 10 años)': lambda x: 6 <= int(x) <= 10,
        'Grupo 3 (mayor a 10 años)': lambda x: int(x) > 10
    }

    total_ciudades = {ciudad: 0 for ciudad in ciudades}
    total_edades = {grupo: 0 for grupo in edades_grupos}

    for dato in datos:
        codigo, sexo, nombre, edad, ciudad = dato
        ciudad_actual = ciudad if ciudad in ciudades else 'Desconocida'
        sexo_actual = sexo if sexo in sexos else 'Desconocido'

        print(f"Código: {codigo}, Nombre: {nombre}, Sexo: {sexo_actual}, Edad: {edad}, Ciudad: {ciudad_actual}")

        total_ciudades[ciudad_actual] += 1
        for grupo, filtro in edades_grupos.items():
            if filtro(edad):
                total_edades[grupo] += 1

    total_registros = len(datos)

    print("\nInforme Especial:")
    print("Total de registros:", total_registros)
    print("\nTotales por Ciudad:")
    for ciudad, cantidad in total_ciudades.items():
        porcentaje = (cantidad / total_registros) * 100
        print(f"{ciudad}: {cantidad} ({porcentaje:.2f}%)")

    print("\nTotales por Grupo de Edad:")
    for grupo, cantidad in total_edades.items():
        print(f"{grupo}: {cantidad}")


# Resto del código (sin cambios)

# Función principal
def main():
    datos = cargar_datos()

    print("********************************")
    print("* Menú Principal *")
    print("* Equipo: XX Nombre: Tu nombre *")
    print("********************************")

    while True:
        print("\na. Cargar Datos")
        print("b. Informe Especial")
        print("c. Operaciones")
        print("d. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            datos = cargar_datos()
        elif opcion == 'b':
            if datos:
                informe_especial(datos)
            else:
                print("No hay datos cargados.")
        elif opcion == 'c':
            submenu_operaciones(datos)
        elif opcion == 'd':
            # Guardar los datos en el archivo chicos.csv
            with open('chicos.csv', 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                for dato in datos:
                    escritor_csv.writerow(dato)

            print("Datos guardados en chicos.csv")
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
