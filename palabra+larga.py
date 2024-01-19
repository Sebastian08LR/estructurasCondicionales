word1 = str(input("Ingrese la primera palabra: "))
word2 = str(input("Ingrese la segunda palabra: "))


if len(word1) > len(word2):
    print(f"La  palabra '{word1}' es más larga que la palabra '{word2}'")
elif len(word2) > len(word1):
    print(f"La  palabra '{word2}' es más larga que la palabra '{word1}'")
else: 
     print("Ambas palabras son igual de largas")
    

