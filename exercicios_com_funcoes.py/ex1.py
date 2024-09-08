'''
crie uma função que necessite de tres argumentos
forneça a soma desses 3 argumentos '''

def soma(num1, num2, num3):
    '''
    Calculando a soma de 3 números.
    
    Args:
        num1 = int(input('Digite o valor 1: '))
        num2 = int(input('Digite o valor 2: '))
        num3 = int(input('Digite o valor 3: '))
    
    Returns:
        int: a soma dos 3 números
    '''

    try:
        soma = num1 + num2 + num3
        return soma
        #trata de um erro ao tentar fazer o cálculo com dados de tipos diferentes
    except TypeError:
        print('Insira apenas números inteiros.')

#obtendo os valores do usuário
try:
    num1 = int(input('Digite o valor 1: '))
    num2 = int(input('Digite o valor 2: '))
    num3 = int(input('Digite o valor 3: '))

#armazenando o resultado ele pode ser utilizado posteriormente
    resultado = soma(num1, num2, num3)
    print(f'A soma dos valores é = {resultado}')
#trata o erro quando o usuário insere um valor não numérico
except ValueError:
    print('Entrada inválida. Insira apenas valores inteiros.')

