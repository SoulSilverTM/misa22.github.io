# Se explica la concatenacion
print("Esta parte del codigo muestra como se logra hacer una concatenacion:\n")
letras = "Eres el numero"
numeros = "1"
resultado = letras + " " + numeros

print(resultado)

print("Esta parte del codigo muestra como se hace la produccion en un lenguaje formal")

def replace_letters_with_numbers(input_string):
    letter_to_number_map = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10',
        'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
        'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }
    output_string = ""
    for char in input_string:
        if char.isalpha():
            output_string += letter_to_number_map[char.lower()]
        else:
            output_string += char
    return output_string

input_string = "Hello, World!"
output_string = replace_letters_with_numbers(input_string)
print(output_string)  