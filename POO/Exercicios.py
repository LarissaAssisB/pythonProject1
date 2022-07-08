# Criar uma classe para uma lata de coca-cola.
# A classe deve ter todos os atributos dimensionais,
# e suas características de material.
# As funcionalidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre, e descartar
#
# class Coca:
#     def __init__(self, material, altura, diametro, ML , rotulo):
#         self.material = material
#         self.altura = altura
#         self.diametro = diametro
#         self.ML = ML
#         self.rotulo = rotulo
#
#     def __repr__(self):
#         return repr(f'{self.material} - {self.altura}mm - {self.diametro}d - {self.ML}ml - {self.rotulo}')
#
#     def abrir(self):
#         print('Lata aberta')
#
#     def beber(self):
#         print('Glub Glub')
#
#     def esvaziar(self):
#         print('Sem coca')
#
#     def amassar(self):
#         print('Pleft pleft')
#
#     def lacre(self):
#         print('Lacre removido')
#
#     def descartar(self):
#         print('Lata no lixo')
#
#
# cola = []
# for _ in range(1):
#     material = input('Digite o material: ')
#     altura = input('Digite a altura da coca: ')
#     diametro = input('Digite o diametro da coca: ')
#     ML = input('Digite ml a coca tem: ')
#     rotulo = input('Digite o tipo de rotulo da coca: ')
#     refri = Coca(material, altura, diametro, ML, rotulo)
#
#     cola.append(refri)
#
# print(repr(cola))
#
#======================================================================================

#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor
#
# class Bola:
#     def __init__(self, cor, circunferencia='Circunferência: 60', material='Material: plástico'):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
#
#     def trocar_cor(self, nova_cor):
#         self.cor = nova_cor
#         print(f'Sua nova cor é: {self.cor}')
#
#     def mostrar_cor(self):
#         print(f'Sua cor é: {self.cor}')
#
#
# b1 = Bola('Vermelha')
# b1.mostrar_cor()
# print(b1.circunferencia)
# print(b1.material)
# b1.trocar_cor('azul')
# b1.mostrar_cor()

#======================================================================================================================

# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
#
# class Quadrado:
#     def __init__(self, tamanho):
#         self.tamanho = tamanho
#
#     def retornar_tamanho(self):
#         print(f'O tamanho do quadrado é {self.tamanho}')
#
#     def mudar_tamanho(self, novo_tamanho):
#         self.tamanho = novo_tamanho
#         print(f'O tamanho atualizado do quadrado é: {novo_tamanho} ')
#
#     def calcular(self):
#         print(f'A aréa do seu quadrado é {self.tamanho + self.tamanho}')
#
#
# d1 = Quadrado(10)
# d1.retornar_tamanho()
# d1.mudar_tamanho(10)
# d1.calcular()

#=======================================================================================================================

# Classe Retangulo: Crie uma classe que modele um retângulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um
# local. Depois, deve-se criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés
# # necessários para o local
# piso = 2 , 2
# class Retangulo:
#
#     def __init__(self,comprimento, largura):
#         self.comprimento = comprimento
#         self.largura = largura
#
#     def mudar_valor_comprimento(self,novo_comprimento):
#         self.comprimento = novo_comprimento
#
#     def mudar_valor_largura(self, nova_largura):
#         self.largura = nova_largura
#
#     def retornar_valor_lados(self):
#         print(f'{self.comprimento}cm, {self.largura}cm')
#
#     def calcular_area(self):
#         area = self.largura * self.comprimento
#         print(f'Perimetro: {area}m quadrados')
#         return area
#
#     def calcular_perimetro(self):
#         perimetro = 2*self.largura + 2*self.comprimento
#         return perimetro
#
#     def quantidade_piso(self, area, qnt_piso):
#         qnt_piso = area // piso
#         print(f'VocÊ vai precisar de {qnt_piso}')
#
# x = float(input('selecione o comprimento do local:' ))
# y = float(input('selecione a largura do local:' ))
#
# local = Retangulo(x,y)
#
# print(f'Serão necessários {local.calcular_area()}m quadrado(s) de piso e {local.calcular_perimetro()}m de rodapés para suprir o local')

#====================================================================================================================================

# Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
# Possua uma classe chamada bomba_Combustível, com no mínimo esses atributos:
# tipo_Combustivel.
# valor_Litro
# quantidade_Combustivel
# Possua no mínimo esses métodos:
# abastecer_Por_Valor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_Por_Litro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterar_Valor( ) – altera o valor do litro do combustível.
# alterar_Combustivel( ) – altera o tipo do combustível.
# alterar_Quantidade_Combustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba


#
# class BombaCombustivel:
#     def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
#         self.tipoCombustivel = tipoCombustivel
#         self.valorLitro = valorLitro
#         self.quantidadeCombustivel = quantidadeCombustivel
#
#     def alterarValor(self, valorLitro):
#         self.valorLitro = valorLitro
#
#     def alterarCombustivel(self, tipoCombustivel):
#         self.tipoCombustivel = tipoCombustivel
#
#     def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
#         self.quantidadeCombustivel = quantidadeCombustivel
#
#     def abastecerPorValor(self, valor):
#         temp = valor/self.valorLitro
#         self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - temp)
#         return temp
#
#     def abastecerPorLitro(self, qtd):
#         temp2 = qtd * self.valorLitro
#         self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - qtd)
#         return temp2
#
#
# a1 = BombaCombustivel("Gasolina", 5, 500)
#
# print(a1.abastecerPorValor(150))
# print(a1.quantidadeCombustivel)
# print(a1.abastecerPorLitro(30))
# print(a1.quantidadeCombustivel)
#
#Exercício 05
# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
# (estômago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa
# ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3
# alimentos diferentes e verificando o conteúdo do estômago a cada refeição. Experimente fazer com
# que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def __repr__(self):
        return repr('Opps, encontrei outro macaco aqui')

    def comer(self, comida):
        if self.comer == m1 or self.comer == m2:
            print('CANIBAL')
        self.bucho.append(comida)

    def verBucho(self):
        print("Bucho: ", self.bucho)

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)


m1 = Macaco("Jonas")
m2 = Macaco("Reiter")
print('Macaco Jonas')
m1.comer("Maçã")
m1.verBucho()
m1.comer("Banana")
m1.verBucho()
m1.comer("Abacaxi")
m1.verBucho()
m1.digerir()
m1.verBucho()
print('Macaco Reiter')
m2.comer("Maca")
m2.comer("Banana")
m2.comer(m1)
m2.verBucho()

print(repr)