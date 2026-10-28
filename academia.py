class Academia:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__alunos = []
        self.__planos = []
        self.__pagamentos = []
        self.__treinos = []

    def cadastrar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def cadastrar_plano(self, plano):
        self.__planos.append(plano)

    def registrar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def cadastrar_treino(self, treino):
        self.__treinos.append(treino)
