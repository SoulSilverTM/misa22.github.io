import random
nombre = input("ingresa tu nombre ")
input = nombre 
saludos = [
    "Bienvenido " + input + " ¿Como estas? ",
    "Hola " + input + " ¿En que te puedo ayudar?",
    "Buenas tardes " + input + " ¿Como va tu dia?"
]
indice = random.randint(0, len(saludos)-1)
print(saludos[indice])
