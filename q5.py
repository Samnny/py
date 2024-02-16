def inverter_string(s):
    inverted_string = ""
    for i in range(len(s) - 1, -1, -1):
        inverted_string += s[i]
    return inverted_string

original = input("Digite uma frase para inverter: ")
invertida = inverter_string(original)
print("String original:", original)
print("String invertida:", invertida)
