def add_data_to_dict(user_data):
    # Pedir al usuario la información y agregarla al diccionario
    key = input("¿Qué dato deseas agregar? (nombre, edad, sexo, teléfono, correo electrónico): ").lower()
    value = input(f"Introduce el valor para {key}: ")
    
    # Añadir el dato al diccionario
    user_data[key] = value
    
    # Imprimir el contenido del diccionario
    print("\nContenido del diccionario actualizado:")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")
