class Conta:
    def __init__(self, agencia, conta, saldo=100.0):
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        self.ver_saldo()
        self.__mensagem()

    def ver_saldo(self):
        print(self.__saldo)

    def __mensagem(self):
        print('Bom dia, seu depósito foi atualizado.')

c1 = Conta(3365, '1234-5')
c1.depositar(200)


