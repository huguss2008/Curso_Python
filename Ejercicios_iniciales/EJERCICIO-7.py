# Solicitar al usuario dos números
var_1=int(input("introduce un número"))
var_2=int(input("introduce un número"))

# Operaciones/Calculos

totalsuma=var_1+var_2
totalresta=var_1-var_2
totalproducto=var_1*var_2
totaldivisión=var_1/var_2
totalpotencia=var_1**var_2
totalresto=var_1%var_2
totalredondeo=var_1//var_2
totaldivisionredondeada=round(totaldivisión,2)

# Mostrar resultados por pantalla

print("El total de tu suma",totalsuma)
print("El total de tu resta",totalresta)
print("El total de tu producto",totalproducto)
print("El total de tu división",totaldivisionredondeada)
print("El total de tu potencia",totalpotencia)
print("El total de tu resto",totalresto)
print("El total de tu redondeo",totalredondeo)

