class Lata:
    def __init__(self, altura, diametro, volume, material='Aluminio', rotulo='Coca'):
        self.altura = altura
        self.diametro = diametro
        self.volume = volume
        self.material = material
        self.rotulo = rotulo
        self.lacre = True
        self.amassada = False
        self.descartada = False
        self.aberta = False

    def abrir(self):
        if self.aberta:
           print('A lata já está aberta')
        else:
            print('A lata foi aberta')
            self.aberta = True

    def beber(self, quantidade):
        if not self.aberta:
            print('Lata está fechada')
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume}ml, e ainda faltou {quantidade - self.volume}ml.')
            self.volume = 0
        else:
            self.volume -= quantidade
            print(f'Você bebeu {quantidade}ml, e na lata ainda resta {self.volume}ml.')

    def esvaziar(self):
        if not self.aberta:
            print('Abra a lata primeiro')
        else:
            print('Lata vazia')
            self.volume = 0

    def amassar(self):
        if not self.amassada and self.volume == 0:
            print('Lata amassada')
            self.amassada = True
        else:
            print('Não dá para amassar')

    def retirar_lacre(self):
        if self.lacre:
            self.lacre = False
            print('Lacre retirado')
        else:
            print('Não tinha lacre')

    def descartar(self):
        if self.descartada:
            print('Já foi descartada')
        elif self.amassada:
            print('Lata descartada no lixeiro amarelo')
            self.descartada = True
        else:
            print('Primeiro amasse a lata')


l1 = Lata(12.22, 5.2, 350)
l1.abrir()
l1.beber(200)
l1.esvaziar()
l1.amassar()
l1.retirar_lacre()
l1.descartar()