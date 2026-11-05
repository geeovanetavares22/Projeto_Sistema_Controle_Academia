from academia import Academia
from aluno import Aluno
from plano import Plano
from treino import Treino
from exercicio import Exercicio

if __name__ == "__main__":
    nome_acad = input("Digite o nome da sua academia : ")
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

        if opcao == "1":
            print("\n--- Cadastro de Aluno (digite 'voltar' a qualquer momento para cancelar) ---")
            
            nome = input("Nome do aluno: ")
            if nome.lower() == "voltar": continue
            
            cpf = input("CPF: ")
            if cpf.lower() == "voltar": continue
            
            telefone = input("Telefone: ")
            if telefone.lower() == "voltar": continue
            
            nascimento = input("Data de nascimento (DD/MM/AAAA): ")
            if nascimento.lower() == "voltar": continue
            
            aluno = Aluno(nome, cpf, telefone, nascimento)
            academia.cadastrar_aluno(aluno)
            print(f"Aluno(a) {nome} cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- Cadastro de Plano (digite 'voltar' para cancelar) ---")
            print("Escolha o tipo de plano:")
            print("1. Plano BASIC (R$ 229.90)")
            print("2. Plano VIP (R$ 599.90)")
            
            escolha = input("\nDigite o número da opção (1 ou 2): ")
            if escolha.lower() == "voltar": continue
            
            if escolha == "1":
                nome_plano = "BASIC"
                valor = 229.90
            elif escolha == "2":
                nome_plano = "VIP"
                valor = 599.90
            else:
                print("\nOpção inválida! Escolha 1 ou 2.")
                continue
            
            duracao_str = input("Duração em meses: ")
            if duracao_str.lower() == "voltar": continue
            duracao = int(duracao_str)
            
            plano = Plano(nome_plano, duracao, valor)
            academia.cadastrar_plano(plano)
            print(f"Plano {nome_plano} cadastrado com sucesso!")

        elif opcao == "3":
            print("\n--- Cadastro de Treino (digite 'voltar' para cancelar) ---")
            
            nome_treino = input("Nome/descrição do treino (ex: Treino A - Peito): ")
            if nome_treino.lower() == "voltar": continue
            
            objetivo_treino = input("Objetivo do treino (ex: Hipertrofia, Emagrecimento): ")
            if objetivo_treino.lower() == "voltar": continue
            
            treino = Treino(nome_treino, objetivo_treino)

            cancelou_exercicio = False
            while True:
                print("\nAdicionar Exercício:")
                nome_ex = input("Nome do exercício (ou digite 'voltar' para encerrar): ")
                if nome_ex.lower() == "voltar":
                    cancelou_exercicio = True
                    break
                
                val_series = input("Número de séries: ")
                if val_series.lower() == "voltar":
                    cancelou_exercicio = True
                    break
                series = int(val_series)

                val_rep = input("Número de repetições: ")
                if val_rep.lower() == "voltar":
                    cancelou_exercicio = True
                    break
                repeticoes = int(val_rep)

                val_carga = input("Carga (kg): ")
                if val_carga.lower() == "voltar":
                    cancelou_exercicio = True
                    break
                carga = float(val_carga)
                
                exercicio = Exercicio(nome_ex, series, repeticoes, carga)
                treino.adicionar_exercicio(exercicio)
                print(f"Exercício '{nome_ex}' adicionado ao treino!")

            if cancelou_exercicio and not treino.get_exercicios():
                print("\nCadastro de treino cancelado / Nenhum exercício adicionado.")
            else:
                academia.cadastrar_treino(treino)
                print(f"Treino '{nome_treino}' cadastrado com sucesso!")

        elif opcao == "4":
            print("\n--- Alunos Cadastrados ---")
            alunos = academia.listar_alunos()
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for a in alunos:
                    status = "Ativo" if a.get_matricula_ativa() else "Inativo"
                    print(
                        f"- Nome: {a.get_nome()} | CPF: {a.get_cpf()} | Tel: {a.get_telefone()} | Matrícula: {status}"
                    )
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "5":
            print("\n--- Planos Cadastrados ---")
            planos = academia.listar_planos()
            if not planos:
                print("Nenhum plano cadastrado.")
            else:
                for p in planos:
                    p.exibir_dados()
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "6":
            print("\n--- Treinos Cadastrados ---")
            treinos = academia.listar_treinos()
            if not treinos:
                print("Nenhum treino cadastrado.")
            else:
                for t in treinos:
                    t.exibir_treino()
                    print("\n" * 2)
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "0":
            print("\nEncerrando o sistema. Até o proximo treino!")
            break
        else:
            print("\nOpção inválida! Escolha um número de 0 a 6.")