from exercicio import Exercicio

class Treino:
    def __init__(self, nome: str, objetivo: str):
        self.__nome = nome
        self.__objetivo = objetivo
        self.__exercicios = []

    def get_nome(self) -> str:
        return self.__nome

    def get_objetivo(self) -> str:
        return self.__objetivo

    def get_exercicios(self) -> list:
        return self.__exercicios

    def adicionar_exercicio(self, exercicio: Exercicio):
        self.__exercicios.append(exercicio)

    def remover_exercicio(self, nome: str):
        self.__exercicios = [e for e in self.__exercicios if e.get_nome() != nome]

    def exibir_treino(self):
        print(f"--- Treino: {self.__nome} | Objetivo: {self.__objetivo} ---")
        if not self.__exercicios:
            print("Nenhum exercício cadastrado.")
            return
        for i, exercicio in enumerate(self.__exercicios, 1):
            print(f"{i}.", end=" ")
            exercicio.exibir_exercicio()