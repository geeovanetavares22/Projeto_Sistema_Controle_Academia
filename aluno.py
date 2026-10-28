class Aluno:
    def __init__(self, nome: str, cpf: str, telefone: str, data_nascimento: str, situacao_matricula: str = "Ativo"):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__situacao_matricula = situacao_matricula

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf
    
    def telefone(self):
        return self.__telefone

    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

    def data_nascimento(self):
        return self.__data_nascimento

    def situacao_matricula(self):
        return self.__situacao_matricula

    def situacao_matricula(self, nova_situacao: str):
        self.__situacao_matricula = nova_situacao