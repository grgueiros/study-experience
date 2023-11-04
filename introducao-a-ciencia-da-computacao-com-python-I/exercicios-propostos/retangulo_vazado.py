def imprime_retangulo ():

    largura = int(input('largura: '))
    altura = int(input('altura: '))

    i = 0
    while i < altura:
        j = 0
        while(j < largura):
            primeira_linha = i == 0
            primeira_coluna = j == 0

            ultima_linha = i == altura - 1
            ultima_coluna = j == largura - 1

            eh_borda = primeira_coluna or primeira_linha or ultima_linha or ultima_coluna
            print('#' if eh_borda else ' ', end="")
            j+=1
        print()
        i+=1


imprime_retangulo()