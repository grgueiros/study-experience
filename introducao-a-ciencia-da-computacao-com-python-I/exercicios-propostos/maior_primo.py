def define_primo(numero):
    i = 31
    resultado = True
    while(i > 1):
        if numero % i == 0 and numero != i:
            resultado = False 
        i -= 1;

    return resultado

def maior_primo(referencial):
    eh_primo = define_primo(referencial)
    while(not eh_primo):
        referencial -= 1
        eh_primo = define_primo(referencial)

    return referencial