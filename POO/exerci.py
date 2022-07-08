# class Retangulo:
#
#     def __init__(self, comprimento, largura, piso):
#         self.comprimento = comprimento
#         self.largura = largura
#         self.piso = piso
#
#     def mudar_valor_comprimento(self, novo_comprimento):
#         self.comprimento = novo_comprimento
#         print(f'Você tem {novo_comprimento} de comprimentos.')
#
#     def mudar_valor_largura(self, nova_largura):
#         self.largura = nova_largura
#         print(f'Você tem {nova_largura} de comprimentos.')
#
#     def retornar_valor_lados(self):
#         print(f'{self.comprimento}cm X {self.largura}cm')
#
#     def calcular_area(self):
#         area = self.largura * self.comprimento
#         print(f'Você tem {area}m de area.')
#
#     def calcular_perimetro(self):
#         perimetro = 2*self.largura + 2*self.comprimento
#         print(f'Você tem {perimetro} de perimetro.')
#
#     def quantidade_piso(self, piso=60):
#         piso = self.calcular_area // piso
#         print(f'Você precisa de {piso} pisos.')
#
#
# l1 = Retangulo(60, 80)
# l1.mudar_valor_comprimento(500)
# l1.mudar_valor_largura(600)
# l1.retornar_valor_lados()
# l1.calcular_area()
# l1.calcular_perimetro()
# l1.quantidade_piso(60)