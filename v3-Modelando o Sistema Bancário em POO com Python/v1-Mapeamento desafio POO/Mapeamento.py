from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @staticmethod
    def realizar_transacao(conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self.limite_saques = 0
        self.limite = 500

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        numero_saques = 0
        if self.saldo < valor:
            print("Valor abaixo do saldo, por favor digite o valor corretamente para sacar!")

        elif numero_saques == self.limite_saques:
            print("Você já atingiu o limite de saque diário, por favor aguarde até o outro dia!")

        elif valor <= self.limite:
            numero_saques += 1
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito feito com sucesso!")
            return True

        else:
            print("Falha no depósito, tente novamente!")
            return False

class ContaCorrente(Conta, limite=500, limites=3):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.limite = 500
        self.limite_saques = 3

class Historico:
    def __init__(self):
        self._transacoes = ""

    def adicionar_transacao(self, transacao):
        self._transacoes = transacao

@abstractmethod
class Transacao(ABC):
    def valor(self):
        pass

    def registrar(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self):
        return "Depósito - Valor: ***.**"

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self):
        return "Saque - Valor: ***.**"
