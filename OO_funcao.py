
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo R$ {self.__saldo} do titular: {self.__titular}')
        
    def deposita(self, valor):
        self.__saldo += valor
        
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
        
    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        
    def transfere(self,valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular.title()
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod    
    def codigo_banco():
        return "001"



conta = Conta("123", "ricardo", "500,20", "1000,00")

print(conta.limite)
print(conta.saldo)
print(conta.extrato())
