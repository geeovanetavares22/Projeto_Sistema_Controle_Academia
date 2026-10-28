class Plano:
    def __init__(self, nome_plano: str, duracao_meses: int, valor: float):
        self.__nome_plano = nome_plano
        self.__duracao_meses = duracao_meses
        self.__valor = valor

    
    def nome_plano(self):
        return self.__nome_plano
    
    def duracao_meses(self):
        return self.__duracao_meses
  
    def valor(self):
        return self.__valor

    def valor(self, novo_valor: float):
        if novo_valor >= 0:
            self.__valor = novo_valor

