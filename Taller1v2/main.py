import pandas as pd
from IPython.display import display


# Funcion para cargar datos desde el archivo chicos.csv
def upload_data():
    try:
        column_names = ["Codigo", "Sexo", "Nombre", "Edad", "Ciudad"]
        df = pd.read_csv('chicos.csv', header=None, names=column_names, encoding='latin1')

        print("Datos cargados con éxito desde chicos.csv\n")
        display(df)
        return df
    except FileNotFoundError:
        print("El archivo chicos.csv no existe.")
        return None


def detailed_report(df):
    if df is not None:
        # Cambiamos los valores numericos de ciudad a string.
        city_mapping = {1: "Bucaramanga", 2: "Giron", 3: "Florida", 4: "Piedecuesta"}
        df['Ciudad'] = df['Ciudad'].replace(city_mapping)

        # Cambiamos las iniciales de sexo a string.
        sex_mapping = {"F": "Femenino", "M": "Masculino"}
        df['Sexo'] = df['Sexo'].replace(sex_mapping)

        display(df)

        # Calculamos los totales por ciudad
        city_totals = df['Ciudad'].value_counts()
        total_participants = len(df)

        # Calculamos porcentaje de participación por ciudad
        city_percentages = (city_totals / total_participants) * 100

        # Mostramos los totales y porcentajes por ciudad
        city_summary = pd.DataFrame({
            'Ciudad': city_totals.index,
            'Total': city_totals.values,
            '% Participación': city_percentages.values
        })

        print("\nTotales y Porcentajes por Ciudad:")
        display(city_summary)

        # Calculamos el número de chicos en cada grupo de edad
        # Grupo 1: menores e iguales a 5 años.
        # Grupo 2: mayor a 5 y menor e igual a 10 años.
        # Grupo 3: mayor a 10 años.

        age_group_counts = {
            'Grupo 1': len(df[df['Edad'] <= 5]),
            'Grupo 2': len(df[(df['Edad'] > 5) & (df['Edad'] <= 10)]),
            'Grupo 3': len(df[df['Edad'] > 10])
        }

        # Mostramos el numero de chicos por grupo de edad
        age_group_summary = pd.DataFrame({
            'Grupo de Edad': age_group_counts.keys(),
            'Número de Chicos': age_group_counts.values()
        })

        print("\nNúmero de Chicos por Grupo de Edad:")
        display(age_group_summary)
    else:
        print("Por favor cargue el archivo chicos.csv")


def add_record(df):
    print("A continuación se le pedirán los datos requeridos para el nuevo registro: ")

    name = validate_name()
    code = validate_code()
    sex = validate_sex()
    age = validate_age()
    city = validate_city()

    new_record = {
        'Codigo': code,
        'Sexo': sex,
        'Nombre': name,
        'Edad': age,
        'Ciudad': city
    }
    # Agregar el nuevo registro al DataFrame
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)

    print("\nArchivo actualizado con exito:\n")
    display(df)

    return df


def edit_record(df):
    print("\nRegistros actuales:")
    display(df)

    code_to_edit = input("Por favor ingrese el codigo del registro que desea editar: ")
    code_to_edit = int(code_to_edit)

    if code_to_edit in df['Codigo'].values:
        print("\nRegistro antes de la modificación:")
        display(df[df['Codigo'] == code_to_edit])

        new_name = validate_name()
        new_sex = validate_sex()
        new_age = validate_age()
        new_city = validate_city()

        df.loc[df['Codigo'] == code_to_edit, 'Nombre'] = new_name
        df.loc[df['Codigo'] == code_to_edit, 'Sexo'] = new_sex
        df.loc[df['Codigo'] == code_to_edit, 'Edad'] = new_age
        df.loc[df['Codigo'] == code_to_edit, 'Ciudad'] = new_city

        print("\nRegistro actualizado con éxito:\n")
        display(df)
    else:
        print("El código ingresado no existe en los registros.")

    return df


def delete_record(df):
    print("\nRegistros actuales:")
    display(df)

    code_to_delete = input("Por favor ingrese el código del registro que desea eliminar: ")
    code_to_delete = int(code_to_delete)

    if code_to_delete in df['Codigo'].values:
        df = df[df['Codigo'] != code_to_delete]
        print("\nRegistro eliminado con éxito:\n")
        display(df)
    else:
        print("El código ingresado no existe en los registros.")

    return df


def save_and_exit(df):
    while True:
        save_choice = input("\n¿Desea guardar las operaciones realizadas en 'chicosModified.csv'? (Sí/No): ").lower()
        if save_choice in ["si", "sí"]:
            df.to_csv('chicosModified.csv', index=False)
            print("Operaciones guardadas con éxito en 'chicosModified.csv'.")
            break
        elif save_choice == 'no':
            print("Operaciones no guardadas.")
            break
        else:
            print("Respuesta no válida. Por favor, responda 'Sí' o 'No'.")


def validate_age():
    while True:
        try:
            age = int(input("Ingrese la nueva edad: "))
            if 0 <= age <= 150:
                break
            else:
                print("La edad debe estar entre 0 y 150.")
        except ValueError:
            print("Por favor, ingrese una edad válida (número entero).")
    return age


def validate_city():
    while True:
        try:
            city = int(
                input("Ingrese la nueva ciudad (1: Bucaramanga, 2: Giron, 3: Florida, 4: Piedecuesta): "))
            if 1 <= city <= 4:
                break
            else:
                print("La ciudad debe ser un número entre 1 y 4.")
        except ValueError:
            print("Por favor, ingrese una ciudad válida (número entero).")
    return city


def validate_sex():
    while True:
        sex = input("\nPor favor ingrese el sexo (F o M): ")
        if sex in ["F", "f", "M", "m"]:
            break
        else:
            print("Opción no válida. Por favor, ingrese 'F' o 'M'.")
    return sex


def validate_code():
    while True:
        try:
            code = int(input("\nPor favor ingrese el codigo: "))
            break
        except ValueError:
            print("El código debe ser un número entero.")
    return code


def validate_name():
    while True:
        name = input("\nPor favor ingrese el nombre: ")
        if not any(char.isdigit() for char in name):
            break
        else:
            print("El nombre no puede contener números.")
    return name


def main():
    df = None
    while True:
        print("\n********************************")
        print("* Menú Principal *")
        print("* Nombre: Daniel Cobos *")
        print("********************************")
        print("* a. Cargar Datos. *")
        print("* b. Informe Especial. *")
        print("* c. Operaciones *")
        print("* d. Salir *")
        print("********************************")

        choice = input("Seleccione una opción (a/b/c/d): ").lower()

        if choice == 'a':
            df = upload_data()
        elif choice == 'b':
            detailed_report(df)
        elif choice == 'c':
            while True:
                print("\n********************************")
                print("* Menú de Operaciones *")
                print("********************************")
                print("* 1. Agregar Registro *")
                print("* 2. Editar Registro *")
                print("* 3. Eliminar Registro *")
                print("* 4. Volver al Menú Principal *")
                print("********************************")

                operation_choice = input("Seleccione una opción (1/2/3/4): ")

                if operation_choice == '1':
                    df = add_record(df)
                elif operation_choice == '2':
                    df = edit_record(df)
                elif operation_choice == '3':
                    df = delete_record(df)
                elif operation_choice == '4':
                    break
                else:
                    print("Opción no válida.")
        elif choice == 'd':
            save_and_exit(df)
            break
        else:
            print("Opción no válida. Por favor, seleccione a, b, c o d.")


if __name__ == "__main__":
    main()
