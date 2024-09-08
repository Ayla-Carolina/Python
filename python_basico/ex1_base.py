#exercícios conceitos básicos de python

'''
peça dois números e realize as principais contas
'''
'''
num1 = int(input('Informe um valor inteiro: '))
num2 = int(input('Informe outro valor inteiro: '))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2 
div = num1 // num2

print(f'Soma: {soma} \nSubtração: {sub} \nMultiplicação: {multi} \nDivisão: {div}')
'''

'''
peça o ano de nascimento do usuário e calcule a idade atual

ano_nascimento = int(input('Informe o ano em que você nasceu: '))

idade_atual =  2024 - ano_nascimento

print(f'Você tem {idade_atual} anos de idade.')
'''

'''
peça a quantidade de km, tranforme em metros, centímetros e milímetros

qtd_km = float(input('Informa a distância em quilômetros: '))

metros = qtd_km * 1000
centimetros = qtd_km * 10000
milimetros = qtd_km * 1000000

print(f'Metros: {metros} \nCentímetros: {centimetros} \nMilímetros: {milimetros}')
'''

'''
calcule o tempo de viagem do mesmo percurso de avião, carro e ônibus 
avião = 600km/hr
carro = 100km/h
onibus = 80km/h


tempo_viagem = float(input('Informe o tempo de viagem em horas: '))

t_aviao = tempo_viagem * 600
t_carro = tempo_viagem * 100
t_onibus = tempo_viagem * 80 

print(f'O tempo de viagem em utilizando \ncarro = {t_carro:.0f} \navião = {t_aviao} \nônibus = {t_onibus}')
'''

'''
solicite o peso e kg e altura em metros
calcule o IMC = peso / altura x altura 


peso_kg = float(input('Informe o seu peso em kg: '))
altura_metros = float(input('Informe a sua altura: '))

IMC = peso_kg / (altura_metros * altura_metros)

print(IMC)
'''

'''
peça o valor da hora e o número de horas trabalhadas no mês
calcule o valor do mês inteiro 


val_hora = float(input('Informe quanto você ganha por hora: '))
num_horas_mes = int(input('Informe o número de horas trabalhadas no mês: '))


salario_mes = num_horas_mes * val_hora

print(f'O seu salário é de R${salario_mes} reais por mês.')
'''

'''
peça o numero de horas de exercício físico por semana 
calcule o total de calorias em um mês gastas
considere a média de 5 calorias por minuto de exercício


horas_semana = int(input('Informe o total de horas de exercício física na semana: '))

horas_para_minutos = horas_semana * 60 

total_calorias = horas_para_minutos * 5 

print(f'O total de calorias gastas por semana é de {total_calorias} calorias.')
'''

'''
variáveis aleatórias apenas para junção no retorno '''

nome_user = input('Informe seu nome: ')
idade = int(input('Informe a sua idade: '))
formacao = input('Informe seu nível de escolaridade: ')
cidade_facul = input('De onde é a sua faculdade?')
nome_curso = input('Qual o nome do seu curso? ')
cidade_natal = input('Qual é a cidade em que você mora? ')

print(f'Ficha técnica para o curso {nome_curso}:\nNome: {nome_user} \nIdade: {idade} \nNível de formação:{formacao} \nCidade do curso: {cidade_facul} \nNome do curso: {nome_curso} \nCidade Natal: {cidade_natal}')