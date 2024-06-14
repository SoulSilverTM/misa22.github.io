print ("Cerradura: La suma de dos numeros reales siempre da como resultado otro numero real. ")
print ("A + B PERTENECE R")
print ()

print ("El siguiente programa realiza la propiedad de la cerradura. ")
print ()

num1 = float(input("Ingresa el primer numero \n"))
num2 = float(input("Ingresa el segundo numero \n"))
suma = num1 + num2 

if suma.is_integer():
    resultado = "Entero"
else:
    resultado = "Racional"

print("El resultado de la suma es: \n", suma)
print("El resultado es un numero \n", resultado)