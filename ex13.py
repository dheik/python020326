def calculador(a,b,operacao):
    if operacao == "+":
        resultado = a + b
    elif operacao == "-":
        resultado = a - b
    elif operacao == "*":
        resultado = a * b
    elif operacao == "/":
        resultado = a / b
    else:
        resultado = "Operação inválida"
    return resultado

print(calculador(10, 5, "+"))
print(calculador(10, 5, "-"))
print(calculador(10, 5, "*"))
print(calculador(10, 5, "/"))