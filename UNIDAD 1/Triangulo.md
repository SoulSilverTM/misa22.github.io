import math


def calcular_lado_faltante():
    print("Introduce los valores de dos lados de un triangulo rectangulo")
    print("deja en blanco el valor del lado que se deseas")

a = input("lado a (cateto): ")
b = input("lado b (cateto): ")
c = input("lado c (hipotenusa): ")

#convertir las entradas a numeros

a = float(a) if a else None
b = float(b) if b else None
c = float(c) if c else None

#calcula el lado faltante usando el teorema de pitagoras 

if a is None and b is not None and c is not None:
    a = math.sqrt(c**2 - b**2)
    lado_calculado = "a (cateto)"
elif b is None and a is not None and c is not None:
    b = math.sqrt(c**2 - a**2)
    lado_calculado = "b (cateto)"
elif c is None and a is not None and b is not None:
    c = math.sqrt(a**2 + b**2)
    lado_calculado = "c (hipotenusa)"
    else:
    return "Error: debe proporcionar exactamente dos lados."
    
return f"El lado faltante es {lado_calculado} y su valor es: {a if
    lado_calculado == 'a (cateto)' else b if lado_calculado == 'b (cateto)' else c:.2f}"

resultado = calcular_lado_faltante()
print(resultado)