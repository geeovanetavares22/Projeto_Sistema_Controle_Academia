class Pagamento:
    def __init__(self, valor: float, data: str, situacao: str = "Pendente"):
        self.__valor = valor
        self.__data = data
        self.__situacao = situacao

    def valor(self):
        return self.__valor

    def data(self):
        return self.__data

    def situacao(self):
        return self.__situacao

    def situacao(self, nova_situacao: str):
        self.__situacao = nova_situacao
