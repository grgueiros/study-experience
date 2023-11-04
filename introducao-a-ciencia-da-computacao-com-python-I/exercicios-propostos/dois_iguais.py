adjacentes = False

entrada = input("Digite um número")
digitos = len(entrada)
i = 0
anterior = ''
while(i < digitos):
    if(entrada[i] == anterior):
        adjacentes = True
    anterior = entrada[i]
    i += 1

print("sim" if adjacentes else "não")
