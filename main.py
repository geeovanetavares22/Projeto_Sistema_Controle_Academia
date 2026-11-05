from academia import Academia
from aluno import Aluno
from plano import Plano
from treino import Treino
from exercicio import Exercicio


if __name__ == "__main__":
    nome_acad = input("Digite o nome da sua academia: ")

    if nome_acad.lower() == "voltar":
        exit()

    academia = Academia(nome_acad)

    while True:
        print(f"\n=== SISTEMA DE GESTÃO: {academia.get_nome()} ===")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Plano")
        print("3. Cadastrar Treino e Exercícios")
        print("4. Listar Alunos")
        print("5. Listar Planos")
        print("6. Listar Treinos")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        # CADASTRAR ALUNO
        if opcao == "1":
            print("\n--- Cadastro de Aluno ---")

            nome = input("Nome do aluno: ")
            if nome.lower() == "voltar":
                continue

            cpf = input("CPF: ")
            if cpf.lower() == "voltar":
                continue

            telefone = input("Telefone: ")
            if telefone.lower() == "voltar":
                continue

            nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            if nascimento.lower() == "voltar":
                continue

            aluno = Aluno(nome, cpf, telefone, nascimento)
            academia.cadastrar_aluno(aluno)

            print(f"\nAluno {nome} cadastrado com sucesso!")

        # CADASTRAR PLANO
        elif opcao == "2":
            print("\n--- Cadastro de Plano ---")

            nome_plano = input("Nome do plano: ")
            if nome_plano.lower() == "voltar":
                continue

            try:
                duracao = int(input("Duração em meses: "))
                valor = float(input("Valor do plano: "))
            except ValueError:
                print("\nErro: digite números válidos!")
                continue

            plano = Plano(nome_plano, duracao, valor)
            academia.cadastrar_plano(plano)

            print(f"\nPlano {nome_plano} cadastrado com sucesso!")

        # CADASTRAR TREINO
        elif opcao == "3":
            print("\n--- Cadastro de Treino ---")

            nome_treino = input("Nome do treino: ")
            if nome_treino.lower() == "voltar":
                continue

            objetivo_treino = input("Objetivo do treino: ")
            if objetivo_treino.lower() == "voltar":
                continue

            treino = Treino(nome_treino, objetivo_treino)

            while True:
                print("\nAdicionar Exercício:")

                nome_ex = input(
                    "Nome do exercício (ou digite 'voltar' para finalizar): "
                )

                if nome_ex.lower() == "voltar":
                    break

                try:
                    series = int(input("Número de séries: "))
                    repeticoes = int(input("Número de repetições: "))
                    carga = float(input("Carga (kg): "))
                except ValueError:
                    print("\nErro: digite números válidos!")
                    continue

                exercicio = Exercicio(
                    nome_ex,
                    series,
                    repeticoes,
                    carga
                )

                treino.adicionar_exercicio(exercicio)

                print(f"Exercício '{nome_ex}' adicionado com sucesso!")

            if not treino.get_exercicios():
                print("\nNenhum exercício foi adicionado. Treino cancelado.")
            else:
                academia.cadastrar_treino(treino)
                print(f"\nTreino '{nome_treino}' cadastrado com sucesso!")

        # LISTAR ALUNOS
        elif opcao == "4":
            print("\n--- Alunos Cadastrados ---")

            alunos = academia.listar_alunos()

            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for a in alunos:
                    status = (
                        "Ativo"
                        if a.get_matricula_ativa()
                        else "Inativo"
                    )

                    print(
                        f"Nome: {a.get_nome()} | "
                        f"CPF: {a.get_cpf()} | "
                        f"Telefone: {a.get_telefone()} | "
                        f"Matrícula: {status}"
                    )

            input("\nPressione Enter para voltar ao menu...")

        # LISTAR PLANOS
        elif opcao == "5":
            print("\n--- Planos Cadastrados ---")

            planos = academia.listar_planos()

            if not planos:
                print("Nenhum plano cadastrado.")
            else:
                for p in planos:
                    p.exibir_dados()

            input("\nPressione Enter para voltar ao menu...")

        # LISTAR TREINOS
        elif opcao == "6":
            print("\n--- Treinos Cadastrados ---")

            treinos = academia.listar_treinos()

            if not treinos:
                print("Nenhum treino cadastrado.")
            else:
                for t in treinos:
                    t.exibir_treino()
                    print("-" * 30)

            input("\nPressione Enter para voltar ao menu...")

        # SAIR
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break

        # OPÇÃO INVÁLIDA
        else:
            print("\nOpção inválida! Escolha um número de 0 a 6.")
