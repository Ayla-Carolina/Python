'''
Versão 1 - sem correções e melhorias 

leia quanto a pessoa tem de dinheiro na carteira 
calcule quanto poderia comprar de cada moeda estrangeira 
dólar americano = 4,91
peso argentino = 0,02
dolar australiano = 3,18 
dolar canadense = 3,64 
franco suiço = 0,42
euro = 5,36
libra esterlina = 6,21


#função para converter para dolar americano 
def dolar_americano(moeda_americana):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_americana = valor_carteira * 4.91
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_americana}')
        return moeda_americana
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para peso argentino
def peso_argentino(moeda_argentina ):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_argentina = valor_carteira * 0.02
        print(f'O valor {valor_carteira} convertido para Peso Argentino = {moeda_argentina}')
        return moeda_argentina
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para dolar australiano 
def dolar_australiano(moeda_australiana):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_australiana = valor_carteira * 3.18
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_australiana}')
        return  moeda_australiana
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para dolar canadense 
def dolar_canadense(moeda_canadense):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_canadense = valor_carteira * 3.64
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_canadense}')
        return moeda_canadense
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para franco suiço 
def franco_suico(moeda_suica):

    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_suica = valor_carteira * 0.42
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_suica}')
        return  moeda_suica
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para euro 
def euro( moeda_europeia):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_europeia = valor_carteira * 5.36
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_europeia}')
        return moeda_europeia
    
    except TypeError:
        print('Insira apenas números.')
        return None

#função para converter para euro 
def libra_esterlina(moeda_libra):
    #adicionando uma exceção para o caso do usuário inserir além de números 
    try:
        moeda_libra = valor_carteira * 6.21
        print(f'O valor {valor_carteira} convertido para Dólar Americano = {moeda_libra}')
        return moeda_libra
    
    except TypeError:
        print('Insira apenas números.')
        return None


valor_carteira = float(input('Informe quanto de dinheiro você possui na carteira: '))
dolar_americano(valor_carteira)
peso_argentino(valor_carteira)
dolar_australiano(valor_carteira)
dolar_canadense(valor_carteira)
franco_suico(valor_carteira)
euro(valor_carteira)
libra_esterlina(valor_carteira)

'''


'''
Versão 2 - com correções e melhorias no código geral 

'''

def converter_moeda(valor_carteira, moeda):
    '''
    Converte um valor para a moeda desejada 

    Args: 
    valor_carteira - float - valor em reais a ser convertido 
    moeda - str - código da moeda para conversão 

    Returns: 
    float - valor convertido ou none caso ocorra algum erro.

    '''
    #criando um dicionário para armazenar as taxas
    taxas_conversao = {
        'USD': 4.91,
        'ARS': 0.02,
        'AUD': 3.18,
        'CAD': 3.64,
        'CHF': 0.42,
        'EUR': 5.36,
        'GBP': 6.21
    }

    try:
        taxa = taxas_conversao[moeda]
        valor_convertido = valor_carteira * taxa
        print(f'O valor {valor_carteira:.2f} reais convertido para {moeda} é {valor_convertido:.2f}')
        return valor_convertido
    
    except KeyError:
        print(f'Moeda {moeda} inválida.')
    except TypeError:
        print('Por favor, insira um valor numérico positivo.')
        return None
    
#obtendo o valor da carteiro do usuário 
valor_carteira = float(input('Informa o quanto de dinheiro você possui na carteira: '))

#solicitando as moedas para conversão 
moedas = input('Informe as moedas para conversão (siglas, sem espaços e separadas por vírgula): ').upper().split(',')

#convertendo 
for moeda in moedas:
    converter_moeda(valor_carteira, moeda)