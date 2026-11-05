from aluno import Aluno

class Pagamento:
    def __init__(self, valor: float, data: str, aluno: Aluno, pago: bool = False):
        self.__valor = valor
        self.__data = data
        self.__pago = pago
        self.__aluno = aluno

    def get_valor(self) -> float:
        return self.__valor

    def get_data(self) -> str:
        return self.__data

    def get_aluno(self) -> Aluno:
        return self.__aluno

    def get_pago(self) -> bool:
        return self.__pago

    def registrar_pagamento(self):
        self.__pago = True
        print(f"Pagamento de R$ {self.__valor:.2f} registrado com sucesso para {self.__aluno.get_nome()}.")

    def verificar_status(self) -> bool:
        return self.__pago