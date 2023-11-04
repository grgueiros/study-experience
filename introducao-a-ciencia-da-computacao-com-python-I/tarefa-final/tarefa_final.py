import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def palavras_do_texto(texto):
    sentencas = separa_sentencas(texto)
    palavras = []
    for sentenca in sentencas:
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                palavras.append(palavra)

    return palavras

def n_caracteres_da_sentenca(texto):
    sentencas = separa_sentencas(texto)
    soma = 0
    for sentenca in sentencas:
        soma += len(sentenca)
    
    return soma

def n_caracteres_da_frase(texto):
    sentencas = separa_sentencas(texto)
    soma = 0
    for sentenca in sentencas:
        for frase in separa_frases(sentenca):
            soma += len(frase)

    return soma

def n_caracteres(texto):
    palavras = palavras_do_texto(texto)
    soma = 0
    for palavra in palavras:
        soma += len(palavra)
    return soma

def calcula_tamanho_medio_de_palavra(texto):
    soma = n_caracteres(texto)
    return soma / len(palavras_do_texto(texto))

def n_frases(texto):
    sentencas = separa_sentencas(texto)
    soma_frases = 0
    for sentenca in sentencas:
        soma_frases += len(separa_frases(sentenca))
    return soma_frases

    

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    quantidade_de_tracos = len(as_a)
    
    lista_de_diferencas = []
    for i in range(quantidade_de_tracos):
        diferenca_absoluta = abs(as_a[i] - as_b[i])
        lista_de_diferencas.append(diferenca_absoluta)
    
    grau_similaridade = sum(lista_de_diferencas) / quantidade_de_tracos

    return grau_similaridade



def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    lista_palavras = palavras_do_texto(texto)
    total_palavras = len(lista_palavras)

    tamanho_medio_palavras = calcula_tamanho_medio_de_palavra(texto)
    relacao_type_token = n_palavras_diferentes(lista_palavras) / total_palavras
    razao_hapax_legomana = n_palavras_unicas(lista_palavras) / total_palavras
    tamanho_medio_sentenca = n_caracteres_da_sentenca(texto) / len(separa_sentencas(texto))
    complexidade_sentenca = n_frases(texto) / len(separa_sentencas(texto))
    tamanho_medio_frase = n_caracteres_da_frase(texto) / n_frases(texto)


    return [tamanho_medio_palavras, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]

    

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    mais_semelhante = textos[0]
    for indice in range(len(textos)):
        grau_similaridade_atual = compara_assinatura(calcula_assinatura(textos[indice]), ass_cp)
        grau_similaridade_mais_baixo = compara_assinatura(calcula_assinatura(mais_semelhante), ass_cp)

        if(grau_similaridade_atual < grau_similaridade_mais_baixo):
            mais_semelhante = textos[indice]

    return textos.index(mais_semelhante) + 1

