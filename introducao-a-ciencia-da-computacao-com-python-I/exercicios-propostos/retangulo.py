def imprime_retangulo ():

    largura = int(input('largura: '))
    altura = int(input('altura: '))

    i = 0
    while i < altura:
        j = 0
        while j < largura:
            print('#', end="")
            j += 1
        print()
        i += 1


imprime_retangulo()