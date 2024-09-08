def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('Erro: Impossível dividir um valor por zero.')
    except TypeError as e:
        print(f'Erro: o tipo do dado informado está incorreto. Detalhes: {e}')
    else:
        print('Sem exceções.')


divisao(10, 'oi')