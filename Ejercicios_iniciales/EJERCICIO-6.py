# Solicita al usuario ingresar cinco palabras
palabra_1 = input("Ingresa la primera palabra: ")
palabra_2 = input("Ingresa la segunda palabra: ")
palabra_3 = input("Ingresa la tercera palabra: ")
palabra_4 = input("Ingresa la cuarta palabra: ")
palabra_5 = input("Ingresa la quinta palabra: ")

# Crea la frase con las palabras separadas por comas
frase = f"{palabra_1}, {palabra_2}, {palabra_3}, {palabra_4}, {palabra_5}"

# Muestra la frase
print("La frase formada con las palabras es:")
print(frase)
# Muestra la frase inversa
fraseinversa=f"{palabra_5}, {palabra_4}, {palabra_3}, {palabra_2}, {palabra_1}"
print("La frase a la inversa formada con las palabras es:")
print(fraseinversa)
