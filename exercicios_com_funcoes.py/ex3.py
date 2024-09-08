'''
pergunte ao usuáro se ele deseja converter uma temperatura 
de grau Celsius para Fahrenheit ou vice-versa
Para cada opção crie uma função '''

'''
-----  versão 1 sem correções e melhorias ----
def celsius_para_fahrenheit(celsius):
    try:
        cels = int(input('Insira a temperatura: '))
        fahr = (cels * 9/5) + 32

        print(f'{cels} Graus Celsius é {fahr} Fahrenheit ')

    except TypeError:
        print('Insira apenas números.')
        return None

def fahrenheit(escolha_temp):
    try:
        fahr = int(input('Insira a temperatura: '))
        cels = (fahr - 32) * 5/9
        print(f'{fahr} Fahrenheit é {cels} Graus Celsius')

    except TypeError:
        print('Insira apenas números.')
        return None

escolha_temp = int(input('Você deseja converter qual temperatura: \nGraus Celsius para Fahrenheit (1) \nFahrenheit para Celsius (2) \nInsira 1 ou 2:'))

try:
    if escolha_temp == 1:
      graus_celsius(escolha_temp)

    elif escolha_temp == 2:
       fahrenheit(escolha_temp)


except ValueError:
    print('Insira apenas valores inteiros.')
'''

''' 
---- versão com melhorias 
'''
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
 
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#criando uma função principal para organizar o fluxo
#o while vai garantir que o usuário insira uma opção válida
#criação de uma terceira opcao para sair do programa...

def main():
    while True:
        try:
            escolha_temp = int(input('Você deseja converter qual temperatura? \n1. Graus Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n3. Sair\n'))

            if escolha_temp == 1:
                celsius = float(input('Insira a temperatura em Celsius: '))
                fahrenheit = celsius_para_fahrenheit(celsius)
                print(f'{celsius}°C equivalem a {fahrenheit}°F')
            elif escolha_temp == 2:
                fahrenheit = float(input('Insira a temperatura em Fahrenheit: '))
                celsius = fahrenheit_para_celsius(fahrenheit)
                print(f'{fahrenheit}°F equivalem a {celsius}°C')
            elif escolha_temp == 3:
                print('Saindo...')
                break
            else:
                print('Opção inválida. Insira 1, 2 ou 3.')
        except ValueError:
            print('Por favor, insira um número inteiro válido.')

if __name__ == "__main__":
    main()


