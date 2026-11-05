import tkinter as tk
from tkinter import messagebox, simpledialog

from academia import Academia
from aluno import Aluno
from plano import Plano
from treino import Treino
from exercicio import Exercicio


class SistemaAcademia:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Gestão de Academia")
        self.janela.geometry("700x500")
        self.janela.resizable(False, False)

        # Cria a academia
        self.academia = Academia("Minha Academia")

        # Título
        titulo = tk.Label(
            janela,
            text="SISTEMA DE GESTÃO DE ACADEMIA",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            janela,
            text="Escolha uma opção abaixo",
            font=("Arial", 11)
        )
        subtitulo.pack(pady=5)

        # Área dos botões
        frame_botoes = tk.Frame(janela)
        frame_botoes.pack(pady=20)

        tk.Button(
            frame_botoes,
            text="Cadastrar Aluno",
            width=25,
            height=2,
            command=self.cadastrar_aluno
        ).grid(row=0, column=0, padx=10, pady=10)

        tk.Button(
            frame_botoes,
            text="Cadastrar Plano",
            width=25,
            height=2,
            command=self.cadastrar_plano
        ).grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            frame_botoes,
            text="Cadastrar Treino",
            width=25,
            height=2,
            command=self.cadastrar_treino
        ).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(
            frame_botoes,
            text="Listar Alunos",
            width=25,
            height=2,
            command=self.listar_alunos
        ).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(
            frame_botoes,
            text="Listar Planos",
            width=25,
            height=2,
            command=self.listar_planos
        ).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(
            frame_botoes,
            text="Listar Treinos",
            width=25,
            height=2,
            command=self.listar_treinos
        ).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(
            janela,
            text="Sair",
            width=20,
            command=self.janela.destroy
        ).pack(pady=10)

    # CADASTRAR ALUNO
    def cadastrar_aluno(self):
        nome = simpledialog.askstring(
            "Cadastrar Aluno",
            "Digite o nome do aluno:"
        )

        if not nome:
            return

        cpf = simpledialog.askstring(
            "Cadastrar Aluno",
            "Digite o CPF:"
        )

        if not cpf:
            return

        telefone = simpledialog.askstring(
            "Cadastrar Aluno",
            "Digite o telefone:"
        )

        if not telefone:
            return

        nascimento = simpledialog.askstring(
            "Cadastrar Aluno",
            "Digite a data de nascimento:"
        )

        if not nascimento:
            return

        aluno = Aluno(nome, cpf, telefone, nascimento)
        self.academia.cadastrar_aluno(aluno)

        messagebox.showinfo(
            "Sucesso",
            f"Aluno {nome} cadastrado com sucesso!"
        )

    # CADASTRAR PLANO
    def cadastrar_plano(self):
        nome = simpledialog.askstring(
            "Cadastrar Plano",
            "Digite o nome do plano:"
        )

        if not nome:
            return

        duracao = simpledialog.askinteger(
            "Cadastrar Plano",
            "Digite a duração em meses:"
        )

        if not duracao:
            return

        valor = simpledialog.askfloat(
            "Cadastrar Plano",
            "Digite o valor do plano:"
        )

        if valor is None:
            return

        plano = Plano(nome, duracao, valor)
        self.academia.cadastrar_plano(plano)

        messagebox.showinfo(
            "Sucesso",
            f"Plano {nome} cadastrado com sucesso!"
        )

    # CADASTRAR TREINO
    def cadastrar_treino(self):
        nome = simpledialog.askstring(
            "Cadastrar Treino",
            "Digite o nome do treino:"
        )

        if not nome:
            return

        objetivo = simpledialog.askstring(
            "Cadastrar Treino",
            "Digite o objetivo do treino:"
        )

        if not objetivo:
            return

        treino = Treino(nome, objetivo)

        while True:
            adicionar = messagebox.askyesno(
                "Exercícios",
                "Deseja adicionar um exercício?"
            )

            if not adicionar:
                break

            nome_ex = simpledialog.askstring(
                "Exercício",
                "Nome do exercício:"
            )

            if not nome_ex:
                continue

            series = simpledialog.askinteger(
                "Exercício",
                "Número de séries:"
            )

            repeticoes = simpledialog.askinteger(
                "Exercício",
                "Número de repetições:"
            )

            carga = simpledialog.askfloat(
                "Exercício",
                "Carga em kg:"
            )

            if (
                series is None
                or repeticoes is None
                or carga is None
            ):
                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os dados do exercício."
                )
                continue

            exercicio = Exercicio(
                nome_ex,
                series,
                repeticoes,
                carga
            )

            treino.adicionar_exercicio(exercicio)

        self.academia.cadastrar_treino(treino)

        messagebox.showinfo(
            "Sucesso",
            f"Treino {nome} cadastrado com sucesso!"
        )

    # LISTAR ALUNOS
    def listar_alunos(self):
        alunos = self.academia.listar_alunos()

        if not alunos:
            messagebox.showinfo(
                "Alunos",
                "Nenhum aluno cadastrado."
            )
            return

        texto = "ALUNOS CADASTRADOS\n\n"

        for aluno in alunos:
            status = (
                "Ativo"
                if aluno.get_matricula_ativa()
                else "Inativo"
            )

            texto += (
                f"Nome: {aluno.get_nome()}\n"
                f"CPF: {aluno.get_cpf()}\n"
                f"Telefone: {aluno.get_telefone()}\n"
                f"Matrícula: {status}\n\n"
            )

        messagebox.showinfo("Alunos", texto)

    # LISTAR PLANOS
    def listar_planos(self):
        planos = self.academia.listar_planos()

        if not planos:
            messagebox.showinfo(
                "Planos",
                "Nenhum plano cadastrado."
            )
            return

        texto = "PLANOS CADASTRADOS\n\n"

        for plano in planos:
            texto += (
                f"Plano: {plano.get_nome()}\n"
                f"Duração: {plano.get_duracao_meses()} meses\n"
                f"Valor: R$ {plano.get_valor():.2f}\n\n"
            )

        messagebox.showinfo("Planos", texto)

    # LISTAR TREINOS
    def listar_treinos(self):
        treinos = self.academia.listar_treinos()

        if not treinos:
            messagebox.showinfo(
                "Treinos",
                "Nenhum treino cadastrado."
            )
            return

        texto = "TREINOS CADASTRADOS\n\n"

        for treino in treinos:
            texto += (
                f"Treino: {treino.get_nome()}\n"
                f"Objetivo: {treino.get_objetivo()}\n"
            )

            exercicios = treino.get_exercicios()

            if not exercicios:
                texto += "Nenhum exercício cadastrado.\n"
            else:
                for exercicio in exercicios:
                    texto += (
                        f"• {exercicio.get_nome()} - "
                        f"{exercicio.get_series()} séries | "
                        f"{exercicio.get_repeticoes()} repetições | "
                        f"{exercicio.get_carga()} kg\n"
                    )

            texto += "\n"

        messagebox.showinfo("Treinos", texto)


# INICIAR O PROGRAMA
janela = tk.Tk()

app = SistemaAcademia(janela)

janela.mainloop()
