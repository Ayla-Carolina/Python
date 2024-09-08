'''
solicite 3 numeros e determine o maior entre eles



valores = []

#solicita 3 números e adiciona à lista 
for i in range(3):
    valor = int(input('Informe o valor {}: '.format(i+1)))
    
    valores.append(valor)

#encontra o maior da lista 
maior_valor = max(valores)

#verificando se são iguais
if maior_valor == valores[0] and maior_valor == valores[1] and maior_valor == valores[2]:
    print('Os valores são iguais.')
else:
    print(f'Maior valor = {maior_valor}')
'''
'''
i+1 no .format está inserindo um valor ao placeholder que é o valor que seria inserido nas {}
ou seja, com isso, será acrescentado 1 nela. como ela inicia vazia, vai iniciar como 1, dps 2 e no final do loop, 3'''

'''
calcule e apresente a quantiade de números pares e impares inseridos
incerre a leitura quando o usuário informar o valor 0
aceite apenas valores positivos

pares = 0
impares = 0

while True:
    valor = int(input('Digite um valor positivo (0 para sair): '))

    if valor == 0:
        break

    if valor < 0:
        print('Valor inválido. Digite um número positivo.')
        continue

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
'''

'''
receba 3 números e imprima eles em ordem crescente 
numero = []
for i in range(3):
  num = int(input('Digite um número: '))
  numero.append(num)

ordem_crescente = sorted(numero)
ordem_decrescente = sorted(numero, reverse=True)
print(f'Valores em ordem crescente: {ordem_crescente} \nDecrescente: {ordem_decrescente}')
'''

'''
informar o salario líquido com o desconto do imposto de renda 

salario_bruto = float(input('Salário bruto =  '))

if salario_bruto <= 1903.98:
  print(f'Você está isento de imposto de renda. Seu salário é = {salario_bruto}')

if 1903.99 >= salario_bruto <= 2826.65:
  imposto = salario_bruto - (salario_bruto * 0.075)
  print(f'Seu salário com o desconto do imposto de renda é = {imposto:.2f}')

if 2826.66 >= salario_bruto <= 3751.05:
  imposto = salario_bruto - (salario_bruto * 0.15)
  print(f'Seu salário com o desconto do imposto de renda é = {imposto:.2f}')

if 3751.06 >= salario_bruto <= 4664.68:
  imposto = salario_bruto - (salario_bruto * 0.225)
  print(f'Seu salário com o desconto do imposto de renda é = {imposto:.2f}')

if salario_bruto > 4664.68:
  imposto = salario_bruto - (salario_bruto * 0.275)
  print(f'Seu salário com o desconto do imposto de renda é = {imposto:.2f}')
  

'''