#criando funções 

def soma(num1, num2): #definindo a função 
   
    calculo = num1 + num2
    print(f'O resultado da soma é {calculo}')


def subtracao(num1, num2):
    sub = 10-2
    print(f'O resultado da subtração é {sub}')
    

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))


soma(num1, num2) #chamada da função 
subtracao(num1, num2)

