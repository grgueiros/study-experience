def eh_hipotenusa (numero):
    i = numero
    resultado = False
    while i > 1:
        j = numero     
        while j > 1 and resultado == False:
            if numero ** 2 == i**2 + j**2:
                resultado = True
            j -= 1
        i -= 1
    
    return resultado


def soma_hipotenusas (numero):
    soma = 0
    while numero >= 5:
        if eh_hipotenusa(numero):
            soma += numero
        numero-= 1

    return soma
