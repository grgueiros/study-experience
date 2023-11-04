entrada = int(input("Digite o valor de n: "))


def calcula_fatorial (numero):
    i = numero;
    resultado = 1;
    while(i > 0):
        resultado = resultado * i
        i -= 1;
    return resultado

print(calcula_fatorial(entrada))
    