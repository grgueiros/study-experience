def soma_digitos(numero):
    digitos = len(numero)
    i = 0
    soma = 0
    while i < digitos:
        soma += int(numero[i])
        i+=1

    return soma

entrada = input('digite um número')

print(soma_digitos(entrada))