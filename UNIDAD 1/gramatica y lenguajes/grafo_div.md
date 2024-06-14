import matplotlib.pyplot as plt
# Este codigo crea un grafo dirigido con 4 variables 
# Primero creamos un grafo vacio }
grafo = {}

# Agregamos vertices al grafo 

grafo ["A"] = ["B", "C"]
grafo ["B"] = ["D"]
grafo ["C"] = ["D"]
grafo ["D"] = []

# Se imprimen los grafo s

print("grafo: ")
for vertice, adyacentes in grafo.items():
    print(f"{vertice} -> {adyacentes}")