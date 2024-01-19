# IMC(Indice de Masa Corporal)
peso = float(input("Por favor, Ingrese su peso en Kg: "))
altura = float(input("Por favor, Ingrese su altura en Metros: "))

imc = peso / (altura**2) # los dos (**) significan potenciacion
if imc < 18.5:
    resultado = "Bajo peso"
elif imc < 25:
    resultado = "Un peso adecuado"
else: 
    resultado = "Sobre peso"

print(f"Su IMC es {imc:.1f}. Usted tiene {resultado}.")     