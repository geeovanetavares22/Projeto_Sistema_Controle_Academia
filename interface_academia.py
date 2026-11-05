import tkinter as tk
from tkinter import ttk, messagebox
from academia import Academia
from aluno import Aluno
from plano import Plano
from treino import Treino
from exercicio import Exercicio

LARANJA, LARANJA_ESCURO, PRETO, CINZA, FUNDO, BRANCO, TEXTO = (
    "#FF5A00", "#E64D00", "#171717", "#242424", "#F4F4F4", "#FFFFFF", "#252525"
)

class AcademiaApp:
    def __init__(self, root):
        self.root, self.academia = root, Academia("Academia Magneta")
        root.title("Academia Magneta | Gestão da Academia")
        root.geometry("1050x680")
        root.minsize(900, 600)
        root.configure(bg=FUNDO)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=BRANCO, foreground=TEXTO, fieldbackground=BRANCO, rowheight=30, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background=PRETO, foreground=BRANCO, font=("Segoe UI", 10, "bold"), padding=8)
        style.map("Treeview", background=[("selected", "#FFD5C2")], foreground=[("selected", PRETO)])

        topo = tk.Frame(root, bg=PRETO, height=75)
        topo.pack(fill="x")
        topo.pack_propagate(False)
        tk.Label(topo, text=" MAGNATA", bg=PRETO, fg=LARANJA, font=("Segoe UI", 21, "bold")).pack(side="left", padx=28)
        tk.Label(topo, text="SISTEMA DE GESTÃO", bg=PRETO, fg=BRANCO, font=("Segoe UI", 10, "bold")).pack(side="right", padx=28)

        principal = tk.Frame(root, bg=FUNDO)
        principal.pack(fill="both", expand=True)
        menu = tk.Frame(principal, bg=CINZA, width=220)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(menu, text="MENU", bg=CINZA, fg="#AAAAAA", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=22, pady=(28, 15))
        for nome in ("Início", "Alunos", "Planos", "Treinos"):
            tk.Button(menu, text=nome, command=lambda p=nome: self.mostrar_pagina(p), bg=CINZA, fg=BRANCO,
                      activebackground=LARANJA, activeforeground=BRANCO, relief="flat", bd=0, anchor="w",
                      padx=22, pady=13, font=("Segoe UI", 11, "bold"), cursor="hand2").pack(fill="x", padx=8, pady=3)

        tk.Label(menu, text="Desempenho Magnata", bg=CINZA, fg="#AAAAAA", font=("Segoe UI", 9), justify="left").pack(side="bottom", anchor="w", padx=22, pady=25)

        self.conteudo = tk.Frame(principal, bg=FUNDO)
        self.conteudo.pack(side="left", fill="both", expand=True, padx=28, pady=25)
        self.mostrar_pagina("Início")

    def titulo(self, t, sub):
        tk.Label(self.conteudo, text=t, bg=FUNDO, fg=PRETO, font=("Segoe UI", 23, "bold")).pack(anchor="w")
        tk.Label(self.conteudo, text=sub, bg=FUNDO, fg="#666666", font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 20))

    def botao(self, parent, txt, cmd):
        return tk.Button(parent, text=txt, command=cmd, bg=LARANJA, fg=BRANCO, activebackground=LARANJA_ESCURO,
                         activeforeground=BRANCO, relief="flat", bd=0, padx=16, pady=9, font=("Segoe UI", 10, "bold"), cursor="hand2")

    def tabela(self, cols, titulos):
        t = ttk.Treeview(self.conteudo, columns=cols, show="headings", height=9)
        for c, tit in zip(cols, titulos):
            t.heading(c, text=tit); t.column(c, width=150, anchor="w")
        t.pack(fill="both", expand=True)
        return t

    def mostrar_pagina(self, pagina):
        for w in self.conteudo.winfo_children(): w.destroy()
        n_alunos, n_planos, n_treinos = len(self.academia.listar_alunos()), len(self.academia.listar_planos()), len(self.academia.listar_treinos())

        if pagina == "Início":
            self.titulo("Bem-vindo!", "Gerencie alunos, planos e treinos da sua academia.")
            resumo = tk.Frame(self.conteudo, bg=FUNDO); resumo.pack(fill="x", pady=10)
            for leg, qtd in [("ALUNOS", n_alunos), ("PLANOS", n_planos), ("TREINOS", n_treinos)]:
                card = tk.Frame(resumo, bg=BRANCO, padx=22, pady=22, highlightthickness=1, highlightbackground="#E2E2E2")
                card.pack(side="left", fill="x", expand=True, padx=(0, 14))
                tk.Label(card, text=leg, bg=BRANCO, fg="#777777", font=("Segoe UI", 10, "bold")).pack(anchor="w")
                tk.Label(card, text=str(qtd), bg=BRANCO, fg=LARANJA, font=("Segoe UI", 28, "bold")).pack(anchor="w", pady=(5, 0))

            tk.Label(self.conteudo, text="Acesso rápido", bg=FUNDO, fg=PRETO, font=("Segoe UI", 15, "bold")).pack(anchor="w", pady=(35, 12))
            acoes = tk.Frame(self.conteudo, bg=FUNDO); acoes.pack(anchor="w")
            for nome, p in [("Cadastrar aluno", "Alunos"), ("Cadastrar plano", "Planos"), ("Cadastrar treino", "Treinos")]:
                self.botao(acoes, nome, lambda pag=p: self.mostrar_pagina(pag)).pack(side="left", padx=(0, 10))

        elif pagina == "Alunos":
            self.titulo(f"Alunos ({n_alunos} cadastrados)", "Cadastre e consulte os alunos.")
            form = tk.Frame(self.conteudo, bg=BRANCO, padx=18, pady=15); form.pack(fill="x", pady=(0, 18))
            ents = {}
            for i, c in enumerate(["Nome", "CPF", "Telefone", "Nascimento (DD/MM/AAAA)"]):
                tk.Label(form, text=c, bg=BRANCO, fg=TEXTO, font=("Segoe UI", 9, "bold")).grid(row=(i//2)*2, column=(i%2)*2, sticky="w", padx=(0, 8), pady=(4, 2))
                e = ttk.Entry(form, width=30); e.grid(row=(i//2)*2+1, column=(i%2)*2, sticky="ew", padx=(0, 22), pady=(0, 9)); ents[c] = e
            form.columnconfigure((0, 2), weight=1)
            tb = self.tabela(("nome", "cpf", "telefone", "status"), ("Nome", "CPF", "Telefone", "Matrícula"))

            def att():
                tb.delete(*tb.get_children())
                for a in self.academia.listar_alunos(): tb.insert("", "end", values=(a.get_nome(), a.get_cpf(), a.get_telefone(), "Ativa" if a.get_matricula_ativa() else "Inativa"))

            def cad():
                vals = [e.get().strip() for e in ents.values()]
                if not all(vals): return messagebox.showwarning("Atenção", "Preencha todos os campos.")
                self.academia.cadastrar_aluno(Aluno(*vals))
                for e in ents.values(): e.delete(0, tk.END)
                self.mostrar_pagina("Alunos")
                messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

            self.botao(form, "Cadastrar aluno", cad).grid(row=4, column=0, columnspan=4, sticky="w", pady=(5, 0))
            att()

        elif pagina == "Planos":
            self.titulo(f"Planos ({n_planos} cadastrados)", "Cadastre e consulte os planos disponíveis.")
            form = tk.Frame(self.conteudo, bg=BRANCO, padx=18, pady=18); form.pack(fill="x", pady=(0, 18))
            tk.Label(form, text="Nome do plano", bg=BRANCO).grid(row=0, column=0, sticky="w")
            nome = ttk.Combobox(form, values=("BASIC", "VIP"), state="readonly", width=22); nome.grid(row=1, column=0, padx=(0, 15), pady=7, sticky="ew"); nome.current(0)
            tk.Label(form, text="Duração (meses)", bg=BRANCO).grid(row=0, column=1, sticky="w")
            duracao = ttk.Entry(form, width=18); duracao.grid(row=1, column=1, padx=(0, 15), pady=7, sticky="ew")
            tk.Label(form, text="Valor mensal (R$)", bg=BRANCO).grid(row=0, column=2, sticky="w")
            valor = ttk.Entry(form, width=18); valor.grid(row=1, column=2, pady=7, sticky="ew")
            tb = self.tabela(("nome", "duracao", "valor", "total"), ("Plano", "Duração", "Valor mensal", "Valor total"))

            def att():
                tb.delete(*tb.get_children())
                for p in self.academia.listar_planos(): tb.insert("", "end", values=(p.get_nome(), f"{p.get_duracao_meses()} meses", f"R$ {p.get_valor():.2f}", f"R$ {p.calcular_valor_total():.2f}"))

            def cad():
                try:
                    meses, preco = int(duracao.get()), float(valor.get().replace(",", "."))
                    if meses <= 0 or preco < 0: raise ValueError
                except ValueError: return messagebox.showerror("Dados inválidos", "Informe uma duração positiva e um valor numérico válido.")
                self.academia.cadastrar_plano(Plano(nome.get(), meses, preco))
                self.mostrar_pagina("Planos")
                messagebox.showinfo("Sucesso", "Plano cadastrado com sucesso!")

            self.botao(form, "Cadastrar plano", cad).grid(row=2, column=0, columnspan=3, sticky="w", pady=(8, 0))
            att()

        elif pagina == "Treinos":
            self.titulo(f"Treinos ({n_treinos} cadastrados)", "Cadastre treinos e seus exercícios.")
            form = tk.Frame(self.conteudo, bg=BRANCO, padx=18, pady=15); form.pack(fill="x", pady=(0, 18))
            tk.Label(form, text="Nome do treino", bg=BRANCO).grid(row=0, column=0, sticky="w")
            nome = ttk.Entry(form, width=28); nome.grid(row=1, column=0, padx=(0, 12), pady=6)
            tk.Label(form, text="Objetivo", bg=BRANCO).grid(row=0, column=1, sticky="w")
            objetivo = ttk.Entry(form, width=28); objetivo.grid(row=1, column=1, pady=6)
            tk.Label(form, text="Exercício", bg=BRANCO).grid(row=2, column=0, sticky="w")
            nome_ex = ttk.Entry(form, width=28); nome_ex.grid(row=3, column=0, padx=(0, 12), pady=6)
            
            ents_ex = []
            for lbl, col in [("Séries", 1), ("Repetições", 2), ("Carga (kg)", 3)]:
                tk.Label(form, text=lbl, bg=BRANCO).grid(row=2, column=col, sticky="w")
                e = ttk.Entry(form, width=10); e.grid(row=3, column=col, sticky="w", pady=6); ents_ex.append(e)
            series, repeticoes, carga = ents_ex
            tb = self.tabela(("nome", "objetivo", "exercicios"), ("Treino", "Objetivo", "Exercícios"))

            def att():
                tb.delete(*tb.get_children())
                for t in self.academia.listar_treinos(): tb.insert("", "end", values=(t.get_nome(), t.get_objetivo(), ", ".join(ex.get_nome() for ex in t.get_exercicios())))

            def cad():
                try:
                    if not all(c.get().strip() for c in (nome, objetivo, nome_ex)): return messagebox.showwarning("Atenção", "Preencha o nome, objetivo e exercício.")
                    s, r, c = int(series.get()), int(repeticoes.get()), float(carga.get().replace(",", "."))
                    if s <= 0 or r <= 0 or c < 0: raise ValueError
                except ValueError: return messagebox.showerror("Dados inválidos", "Confira séries, repetições e carga.")
                
                treino = Treino(nome.get().strip(), objetivo.get().strip())
                treino.adicionar_exercicio(Exercicio(nome_ex.get().strip(), s, r, c))
                self.academia.cadastrar_treino(treino)
                self.mostrar_pagina("Treinos")
                messagebox.showinfo("Sucesso", "Treino cadastrado com sucesso!")

            self.botao(form, "Cadastrar treino", cad).grid(row=4, column=0, columnspan=4, sticky="w", pady=(8, 0))
            att()

if __name__ == "__main__":
    root = tk.Tk()
    app = AcademiaApp(root)
    root.mainloop()