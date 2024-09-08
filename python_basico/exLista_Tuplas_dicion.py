'''
usando listas 
faça 5 perguntas sobre um crime 
telefonou para a vítima 
esteve no local do crime 
mora perto da vitima 
devia para a vitima 
ja trabalhou com a vitima 

emita uma classificação sobre a participação da pessoa no crime 

se ela responder positivamente a 2 questões ela deve ser classificada como suspeita 
3 e 4 como cumplice 
e 5 como assassino
senão ela é inocente


respostas = []

pergunta_1 = input('Você telefonou para a vítima pouco antes do crime? (Sim ou Não)')
respostas.append(pergunta_1)

pergunta_2 = input('Você esteve no local do crime? (Sim ou Não)')
respostas.append(pergunta_2)

pergunta_3 = input('Você mora perto da vítima? (Sim ou Não)')
respostas.append(pergunta_3)

pergunta_4 = input('Você devia algo para a vítima? (Sim ou Não)')
respostas.append(pergunta_4)

pergunta_5 = input('Você já trabalhou com a vítima? (Sim ou Não)')
respostas.append(pergunta_5)

#contando sim maiúsculos e minúsculos e somando o total de respostas sim 
qtd_total_sim = respostas.count('Sim'.lower())

if qtd_total_sim == 2:
    print('Suspeito.')
elif qtd_total_sim <= 4:
    print('Cúmplice.')
elif qtd_total_sim == 5:
    print('Assassino!')
else:
    print('Inocente')
'''

'''
peça quatro notas de 5 alunos
armazene numa lista a média de cada aluno
imprima o número de alunos com média maior ou igual a 7.0



notas = []
#lista vazia que armazena as notas dos alunos

#laço que itera 5 vezes = 5 alunos
for aluno in range(1, 6):
    #variável que vai inicializar sempre com 0 e toda vez que o loop começar de novo. 
    #para que não haja repetição de médias.
    soma_notas = 0
    
    #loop 4 vezes para 4 notas
    for i in range(4):
        nota_alunos = float(input(f'Digite a nota {i+1} do aluno {aluno}: '))

        #armazenando a soma das notas 
        soma_notas += nota_alunos

    #calculando a média 
    media = soma_notas / 4

    #adicionando a média calculada à lista 
    notas.append(media)
#aqui o loop começa novamente com o soma_notas = 0 e assim para os 5 alunos

#soma 1 em medias_maiores para cada nota em notas que for maior ou igual a 7
medias_maiores = sum(1 for nota in notas if nota >= 7.0)

print(f'O número de alunos com média maior ou igual a 7.0 é {medias_maiores}')
'''

'''
crie um dicionario representando um carrinho de compras 
adicione produtos = chave 
quantidades = valores
calcule o total do carrinho de compra 


carrinho = { }

carrinho['Arroz'] = 2
carrinho['Feijão'] = 5
carrinho['Carne'] = 7
carrinho['Oleo'] = 2
carrinho['Farinha'] = 4
carrinho['Milho'] = 4
carrinho['Ervilha'] = 2
carrinho['Tomate'] = 7

#para casos mais complexos

soma_carrinho = sum(valor for valor in carrinho.values())
print(f'Forma mais complexa = {soma_carrinho}')

#para casos mais simples e menores

total_carrinho = sum(carrinho.values())
print(f'Caso mais simples = {total_carrinho}')

'''

'''
dicionario representando contato com nome e telefone 
o usuario deve procurar um contato pelo nome 

contatos_telefone = {
    "João": 6576896543,
    "Ana": 6576896543,
    "Bianca": 6576896543,
    "Caio": 6576896543,
    "Bruno": 6576896543,
    "Carlos": 6576896543
}

busca = input('Qual contato você deseja buscar? ')

if busca.lower() in {nome.lower(): telefone for nome, telefone in contatos_telefone.items()}:
      print(f'Sua busca foi encontrada  \n{busca} : {contatos_telefone[busca]}')
else:
    print('Contato não encontrado.')
'''

'''
crie duas tuplas e concatene elas em uma só 

tupla1 = ('MARIA','jOANA')

tupla2 = ('Carlos', 'Pedro')

tuplas = tupla1 + tupla2

print(tuplas)
'''

'''
o usuário digita o seu nome 
em seguida mostra o nome dele de trás pra frente usando letras maiusculas '''

nome = input('Insira seu nome (pode ser letras maiúsculas ou minúsculas): ')

#utilizando o upper para converter as letras para maiusculas 
#usando o slice para inverter a string
#o : pega todos os elementos e o -1 diz para percorrer a string de trás pra frente 

nome_ao_contrario = nome.upper()[::-1]
print(nome_ao_contrario)