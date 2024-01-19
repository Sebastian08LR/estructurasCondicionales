caracter = input("Ingrese un caracter: ")

# Comprueba si el caracter es letra, número o ninguno de los dos
if caracter.isalpha():
    print(f"El caracter '{caracter}' es una letra.")
    # Comprueba si la letra es mayúscula o minúscula
    if caracter.isupper():
        print("La letra es mayúscula.")
    elif caracter.islower():
        print("La letra es minúscula.")
else:
    if caracter.isdigit():
        print(f"El caracter '{caracter}' es un número.")
    else:
        print(f"El caracter '{caracter}' no es letra ni número.")
    