print("El siguiente programa realiza la cerradura de la multiplicacion")
print()

num1 = float(input("Ingresa el primer numero \n"))
num2 = float(input("Ingresa el segundo numero \n"))
multi = num1 * num2 

if multi.is_integer():
    resultado = "Entero"
else:
    resultado = "Racional"

print("El resultad de la multiplicacion es: \n", multi)
print("el resultado es un numero \n", resultado)