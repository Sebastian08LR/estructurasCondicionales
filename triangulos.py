#inputs de los lados de los triangulos 
ladoA = float(input("Ingrese la longitud del lado A: "))
ladoB = float(input("Ingrese la longitud del lado B: "))
ladoC = float(input("Ingrese la longitud del lado C: "))
sum_lados = ladoA + ladoB + ladoC

if (ladoA > (ladoB + ladoC) or (ladoB > (ladoA + ladoC)) or ladoC > (ladoB + ladoA)):
   print("NO ES UN TRIANGULO VÁLIDO")
elif (ladoA == ladoB and ladoC != ladoA and ladoC != ladoB) or (ladoC == ladoB and ladoA != ladoB and ladoA != ladoC) or (ladoC == ladoA and ladoB != ladoA and ladoB != ladoC):
    print("El triangulo que ingresó es isoceles")
elif (ladoA == ladoB and ladoB == ladoC) and (ladoC == ladoA):
    print("El triangulo que ingresó es equilatero")
elif (ladoA != ladoB and ladoB != ladoC) and (ladoC != ladoA):
    print("El triangulo que ingresó es escaleno")
    
    
     