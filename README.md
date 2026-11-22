1. Introdução
O projeto consiste no desenvolvimento de um sistema simples de gerenciamento de academia, feito em Python e utilizando Programação Orientada a Objetos (POO). O programa permite organizar cadastros de alunos, planos e treinos, além de registrar exercícios que compõem cada treino. A aplicação é executada pelo terminal e utiliza classes separadas em arquivos Python para organizar o código.
2. Objetivo
O objetivo é auxiliar no controle das principais atividades de uma academia por meio de uma aplicação que permita cadastrar e consultar alunos, planos e treinos. O projeto também busca aplicar os conceitos de POO estudados na disciplina, como classes, objetos, encapsulamento e divisão de responsabilidades.
3. Funcionalidades implementadas
Informar o nome da academia ao iniciar o sistema;
cadastrar alunos com nome, CPF, telefone e data de nascimento;
cadastrar planos com nome, duração em meses e valor;
cadastrar treinos com nome/descrição e objetivo;
adicionar exercícios aos treinos, informando séries, repetições e carga;
listar alunos cadastrados, incluindo CPF, telefone e situação da matrícula;
listar planos cadastrados, exibindo duração, valor e valor total;
listar treinos cadastrados e seus exercícios;
utilizar um menu no terminal para acessar as opções e encerrar o programa.
4. Aplicação da Programação Orientada a Objetos
O código foi dividido em classes, cada uma responsável por representar uma parte do sistema. Os atributos são mantidos como atributos privados (com dois underscores) e o acesso ou alteração ocorre por métodos definidos nas classes.
Academia: mantém o nome da academia e listas de alunos, planos e treinos. Possui métodos para cadastrar e listar esses elementos.
Aluno: armazena nome, CPF, telefone, data de nascimento, situação da matrícula, plano associado e lista de treinos. Possui métodos para consultar e atualizar dados, verificar matrícula e adicionar/listar treinos.
Plano: guarda nome, duração em meses e valor. Permite consultar e alterar o valor, calcular o valor total do plano e exibir seus dados.
Treino: guarda nome, objetivo e uma lista de exercícios. Permite adicionar, remover e exibir exercícios.
Exercicio: guarda nome, séries, repetições e carga. Permite consultar os dados, alterar a prescrição e exibir o exercício.
Pagamento: guarda valor, data, situação de pagamento e aluno relacionado. Permite registrar pagamento e verificar seu status. A classe existe no repositório, mas ainda não está integrada às opções do menu principal.
5. Tecnologias e armazenamento
Python;
Programação Orientada a Objetos;
Listas utilizadas para manter alunos, planos, treinos e exercícios durante a execução;
Interface de interação pelo terminal (menu textual);
Arquivos Python separados por classe/módulo;
Não há persistência em arquivo ou banco de dados implementada no código atual; os registros ficam em memória e são perdidos ao encerrar o programa.
6. Organização dos arquivos
A estrutura atual do repositório é:
Projeto_Sistema_Controle_Academia/
├── README.md
├── Interface
├── main.py
├── academia.py
├── aluno.py
├── plano.py
├── pagamento.py
├── treino.py
└── exercicio.py
O arquivo main.py é o ponto de entrada e contém o menu e o fluxo de interação. Os demais arquivos definem as classes utilizadas pelo sistema. O README.md contém uma descrição breve do projeto.
7. Funcionamento do sistema
Ao iniciar, o programa solicita o nome da academia e apresenta um menu com as opções de cadastro de aluno, cadastro de plano, cadastro de treino e exercícios, listagem de alunos, planos e treinos, além da opção de sair. Durante alguns cadastros, o usuário pode digitar “voltar” para cancelar a operação. Os dados são mantidos em listas enquanto o programa está aberto.
8. Classes e relacionamentos
8.1 Classes definidas
Academia: coordena os cadastros e mantém listas de alunos, planos e treinos.
Aluno: representa o aluno e contém seus dados pessoais e situação de matrícula; também possui atributos para plano e treinos.
Plano: representa um plano da academia, com duração e valor.
Treino: representa uma rotina de exercícios e seu objetivo.
Exercicio: representa um exercício com séries, repetições e carga.
Pagamento: representa um pagamento associado a um aluno, com valor, data e status.
8.2 Relacionamentos entre as classes
Academia mantém coleções de alunos, planos e treinos cadastrados.
Aluno pode possuir um plano associado e uma lista de treinos.
Treino possui uma lista de exercícios.
Pagamento mantém uma referência ao aluno relacionado.
Embora as classes Aluno e Pagamento permitam representar o vínculo entre aluno e pagamento, o menu principal ainda não oferece cadastro ou consulta de pagamentos.
9. Limitações identificadas no código atual
Os cadastros não são salvos em arquivo ou banco de dados; ao fechar o programa, os dados são perdidos.
O menu permite cadastrar e listar alunos, planos e treinos, mas não possui opções para editar ou excluir cadastros.
O vínculo entre aluno e plano existe na classe Aluno, porém não é realizado pelo fluxo de cadastro do menu principal.
A classe Pagamento está implementada separadamente, mas não é utilizada pelo menu principal nem pela classe Academia.
As opções de plano exibidas no menu indicam valores diferentes dos valores atribuídos no código: BASIC aparece como R$ 89,90, mas recebe R$ 299,90; VIP aparece como R$ 120,00, mas recebe R$ 599,90. Essa diferença precisa ser corrigida no código.
10. Resultado atual
O repositório contém um protótipo funcional em terminal para cadastrar e consultar alunos, planos e treinos com exercícios. A estrutura demonstra a utilização de classes e objetos e a separação do código em módulos. Para ampliar o sistema, ainda é necessário implementar persistência dos dados, integração do pagamento ao menu, associação de alunos a planos pelo fluxo principal e operações de edição e exclusão de registros.

11. Diagrama de Classes
 
1.Diagrama de classes do Sistema de Controle de Academia, apresentando as classes, atributos, métodos e relacionamentos definidos para o projeto.
 
2.Tela inicial do sistema, com o resumo de alunos, planos e treinos cadastrados, além das opções de acesso rápido às funcionalidades.

 
3.Exemplo de cadastro de aluno, no qual o sistema solicita o nome para registrar um novo usuário.


 
4.Mensagem de confirmação exibida após a conclusão do cadastro de aluno.
12. Programação dos dias
15/10 – Início do trabalho.
22/10 – Definição das classes Academia, Aluno, Treino e Exercício e elaboração do diagrama.
29/10 – Desenvolvimento da interface/menu e codificação baseada no diagrama.
05/11 – Associação entre aluno e treino e avanço da implementação.
12/11 – Continuação e ajustes do sistema.
