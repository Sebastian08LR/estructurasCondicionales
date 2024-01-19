import time
def calculate_age(cump_year, cump_month, cump_day):
    # conseguir la fecha actual
    now = time.localtime()

    # Calcular la edad
    age = now.tm_year - cump_year - 1

    # verificar si el cumpleaños del usuario ya ocurrió
    if now.tm_mon > cump_month or (now.tm_mon == cump_month and now.tm_mday >= cump_day):
        age += 1

    return age

# inputs de la fecha de nacimiento
cump_year = int(input("Ingrese su año de nacimiento: "))
cump_month = int(input("Ingrese su mes de nacimiento(1-12): "))
cump_day = int(input("Ingrese su día de nacimiento(1-31): "))

# 
print("Su edad es:", calculate_age(cump_year, cump_month, cump_day))