##conceito de saída em python 
print('Teste de saída em python com print!')

'''
comentários longos 
teste
'''

# tipo inteiro int

numero = int(input('Digite um número: '))
print(numero)

# tipo float - com vírgula 

numero = float(input('Digite um número float: '))
print(numero)

#tipo string 

frase = input('Digite uma frase: ')
print(frase)

#operadores 
#incremento 
valor = 5
valor += 1
print(valor)


#decremento 
valor -= 1
print(valor)

# modos de formatação de mensagens 

print(f'o valor é {valor}')
print('Olá {}'.format(valor))


#determina 2 casas após a vírgula 
print(f'{valor:.2f}')

#utilizando o for como lanço de repetição 

frutas = ['Maçã', 'banana', 'Uva'] #declarando uma lista 

for i in frutas:
    print(i)