# classe para um veículo

class Veiculo:
    def __init__(self, cor, porta, marca, modelo, ano):
        self.cor = cor
        self.porta = porta
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return repr(f'{self.marca} - {self.modelo} - {self.porta} - {self.cor} - {self.ano}')

    def ligar(self):
        print(f'Wrumm wrumm pro {self.modelo}')

    def desligar(self):
        print(f'Acabou wrumm wrumm pro {self.modelo}')


# v1 = Veiculo('Branco', 4, 'Audi', 'A4', 2005)
# v2 = Veiculo('Vermelho', 2, 'Volkswagen', 'Gol', 1992)
# print(v1.ano)
# print(v2.modelo)
# v2.ligar()
# v2.desligar()

veiculos = []
for _ in range(2):
    cor = input('Digite a cor: ')
    porta = input('Digite a quantidade de portas: ')
    marca = input('Digite a marca: ')
    modelo = input('Digite o modelo: ')
    ano = input('Digite o ano: ')
    cadastro = Veiculo(cor, porta, marca, modelo, ano)
    veiculos.append(cadastro)

print(repr(veiculos))

