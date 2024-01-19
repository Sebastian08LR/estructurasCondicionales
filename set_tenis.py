def get_set_winner(a, b):
    if a < 0 or b < 0:
        return "Resultado inválido"

    elif a == b:
        if a == 6:
            print(f"Set todavía no termina {a}-{b}")
        else:
            print(f"Set todavía no termina {a}-{b}")

    elif a == 6 and b >= 5:
        print(f"Jugador 1 ganó el set\n RESULTADO {a}-{b}")

    elif b == 6 and a >= 5:
        print(f"Jugador 2 ganó el set\n RESULTADO {b}-{a}")
    else:
        print("Resultado inválido")


a = int(input("Ingrese la cantidad de juegos ganados por el jugador numero 1: "))
b = int(input("Ingrese la cantidad de juegos ganados por el jugador numero 2: "))

print(get_set_winner(a, b))