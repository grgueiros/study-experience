# O coeficiente binomial, também chamado de número binomial, de um número n, na classe k,
# consiste no número de combinações de n termos, k a k.


def calcula_fatorial (numero):
    i = numero;
    resultado = 1;
    while(i > 0):
        resultado = resultado * i
        i -= 1;
    
    return resultado;

def calcula_coeficiente_binomial (n, k):
    return calcula_fatorial(n) / (calcula_fatorial(k) * calcula_fatorial(n - k))


n =  int(input('Digite o valor de n: '))
k =  int(input('Digite o valor de k: '))

print(calcula_coeficiente_binomial(n, k))