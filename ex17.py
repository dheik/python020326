def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase: ")
print("Número de vogais na frase:", contar_vogais(frase))