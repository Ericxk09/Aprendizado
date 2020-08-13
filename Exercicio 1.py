def main():

    print("Bem vindo ao jogo do NIM! ")
    print("1 - Para jogar apenas uma partida")
    print("2 - Para jogar um campeonato")
    print("")
    opcao = int(input("Escolha: "))
    
    while opcao < 1 or opcao > 2:
        print("")
        print("Opção Invalida")
        print("")
        opcao = int(input("Escolha: "))
    
    print("")

    if opcao == 1:
        partida()

    else:
        campeonato()
        
def computador_escolhe_jogada(n,m):
    """Estrategia vencedora é deixar sempre os multiplos de m+1 ao oponente.
    Caso isso não seja possível, deverá tirar o número máximo de peças
    possíveis. Devolve quantas peças o computador deve retirar do tabuleiro
    de acordo com a estrategia vencedora"""

    if n - m == 0:
        return m
    else:
        ##calculo do maior multiplo
        multiplo = (n // (m+1))*(m+1)
        
        ##definicao de pecas para Estrategia Vencedora
        ret_pecas = n - multiplo
        
        if m >= ret_pecas and ret_pecas > 0:
            return ret_pecas
        else:
            return m

def usuario_escolhe_jogada(n,m):
    """Solicita a jogada do jogador e verifica se o valor informado é
    válido. Se o valor for válido a função o devolve; caso contrario
    solicita um valor válido. """

    ret_pecas = int(input("Quantas peças você vai tirar? "))
    print("")
    while ret_pecas > n or ret_pecas > m or ret_pecas <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        print("")
        ret_pecas = int(input("Quantas peças você vai tirar? "))
        print("")
    m = ret_pecas
    return m
    
def partida():
    ##Inicia o jogo;
    ##Alterna as jogada
    ##Finaliza o jogo
    """A escolha da jogada inicial é de acordo com a estratégia vencedora;
    Cada jogada imprime o estado atual do jogo(quantas peças foram
    removidas na última jogada e quantas restam na mesa) 
    """
    user = pc = 0
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while n < 0 or m < 0 or  m > n:
        print("Numeros invalidos, tente novamente ")
        print("")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    print("")
    
    if n % (m+1) == 0:
        print("Você começa!")
        while n > 0:
            ##jogada User
            pecas_retiradas = usuario_escolhe_jogada(n,m)
            n = n - pecas_retiradas
            mensagens_user(n,pecas_retiradas)
            if n == 0:
                print("Fim do jogo! Voce ganhou! ")
                user += 1
                break
            ##jogada PC
            pecas_retiradas = computador_escolhe_jogada(n,m)
            n = n - pecas_retiradas
            mensagens_pc(n,pecas_retiradas)
            
            if n == 0:
                print("Fim do jogo! O computador ganhou! ")
                pc += 1
        
    else:
        print("Computador começa!")
        print("")
        while n > 0:
            ##jogada PC
            pecas_retiradas = computador_escolhe_jogada(n,m)
            n = n - pecas_retiradas
            mensagens_pc(n,pecas_retiradas)
            
            if n > 0:
                ##jogada User
                pecas_retiradas = usuario_escolhe_jogada(n,m)
                n = n - pecas_retiradas
                mensagens_user(n,pecas_retiradas)
                if n == 0:
                    print("Fim do jogo! Voce ganhou! ")
                    user += 1
                    break
            if n == 0:
                print("Fim do jogo! O computador ganhou! ")
                pc += 1
    print("")            
    return user,pc

def campeonato():
    """realiza três partidas seguidas do jogo e mostrar o placar
    dessas três partidas e, por fim, indica o vencedor do campeonato"""
    placar = []
    user = pc= 0
    for k in range(3):
        print(f'**** Rodada {k+1} ****')
        print()
        placar = partida()
        user = placar[0] + user
        pc = placar[1] + pc
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print(f'Placar: Você {user} X {pc} Computador')
          
def mensagens_user(n,pecas_retiradas):
    if pecas_retiradas == 1:
       print("Voce tirou uma peça.")
    else:
        print(f'Voce tirou {pecas_retiradas} peças. ')

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro")
        
    else:
        print(f'Agora restam {n} peças no tabuleiro')
    print("")
        
def mensagens_pc(n,pecas_retiradas):
    if pecas_retiradas == 1:
       print("O computador tirou uma peça.")
    else:
        print(f'O computador tirou {pecas_retiradas} peças. ')

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro")
        
    else:
        print(f'Agora restam {n} peças no tabuleiro')
    print("")

main()
