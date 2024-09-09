'''
função chamada contar_vogais 
recebe uma string como parametro 
conte os números de vogais na string e retorne o total 
peça para inserir uma frase e use a função para contar vogais 
'''

def contar_vogais(frase):
    '''
    contar o número de vogais em uma frase
    returns:
    int = o número de vogais na frase 
       '''
    
    #criando um conjunto com as vogais
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    contador = 0 #vai armazenar o número de vogais encontradas

#o for vai iterar sobre cada elemento da frase
    for letra in frase:
        if letra in vogais: #verifica se o caractere atual está no conjunto e adiciona ao contador
            contador += 1
    return contador

#execução 
#recebendo a frase 
frase = input('Digite uma frase: ')
numero_vogais = contar_vogais(frase)
print(f'A frase tem {numero_vogais} vogais.')


