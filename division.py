num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
div = num1/num2
rest = num1%num2

if div == int(div):
    print(f"----La división entre {num1} y {num2} es exacta----\n\t RESULTADO: {div}\n\t RESTO: {rest}")
else:
    print(f"----La división entre {num1} y {num2} no es exacta---- \n\t RESULTADO: {div}\n\t RESTO: {rest}")
    