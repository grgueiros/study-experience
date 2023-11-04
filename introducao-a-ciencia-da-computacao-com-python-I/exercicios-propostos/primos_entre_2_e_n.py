def eh_primo(numero):
    fator = 2
    resultado = True    
    while resultado and fator <= numero/2:
        if numero % fator == 0:
            resultado = False
        fator += 1
    
    return resultado



def n_primos (numero):
    i = 2
    quantidade_primos = 0
    while i <= numero:
        if eh_primo(i):
            quantidade_primos += 1
        i += 1
    return quantidade_primos