import random


def jogar():
    print("*********************************")
    print("bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = ['tomate', 'banana', 'melancia', 'laranja', 'limao', 'teste', 'prato']
    palavra_secreta = random.choice(palavra_secreta)
    enforcou = False
    acertou = False
    #letras_adivinhadas = []
    #max_tentativas = 7
    #enquanto não enforcou e não acertou
    while(not enfrocou and not acertou):
        print("jogando...")
    # Pede ao jogador para adivinhar uma letra
    letra_jogador = input('Adivinhe uma letra: ').lower()

    while max_tentativas > 0 and '_' in letras_adivinhadas:
        # Mostra a palavra com as letras adivinhadas pelo jogador
        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

        # Verifica se a letra está na palavra e adiciona à lista de letras adivinhadas



    if letra_jogador in palavra_secreta:
        letras_adivinhadas.append(letra_jogador)
        print("Parabéns você acertou uma Letra ", letras_adivinhadas)
    else:
        max_tentativas -= 1
        print('Letra não encontrada. Você tem mais', max_tentativas, 'tentativas.')




    # Verifica se o jogador ganhou ou perdeu


    if '_' not in letras_adivinhadas:
        print('Parabéns! Você adivinhou a palavra correta: ', palavra_secreta)
    else:
        print('Que pena! Você perdeu. A palavra correta era', palavra_secreta)

    print("fim do jogo!")


if (__name__ == "__main__"):
    jogar()
