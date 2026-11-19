import tkinter as tk
from tkinter import messagebox, simpledialog

from academia import Academia
from aluno import Aluno
from plano import Plano
from treino import Treino
from exercicio import Exercicio


LARANJA = "#FF5A00"
PRETO = "#171717"
CINZA = "#252525"
FUNDO = "#F4F4F4"
BRANCO = "#FFFFFF"


class SistemaAcademia:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Magnata | Gestão da Academia")
        self.janela.geometry("950x600")
        self.janela.configure(bg=FUNDO)
        self.janela.resizable(False, False)

        self.academia = Academia("Magnata Academia")

       
        topo = tk.Frame(janela, bg=PRETO, height=75)
        topo.pack(fill="x")
        topo.pack_propagate(False)

        tk.Label(topo, text="MAGNATA", bg=PRETO, fg=LARANJA,
                 font=("Arial", 22, "bold")).pack(side="left", padx=25)

        tk.Label(topo, text="SISTEMA DE GESTÃO", bg=PRETO, fg=BRANCO,
                 font=("Arial", 10, "bold")).pack(side="right", padx=25)

        # MENU LATERAL
        corpo = tk.Frame(janela, bg=FUNDO)
        corpo.pack(fill="both", expand=True)

        menu = tk.Frame(corpo, bg=CINZA, width=220)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(menu, text="MENU", bg=CINZA, fg="#AAAAAA",
                 font=("Arial", 10, "bold")).pack(anchor="w", padx=25, pady=30)

        self.conteudo = tk.Frame(corpo, bg=FUNDO)
        self.conteudo.pack(side="left", fill="both", expand=True,
                           padx=28, pady=25)

       
        opcoes = [
            ("Início", self.inicio),
            ("Cadastrar Aluno", self.cadastrar_aluno),
            ("Cadastrar Plano", self.cadastrar_plano),
            ("Cadastrar Treino", self.cadastrar_treino),
            ("Listar Alunos", self.listar_alunos),
            ("Listar Planos", self.listar_planos),
            ("Listar Treinos", self.listar_treinos),
            ("Sair", self.janela.destroy)
        ]

        for nome, funcao in opcoes:
            tk.Button(menu, text=nome, command=funcao, bg=CINZA,
                      fg=BRANCO, activebackground=LARANJA,
                      activeforeground=BRANCO, relief="flat",
                      font=("Arial", 10, "bold"), anchor="w",
                      padx=25, pady=12, cursor="hand2").pack(fill="x")

        tk.Label(menu, text="Controle simples e\norganizado da academia",
                 bg=CINZA, fg="#AAAAAA", font=("Arial", 9),
                 justify="left").pack(side="bottom", anchor="w",
                                      padx=25, pady=25)

        self.inicio()

    # FUNÇÕES VISUAIS
    def limpar(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    def titulo(self, texto):
        tk.Label(self.conteudo, text=texto, bg=FUNDO, fg=PRETO,
                 font=("Arial", 22, "bold")).pack(anchor="w", pady=(0, 15))

    def botao(self, texto, funcao):
        tk.Button(self.conteudo, text=texto, command=funcao,
                  bg=LARANJA, fg=BRANCO, relief="flat",
                  font=("Arial", 10, "bold"), padx=15,
                  pady=8, cursor="hand2").pack(anchor="w", pady=7)

    
    def inicio(self):
        self.limpar()
        self.titulo("Bem-vindo!")

        tk.Label(self.conteudo,
                 text="Gerencie alunos, planos e treinos da sua academia.",
                 bg=FUNDO, fg="#666666").pack(anchor="w")

        cards = tk.Frame(self.conteudo, bg=FUNDO)
        cards.pack(fill="x", pady=30)

        dados = [
            ("ALUNOS", len(self.academia.listar_alunos())),
            ("PLANOS", len(self.academia.listar_planos())),
            ("TREINOS", len(self.academia.listar_treinos()))
        ]

        for nome, quantidade in dados:
            card = tk.Frame(cards, bg=BRANCO, padx=25, pady=20,
                            highlightbackground="#DDDDDD",
                            highlightthickness=1)
            card.pack(side="left", fill="both", expand=True, padx=(0, 12))

            tk.Label(card, text=nome, bg=BRANCO, fg="#777777",
                     font=("Arial", 10, "bold")).pack(anchor="w")

            tk.Label(card, text=quantidade, bg=BRANCO, fg=LARANJA,
                     font=("Arial", 26, "bold")).pack(anchor="w")

        tk.Label(self.conteudo, text="Acesso rápido",
                 bg=FUNDO, fg=PRETO,
                 font=("Arial", 15, "bold")).pack(anchor="w", pady=10)

        for texto, funcao in [
            ("Cadastrar aluno", self.cadastrar_aluno),
            ("Cadastrar plano", self.cadastrar_plano),
            ("Cadastrar treino", self.cadastrar_treino)
        ]:
            self.botao(texto, funcao)

    
    def cadastrar_aluno(self):
        nome = simpledialog.askstring("Aluno", "Nome do aluno:")
        if not nome:
            return

        cpf = simpledialog.askstring("Aluno", "CPF:")
        telefone = simpledialog.askstring("Aluno", "Telefone:")
        nascimento = simpledialog.askstring("Aluno", "Data de nascimento:")

        if not all([cpf, telefone, nascimento]):
            return

        self.academia.cadastrar_aluno(
            Aluno(nome, cpf, telefone, nascimento)
        )

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        self.inicio()

    # CADASTRAR PLANO
    def cadastrar_plano(self):
        nome = simpledialog.askstring("Plano", "Nome do plano:")
        if not nome:
            return

        duracao = simpledialog.askinteger("Plano", "Duração em meses:")
        valor = simpledialog.askfloat("Plano", "Valor mensal (R$):")

        if duracao is None or valor is None:
            return

        if duracao <= 0 or valor < 0:
            messagebox.showerror("Erro", "Informe valores válidos.")
            return

        self.academia.cadastrar_plano(Plano(nome, duracao, valor))

        messagebox.showinfo("Sucesso", "Plano cadastrado com sucesso!")
        self.inicio()

    
    def cadastrar_treino(self):
        alunos = self.academia.listar_alunos()

        if not alunos:
            messagebox.showwarning("Atenção", "Cadastre um aluno primeiro.")
            return

        
        lista = "\n".join(
            f"{i + 1} - {a.get_nome()}"
            for i, a in enumerate(alunos)
        )

        escolha = simpledialog.askinteger(
            "Selecionar aluno",
            f"Escolha o número do aluno:\n\n{lista}"
        )

        if escolha is None:
            return

        if escolha < 1 or escolha > len(alunos):
            messagebox.showerror("Erro", "Aluno inválido.")
            return

        aluno = alunos[escolha - 1]

        
        nome = simpledialog.askstring("Treino", "Nome do treino:")
        if not nome:
            return

        objetivo = simpledialog.askstring("Treino", "Objetivo do treino:")
        if not objetivo:
            return

        treino = Treino(nome, objetivo)

        
        while messagebox.askyesno("Exercícios", "Deseja adicionar um exercício?"):

            nome_ex = simpledialog.askstring("Exercício", "Nome:")
            if not nome_ex:
                continue

            series = simpledialog.askinteger("Exercício", "Número de séries:")
            repeticoes = simpledialog.askinteger("Exercício", "Repetições:")
            carga = simpledialog.askfloat("Exercício", "Carga em kg:")

            if series is None or repeticoes is None or carga is None:
                messagebox.showwarning("Atenção", "Dados incompletos.")
                continue

            if series <= 0 or repeticoes <= 0 or carga < 0:
                messagebox.showerror("Erro", "Informe valores válidos.")
                continue

            treino.adicionar_exercicio(
                Exercicio(nome_ex, series, repeticoes, carga)
            )

        
        aluno.adicionar_treino(treino)

        # CADASTRA O TREINO NA ACADEMIA
        self.academia.cadastrar_treino(treino)

        messagebox.showinfo(
            "Sucesso",
            f"Treino cadastrado para o aluno {aluno.get_nome()}!"
        )

        self.inicio()

    
    def listar_alunos(self):
        alunos = self.academia.listar_alunos()
        texto = "ALUNOS CADASTRADOS\n\n"

        for a in alunos:
            status = "Ativo" if a.get_matricula_ativa() else "Inativo"

            texto += (
                f"Nome: {a.get_nome()}\n"
                f"CPF: {a.get_cpf()}\n"
                f"Telefone: {a.get_telefone()}\n"
                f"Matrícula: {status}\n"
            )

            treinos = a.listar_treinos()
            texto += "Treinos:\n"

            texto += "\n".join(
                f" - {t.get_nome()}" for t in treinos
            ) if treinos else " Nenhum treino cadastrado."

            texto += "\n\n"

        messagebox.showinfo(
            "Alunos",
            texto if alunos else "Nenhum aluno cadastrado."
        )

    
    def listar_planos(self):
        planos = self.academia.listar_planos()
        texto = "PLANOS CADASTRADOS\n\n"

        for p in planos:
            texto += (
                f"Plano: {p.get_nome()}\n"
                f"Duração: {p.get_duracao_meses()} meses\n"
                f"Valor: R$ {p.get_valor():.2f}\n"
                f"Total: R$ {p.calcular_valor_total():.2f}\n\n"
            )

        messagebox.showinfo(
            "Planos",
            texto if planos else "Nenhum plano cadastrado."
        )

    
    def listar_treinos(self):
        treinos = self.academia.listar_treinos()
        alunos = self.academia.listar_alunos()
        texto = "TREINOS CADASTRADOS\n\n"

        for t in treinos:
            aluno = next(
                (a for a in alunos if t in a.listar_treinos()),
                None
            )

            texto += (
                f"Aluno: {aluno.get_nome() if aluno else 'Não vinculado'}\n"
                f"Treino: {t.get_nome()}\n"
                f"Objetivo: {t.get_objetivo()}\n"
                "Exercícios:\n"
            )

            exercicios = t.get_exercicios()

            for e in exercicios:
                texto += (
                    f"- {e.get_nome()} | {e.get_series()} séries | "
                    f"{e.get_repeticoes()} repetições | {e.get_carga()} kg\n"
                )

            if not exercicios:
                texto += "Nenhum exercício cadastrado.\n"

            texto += "\n"

        messagebox.showinfo(
            "Treinos",
            texto if treinos else "Nenhum treino cadastrado."
        )



janela = tk.Tk()
app = SistemaAcademia(janela)
janela.mainloop()
