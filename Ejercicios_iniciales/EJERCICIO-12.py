# Solicitar al usuario los valores del trapecio
lado = float(input("Ingrese la longitud de uno de los lados del trapecio: "))
base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
altura = float(input("Ingrese la altura del trapecio: "))

# Calcular el área del trapecio
area = ((base_mayor + base_menor) / 2) * altura

# Calcular el perímetro del trapecio
perimetro = base_menor + base_mayor + (2 * lado)

# Mostrar el área y el perímetro por pantalla
print(f"El área del trapecio es: {area}")
print(f"El perímetro del trapecio es: {perimetro}")
