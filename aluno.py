from plano import Plano
from treino import Treino

class Aluno:
    def __init__(self, nome: str, cpf: str, telefone: str, data_nascimento: str, matricula_ativa: bool = True, plano: Plano = None):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__matricula_ativa = matricula_ativa
        self.__plano = plano
        self.__treinos = []

    def get_nome(self) -> str:
        return self.__nome

    def get_cpf(self) -> str:
        return self.__cpf
    
    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

    def get_data_nascimento(self) -> str:
        return self.__data_nascimento

    def get_matricula_ativa(self) -> bool:
        return self.__matricula_ativa

    def set_matricula_ativa(self, status: bool):
        self.__matricula_ativa = status

    def get_plano(self) -> Plano:
        return self.__plano

    def set_plano(self, novo_plano: Plano):
        self.__plano = novo_plano

    def atualizar_dados(self, telefone: str = None, matricula_ativa: bool = None, plano: Plano = None):
        if telefone:
            self.__telefone = telefone
        if matricula_ativa is not None:
            self.__matricula_ativa = matricula_ativa
        if plano:
            self.__plano = plano

    def verificar_matricula(self) -> bool:
        return self.__matricula_ativa

    def adicionar_treino(self, treino: Treino):
        self.__treinos.append(treino)

    def listar_treinos(self) -> list:
        return self.__treinos