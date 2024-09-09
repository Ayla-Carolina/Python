import random

'''
jogo da forca 
o programa deve escolher aleatoriamente uma palavra secreta de uma lista predefinida 
a palavra será apresentada por espaços em branco 
um para cada letra 
o jogador terá um número limitado de 6 tentativas
a cada tentativ ele fornece uma letra 
se ela estiver na palavra, ela será revelada nas posições correspondentes
se não, exibe uma mensagem de erro 
depois de um  número máximo de erros, o jogador perde
ele continua até que o jogador adivinhe a palavra ou exceda o número de tentativas
importe uma biblioteca para o exercício '''


#função para o jogo da forca
def jogo_forca():

    #lista com as palavras para serem escolhidas aleatoriamente
    palavras = ['python', 'programação', 'tecnologia']

    #variavel para armazenar a palavra escolhida
    palavra_secreta = random.choice(palavras)

#inicialmente, a lista vai conter apenas _, mas ela será atualizada quando uma letra for acertada
    letras_certas = ['_' for letra in palavra_secreta]

    #lista para armazenar as letras erradas
    letras_erradas = []

    #contador
    tentativas = 6

#enquanto o jogador tiver tentativas e houver letras com _, o loop vai rodar
    while tentativas > 0 and '_' in letras_certas:

        #imprime a palavra atualizada
        print('Palavra: ', ' '.join(letras_certas))
        chute = input('Digite uma letra: ').lower()

#verifica se a letra já foi digitada antes ou se ela está na palavra
        if chute in letras_certas or chute in letras_erradas:
            print('Você já tentou essa letra.')
#se ela estiver na palavra, atualiza as listas de acordo com as tentativas
        elif chute in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_certas[i] = chute 

#se estiver errada, diminui uma tentativa
        else:
            letras_erradas.append(chute)
            tentativas -= 1
            print('Letra incorreta.')

        print('Letras erradas: ', letras_erradas)

#se não houver nenhum _ mais, a palavra foi descoberta e o jogador venceu 
    if '_' not in letras_certas:
        print('Parabés, você venceu!')
    else:
        print('Você perdeu. A palavra era: ', palavra_secreta)

jogo_forca()