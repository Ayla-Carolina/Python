'''
reverso de um número 
função que retorne o reverso de um número inteiro informado
ex.: 127 = 721'''

def reverso(valor):
    """Inverte os dígitos de um número inteiro.

    Args:
        valor (int): O número a ser invertido.

    Returns:
        int: O número invertido.
    """
    try:

    #convertendo para str, invertendo e convertendo de volta para int
        valor_str = str(valor)
        valor_invertido_str = valor_str[::-1]
        valor_invertido = int(valor_invertido_str)
        return valor_invertido

    except TypeError:
        print('Insira apenas valores números.')
    return None

try:
    valor = int(input('Digite um valor: '))

    resultado = reverso(valor)

    if resultado is not None:
        print(f'O valor {valor} ao contrário é {resultado}')

except ValueError:
    print('Insira apenas valores inteiros.')