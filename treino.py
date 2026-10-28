class Treino:
    def __init__(self, nome_treino: str):
        self.__nome_treino = nome_treino
        self.__exercicios = [] ###lembrar de listar os exercios depois


    def nome_treino(self):
        return self.__nome_treino

    
    def exercicios(self):
        return self.__exercicios