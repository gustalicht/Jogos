import random


def jogar():
    print("*********************************")
    print("bem vindo ao jogo da Forca!")
    print("*********************************")

    palavra_secreta = random.choice(['tomate', 'banana', 'melancia', 'laranja', 'limao', 'teste', 'prato'])
    enforcou = False
    acertou = False

    letras_adivinhadas = []
    max_tentativas = 7

    while not enforcou and not acertou:
        print("jogando...")
        letra_jogador = input('Adivinhe uma letra: ').lower()

        if letra_jogador in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra_jogador in palavra_secreta:
            letras_adivinhadas.append(letra_jogador)
            print("Parabéns! Você acertou uma letra:", letras_adivinhadas)
        else:
            max_tentativas -= 1
            print('Letra não encontrada. Você tem mais', max_tentativas, 'tentativas.')

        if max_tentativas == 0:
            enforcou = True
        elif set(palavra_secreta) == set(letras_adivinhadas):
            acertou = True

        # Mostra a palavra com as letras adivinhadas pelo jogador
        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

    if acertou:
        print('Parabéns! Você adivinhou a palavra correta:', palavra_secreta)
    else:
        print('Que pena! Você perdeu. A palavra correta era:', palavra_secreta)

    print("fim do jogo!")


if __name__ == "__main__":
    jogar()
