import math

a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

def sort_float(a, b):
    if(a > b):
        return [b, a] 
    return [a,b]

def extrai_raiz_positiva_com_soma (a, b, delta):
    return (-b + math.sqrt(delta)) / (2 * a)

def calcula_delta (a, b, c):
    return b ** 2 - (4*a*c);

def calcula_bhaskara (a,b,c):
    delta = calcula_delta(a,b,c)

    if( delta > 0):
        #calcula duas raízes
        primeira_raiz = extrai_raiz_positiva_com_soma(a,b,delta)
        segunda_raiz = (-b - math.sqrt(delta)) / (2 * a)

        raizes = sort_float(primeira_raiz, segunda_raiz)

        return "as raízes da equação são {} e {}".format(str(raizes[0]), str(raizes[1]))
        
    
    if(delta == 0):
        #calcula uma raíz
        raiz = extrai_raiz_positiva_com_soma(a,b,delta)
        return "a raiz desta equação é {}".format(str(raiz))

    return "esta equação não possui raízes reais"


resultado = calcula_bhaskara(a,b,c)
print(resultado)