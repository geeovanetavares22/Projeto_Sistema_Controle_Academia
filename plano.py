class Plano:
    def __init__(self, nome: str, duracao_meses: int, valor: float):
        self.__nome = nome
        self.__duracao_meses = duracao_meses
        self.__valor = valor

    def get_nome(self):
        return self.__nome

    def get_duracao_meses(self):
        return self.__duracao_meses

    def get_valor(self):
        return self.__valor

    def set_valor(self, novo_valor: float):
        if novo_valor >= 0:
            self.__valor = novo_valor

    def calcular_valor_total(self) -> float:
        return self.__duracao_meses * self.__valor

    def exibir_dados(self):
        print(
            f"Plano: {self.__nome} | "
            f"Duração: {self.__duracao_meses} meses | "
            f"Valor: R$ {self.__valor:.2f} | "
            f"Total: R$ {self.calcular_valor_total():.2f}"
        )
