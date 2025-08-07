from random import randint
tentativas_facil = tentativas_medio = tentativas_dificil = 11
chances = 0
nivel = ""
print("Bem-vindo ao Jogo de Adivinhação de Números!\nEstou pensando em um número entre 1 e 100.\n")
parar_o_jogo = -1
while not parar_o_jogo == 1:
    numero = randint(1,100)
    Dificuldade = 0
    while Dificuldade not in (1, 2, 3):
        Dificuldade = int(input("Por favor, selecione o nível de dificuldade:\n[1] - Fácil (10 tentativas)\n[2] - Médio (5 tentativas)\n[3] - Difícil (3 tentativas)\n\nDigite sua escolha: "))
    match Dificuldade:
        case 1:
            chances = 10
            nivel = "Fácil"
            print("Ótimo! Você selecionou a dificuldade fácil.")
        case 2:
            chances = 5
            nivel = "Médio"
            print("Ótimo! Você selecionou a dificuldade médio.")
        case 3:
            chances = 3
            nivel = "Difícil"
            print("Ótimo! Você selecionou a dificuldade difícil.")

    print("--"*12)
    for i in range(1, chances+1):
        print(" ")
        palpite = int(input("Qual o seu palpite? "))
        print(" ")
        if palpite == numero:
            print("Parabéns, você acertou o número!")
            match Dificuldade:
                case 1:
                    if i < tentativas_facil :
                        tentativas_facil = i
                        print(f"Parabéns! Você estabeleceu um novo recorde para o nível {nivel}: {tentativas_facil} tentativa(s)!")
                case 2:
                    if i < tentativas_medio:
                        tentativas_medio = i
                        print(f"Parabéns! Você estabeleceu um novo recorde para o nível {nivel}: {tentativas_medio} tentativa(s)!")
                case 3:
                    if i < tentativas_dificil:
                        tentativas_dificil = i
                        print(f"Parabéns! Você estabeleceu um novo recorde para o nível {nivel}: {tentativas_dificil} tentativa(s)!")
            break
        elif numero > palpite: 
            print("Incorreto! O número que estou pensando é maior que o seu palpite!")
        elif numero < palpite: 
            print("Incorreto! O número que estou pensando é menor que o seu palpite!")
    else:
        print(f"Suas tentativas acabaram e você perdeu o jogo! O número correto era {numero}. Boa sorte na próxima vez!")
        print("--"*12)
    print(tentativas_dificil, tentativas_facil, tentativas_medio)
    chances = 0
    print("--"*12)
    parar_o_jogo = -1 
    while parar_o_jogo not in (0,1):
        parar_o_jogo = int(input("Você deseja continuar o jogo? \n[0] - Sim\n[1] - Não\nQual a sua escolha? "))
print(f"O seu placar em cada dificuldade:")
if tentativas_facil == 11:
    print("Fácil: Você não jogou nessa dificuldade.")
else:
    print(f"Fácil: {tentativas_facil} tentativa(s)")

if tentativas_medio == 11:
    print("Você não jogou nessa dificuldade.")
else:
    print(f"Médio: {tentativas_medio} tentativa(s)")

if tentativas_dificil == 11:
    print("Você não jogou nessa dificuldade.")
else:
    print(f"Difícil: {tentativas_dificil} tentativa(s)")
print("--"*12, "\nObrigado por jogar!") 