# Procedimiento que se realiza mediante un ciclo la organización de los datos al igual que lo hace la función "sorted()"
def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
#bubble_sort(numeros) 

# Pedimos al usuario que ingrese los números separados por espacios
entrada_usuario = input("Ingrese los números que desea ordenar (separados por espacios): ")

# Convertimos la entrada en una lista de números
numeros = [int(num) for num in entrada_usuario.split()]
 
#Llamamos a la función sorted() e imprimos el resultado dentro de un print() 
sorted(numeros)

# Mostramos la lista ordenada

print("\t ---LISTA ORDENADA--- ")
print(f"\n\t{sorted(numeros)}")
