from aluno import Aluno
from plano import Plano
from treino import Treino

class Academia:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__alunos = []
        self.__planos = []
        self.__treinos = []

    def get_nome(self):
        return self.__nome

    def cadastrar_aluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def cadastrar_plano(self, plano: Plano):
        self.__planos.append(plano)

    def cadastrar_treino(self, treino: Treino):
        self.__treinos.append(treino)

    def listar_alunos(self) -> list:
        return self.__alunos

    def listar_planos(self) -> list:
        return self.__planos

    def listar_treinos(self) -> list:
        return self.__treinos