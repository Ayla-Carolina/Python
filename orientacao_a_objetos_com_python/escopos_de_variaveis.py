bebida = 'refrigerante'

def cardapio():
    global bebida #dessa forma, modificamos o valor da variável global/externa
    comida = 'hamburguer'
    bebida = 'suco' #sem a primeira linha a função estaria criando uma nova variável
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida: ', bebida)