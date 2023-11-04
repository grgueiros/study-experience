entrada = None
lista_numeros = []
while(entrada != 0):
    print(entrada != 0)
    entrada = int(input('Digite um número inteiro positivo ou 0 para parar'))
    lista_numeros.append(entrada)

indice = len(lista_numeros) - 2
while indice >= 0:
    print(lista_numeros[indice])
    indice -= 1