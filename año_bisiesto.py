year = int(input("Ingrese un año: "))
div_year = year/4
div_year2 = year/400
def es_ultimo_ano_de_siglo(anio):
    """Devuelve True si el año dado es el último año de un siglo, y False en caso contrario."""
    return (anio % 100 == 0) and (anio != 0)

if (year < 1582) or (year > 2300):
    if (div_year) == int(div_year):
        print(f"El año {year} es un año bisiesto") 
    else: 
        print(f"El año {year} no es un año bisiesto")
else:
    if(div_year) == int(div_year) and es_ultimo_ano_de_siglo(year) == False:
        print(f"El año {year} es bisiesto")
    elif (div_year) == int(div_year) and es_ultimo_ano_de_siglo(year) == True:
        if(div_year2 == int(div_year2)):
            print(f"El año {year} es bisisesto")
        else:
            print(f"El año {year} no es bisisesto")
    else: 
        print(f"El año {year} no es bisiesto")
        
            
        
