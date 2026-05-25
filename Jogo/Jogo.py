import random

def jogar():
    # 1. Definimos as opções disponíveis no jogo
    opcoes = ['pedra', 'papel', 'tesoura']

    print("=== Pedra, Papel e Tesoura ===")

    #2. Recebemos a escolha do jogador
    jogador = input("Escolha pedra, papel e tesoura: ").lower().strip()

    # Verificamos se o jogador digitou uma opção válida
    if jogador not in opcoes:
        print("Opções inválida! Digite exatamente pedra, papel ou tesoura.")
        return
    
    #3. O computador faz a sua escolha aleatoriamente
    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador.capitalize()}")
    print(f"Computador escolheu: {computador.capitalize()}")

    if jogador == computador:
        print("Resultado: Deu Empate! ")

    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
         print("Resultado: Você venceu!")
    else:
        print("Resultado: Você perdeu! O computador ganhou.")  


# Executa o jogo
jogar()

