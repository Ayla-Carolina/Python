# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self, cor="Preto", modelo="Corola"):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0 #velocidade inicial 
        self.velocidade_max = 220
        self.velocidade_min = 0

    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'{self.modelo} está ligado.')
        else:
            print(f'{self.modelo} já está ligado.')
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print(f'{self.modelo} agora está desligado.')
        else:
            print(f'{self.modelo} já está desligado.')

    def acelerar(self, incremento=10):
        if not self.ligado:
            print(f'{self.modelo} não é possível acelerar. Está desligado')
            return
        
        if self.velocidade < self.velocidade_max:
            self.velocidade += incremento
            print(f'{self.modelo} acelerou para {self.velocidade} km/h')
        
        else:
            self.velocidade = self.velocidade_max
            print(f'Velocidade máxima atingida.')

    def desacelerar(self, decremento=10):
        if not self.ligado:
            print(f'O carro está desligado.')
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= decremento
            print(f'{self.modelo} desacelerou para {self.velocidade} km/h')
        
        else:
            self.velocidade = self.velocidade_min
            print(f'O carro está parado.')

    def __str__(self) -> str:
        status = "ligado" if self.ligado else "desligado"
        return (f'Carro - Modelo: {self.modelo} - Cor: {self.cor} \n- Status: {status} - Velocidade: {self.velocidade} km/h')

# Crie uma instância da classe carro.
carro_estacionado = Carro()
carro_em_movimento = Carro(cor="Vermelho", modelo="Fiesta")


# Faça o carro "andar" utilizando os métodos da sua classe.
carro_em_movimento.ligar()
carro_em_movimento.acelerar()

print(carro_estacionado)
print(carro_em_movimento)
print()

# Faça o carro "parar" utilizando os métodos da sua classe.

carro_em_movimento.desacelerar()
print(carro_estacionado)
print(carro_em_movimento)
print()

for _ in range(5):
    carro_em_movimento.desacelerar()

print(carro_estacionado)
print(carro_em_movimento)
print()

#Desligando o carro 

carro_em_movimento.desligar()
carro_estacionado.desligar()
print(carro_estacionado)
print(carro_em_movimento)