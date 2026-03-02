def valida_senha(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tamanho_ok = len(senha) >= 8

    if tem_maiuscula and tem_numero and tamanho_ok:
        return "Senha válida"
    else:
        return "Senha inválida"
senha = input("Digite uma senha: ")
print(valida_senha(senha))