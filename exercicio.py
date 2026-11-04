class Exercicio:
    def __init__(self, nome: str, series: int, repeticoes: int, carga: float):
        self.__nome = nome
        self.__series = series
        self.__repeticoes = repeticoes
        self.__carga = carga

    def get_nome(self):
        return self.__nome

    def get_series(self):
        return self.__series

    def get_repeticoes(self):
        return self.__repeticoes

    def get_carga(self):
        return self.__carga

    def alterar_prescricao(self, series: int, repeticoes: int, carga: float):
        self.__series = series
        self.__repeticoes = repeticoes
        self.__carga = carga

    def exibir_exercicio(self):
        print(f"Exercício: {self.__nome} | Séries: {self.__series} | Repetições: {self.__repeticoes} | Carga: {self.__carga}kg") 