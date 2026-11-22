# Sistema de Controle de Academia

## Sobre o projeto
Sistema protótipo desenvolvido em Python para auxiliar no gerenciamento de uma academia. O trabalho foi realizado para a disciplina de Programação Orientada a Objetos (POO), aplicando classes, objetos, encapsulamento e divisão de responsabilidades.

O sistema permite cadastrar e consultar alunos, planos e treinos, além de adicionar exercícios aos treinos. O projeto possui interface gráfica e código organizado em módulos.

## Objetivos
- Organizar informações da academia.
- Facilitar cadastros e consultas de alunos, planos e treinos.
- Aplicar conceitos de Programação Orientada a Objetos.
- Desenvolver um protótipo para solucionar uma necessidade real.

## Funcionalidades
- Informar o nome da academia ao iniciar.
- Cadastrar alunos com nome, CPF, telefone e data de nascimento.
- Cadastrar planos com nome, duração e valor.
- Cadastrar treinos com nome/descrição e objetivo.
- Adicionar exercícios aos treinos, informando séries, repetições e carga.
- Listar alunos, planos e treinos cadastrados.
- Consultar exercícios associados aos treinos.
- Acessar as opções por meio da interface do sistema.

## Tecnologias
- Python
- Programação Orientada a Objetos (POO)
- Interface gráfica
- Git e GitHub

## Estrutura do projeto
Projeto_Sistema_Controle_Academia/
├── README.md
├── Interface/
├── main.py
├── academia.py
├── aluno.py
├── plano.py
├── pagamento.py
├── treino.py
└── exercicio.py
```

- `main.py`: ponto de entrada e fluxo principal.
- `academia.py`: coordena os cadastros.
- `aluno.py`: dados e operações relacionadas aos alunos.
- `plano.py`: informações e operações dos planos.
- `treino.py`: organização dos treinos.
- `exercicio.py`: dados dos exercícios, como séries, repetições e carga.
- `pagamento.py`: classe para representar pagamentos, ainda não integrada ao fluxo principal.
- `Interface/`: arquivos relacionados à interface gráfica.

## Como executar

### Pré-requisitos
- Python instalado.
- Git (para clonar o repositório).
- Editor de código, como VS Code ou PyCharm.

### Clonar o repositório
```bash
git clone https://github.com/geeovanetavares22/Projeto_Sistema_Controle_Academia.git
cd Projeto_Sistema_Controle_Academia
```

### Iniciar
```bash
python main.py
```
No Windows, se necessário:
```bash
py main.py
```
Caso sejam necessárias bibliotecas externas, instale as dependências utilizadas pelo projeto antes de executar.

## Processo de desenvolvimento
O trabalho foi realizado em etapas, desde a definição da proposta até a implementação e ajustes.

- **15/10 – Início:** definição inicial da proposta.
- **22/10 – Modelagem:** definição das classes Academia, Aluno, Treino e Exercício e elaboração do diagrama de classes.
- **29/10 – Desenvolvimento:** criação da interface/menu e codificação baseada no diagrama.
- **05/11 – Implementação:** associação entre aluno e treino e avanço das funcionalidades.
- **12/11 – Ajustes:** continuação do desenvolvimento e revisão do sistema.

### Classes e responsabilidades
- **Academia:** mantém os cadastros de alunos, planos e treinos.
- **Aluno:** armazena dados pessoais, situação da matrícula e referências a plano e treinos.
- **Plano:** contém nome, duração e valor.
- **Treino:** representa uma rotina de exercícios e seu objetivo.
- **Exercicio:** registra nome, séries, repetições e carga.
- **Pagamento:** representa valor, data, status e aluno relacionado; ainda não está integrado ao menu principal.

## Limitações atuais
- Os dados não são persistidos em arquivos ou banco de dados; são perdidos ao encerrar o programa.
- Não estão disponíveis todas as operações de edição e exclusão.
- O vínculo entre aluno e plano ainda não está concluído no fluxo principal.
- A classe Pagamento ainda não está integrada ao menu.
- Os valores de alguns planos exibidos no menu precisam ser revisados para corresponder aos valores definidos no código.

## Melhorias futuras aplicadas
- Implementar persistência em arquivo ou banco de dados.
- Integrar pagamentos ao sistema.
- Concluir a associação de alunos aos planos pelo menu.
- Implementar edição e exclusão de cadastros.
- Revisar os valores dos planos e melhorar as validações.

## Integrantes
- Nome: Guilherme Alves Lames Santana 
- Nome: Geovane Tavares Prado

## Repositório
https://github.com/geeovanetavares22/Projeto_Sistema_Controle_Academia
