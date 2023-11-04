placar_computador = 0
placar_usuario = 0

def eh_multiplo(referencia, numero ):
    return referencia % numero == 0

def computador_escolhe_jogada(n, m):
    quantidade_a_retirar = m

    i = 1
    while(i < m):
        if(eh_multiplo(n - i, m + 1)):
            quantidade_a_retirar = i
        i += 1
    
    eh_uma_peca = quantidade_a_retirar == 1
    print('O computador tirou {} {}.'.format('uma' if eh_uma_peca else quantidade_a_retirar, 'peça' if eh_uma_peca else 'peças' ))
    return quantidade_a_retirar

def usuario_escolhe_jogada(n, m):
    precisa_jogar_novamente = True
    entrada = None

    while(precisa_jogar_novamente):
        entrada = int(input('Quantas peças você vai tirar? '))
        precisa_jogar_novamente = entrada <= 0 or entrada > m or n - entrada < 0
        if(precisa_jogar_novamente):
            print('Oops! Jogada inválida! Tente de novo.')
    return entrada

def define_campeonato():
    return int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato ')) != 1

def partida():

    global placar_computador
    global placar_usuario

    quantidade_de_pecas = int(input('Quantas peças? '))
    limite_pecas = int(input('Limite de peças por jogada? '))

    restante_ideal = limite_pecas + 1
    vez_do_computador = True
    if(eh_multiplo(quantidade_de_pecas, restante_ideal)):
        vez_do_computador = False

    print("{} começa!\n".format("Computador" if vez_do_computador else "Você"))

    while(quantidade_de_pecas > 0):
        if(vez_do_computador):
            quantidade_de_pecas -= computador_escolhe_jogada(quantidade_de_pecas, limite_pecas)
        else:
            quantidade_de_pecas -= usuario_escolhe_jogada(quantidade_de_pecas, limite_pecas)

        vez_do_computador = not vez_do_computador
        
        if(quantidade_de_pecas > 0):
            print("Agora {} no tabuleiro.\n".format("resta apenas uma peça" if quantidade_de_pecas == 1 else "restam {} peças".format(quantidade_de_pecas)))

    print('{} ganhou!'.format('Você' if vez_do_computador else 'O computador'))
    
    if(vez_do_computador):
        placar_usuario += 1
        return;

    placar_computador += 1

def campeonato():
    i  = 0
    while(i < 3):
        print('\n**** Rodada {} ****\n'. format(i + 1))
        partida()
        i += 1
    
    print('**** Final do campeonato! ****\n\n')

    print('Placar:Você {} X {} Computador'.format(placar_usuario, placar_computador))


def main():
    print('\nBem-vindo ao jogo do NIM! Escolha:\n')

    eh_campeonato = define_campeonato()

    if(eh_campeonato):
        campeonato()
    
    partida()

main()



