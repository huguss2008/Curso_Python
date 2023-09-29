# Solicitar al usuario dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular el cociente y el resto de la división
cociente = num1 // num2
resto = num1 % num2

# Determinar si el dividendo es par o impar
if num1 % 2 == 0:
    resultado_dividendo = "par"
else:
    resultado_dividendo = "impar"

# Mostrar la información por pantalla
print(f"Cociente: {cociente}")
print(f"Resto: {resto}")
print(f"El dividendo {num1} es {resultado_dividendo}.")
