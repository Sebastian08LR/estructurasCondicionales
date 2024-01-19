print("-----BIENVENIDO A LA CALCULADORA----\n")
a = float(input("Ingrese un numero: "))
b = float(input("Ingrese un numero: "))

def sumar(a,b):
    suma = a + b
    print(f"{a} + {b} = {suma}")
    return suma

def resta(a,b):
    resta = a - b
    print(f"{a} - {b} = {resta}")
    return resta

def multiplicacion(a,b):
    multiplicacion = a * b
    print(f"{a} * {b} = {multiplicacion}")
    return multiplicacion

def division(a,b):
    division = a / b
    print(f"{a} / {b} = {division}")
    return division

def potencia(a,b):
    potencia = a ** b
    print(f"{a} ** {b} = {potencia}")
    return division


op = str(input("\n\t 1. + \n\t 2. - \n\t 3. * \n\t 4. / \n\t 5. **\nIngrese la operación que desea realizar: "))

if op == "+":
    sumar(a,b)
elif op == "-":
    resta(a,b)
elif op == "*":
    multiplicacion(a,b)
elif op == "/": 
    division(a,b)
elif op == "**":
    potencia(a,b)
else: 
    print("Elección inválida")
