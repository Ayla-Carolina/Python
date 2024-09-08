#praticando a tomada de decisão

'''
peça dois números e imprima o maior deles 

num1 = int(input('Insira o valor inteiro 1:'))
num2 = int(input('Insira o valor inteiro 2:'))

#verificando qual o maior entre eles 
if num1 > num2:
    print(num1)
else:
    print(num2)
'''
'''
pergunte o turno em que ele estuda
M - matutino 
V-vespertino 
N- noturno 
e imprima mensagens de cumprimento de acordo com o turno 


##turno = input('Em qual turno você estuda? \nM - Matutino \nV - Vespertino \nN - Noturno \nR=')

if turno == "M" or "m":
    print('Bom dia!')
elif turno == "V":
    print('Boa tarde!')
elif turno == "N":
    print('Boa noite!')
else:
    print('Resposta inválida! Por favor, siga as instruções.')
'''

'''
peça uma nota, de 0 a 10
mostre a msg caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido 

valor = int(input('Informe um valor de 0 a 10: '))

while True:
    valor = int(input('Informe um valor de 0 a 10: '))
    if 0 <= valor <= 10:
        print('Valor válido!') 
        break
    else:
        print('Valor inválido!')'''


'''
classifique um aluno com base em sua nota no exame 
solicite a nota de 0 a 10
se for maior ou igual a 7 - aprovado 
se não, reprovado 


nota_exame = float(input('Informe a nota do exame: \n'))

if nota_exame >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
'''


'''
solicite o comprimentos dos lados de um triangulo 
e classifique 
equilatero todos os lados iguais 
isosceles dois lados iguais 
escaleno todos os lados com medidas diferentes 


lado1 = float(input('Informe o valor do lado 1: '))
lado2 = float(input('Informe o valor do lado 2: '))
lado3 = float(input('Informe o valor do lado 3: '))

#verificando se formam um triangulo 

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print('Os valores informados não forma um triângulo.')

else:
    #classificando o triangulo 
    equilatero = lado1 == lado2 == lado3
    isosceles = (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)
    escaleno = not equilatero and not isosceles

    if equilatero:
        print('Triângulo equilátero.')
    if isosceles:
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno.')
'''

'''
solicite um login e senha
o programa deve permitir apenas se o usuário for admin e a senha admin123


while True:
    login = input('Informe o seu login: \n')
    senha = input('Informe a sua senha: \n')

    if (login == "admin") and (senha == "admin123"):
        print('Acesso concluído.')
        break
    else:
        print('Senha ou usuário incorretos. Informe novamente: \n')
'''

