import random 

palavras = ['python', 'programacao', 'computador', 'aula', 'variavel']

palavra_sorteada = random.choice(palavras)

palavra_escondida = '-' * len(palavra_sorteada)

letras_adivinhadas = []

max_tentativas = 6

while True:
    print(palavra_escondida)

    letra = input('Digite uma letra: ')

    if letra in letras_adivinhadas:
        print('você já digitou essa letra')
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_sorteada:
        lista = []
        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        palavra_escondida = ''.join(lista)

    else:
        max_tentativas -= 1
        print(f'letra n encontrada. Vc tem mais {max_tentativas} tentativas')

    if palavra_escondida == palavra_sorteada:
        print('Parabénssssss, você ganhou!!!')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu. A palavra era {palavra_sorteada}.')
        break