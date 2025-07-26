# Boas-vindas ao repositório do Job Insights!

Aqui você vai encontrar os detalhes de como foi estruturar o desenvolvimento do projeto a partir deste repositório.

# Entregáveis

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />
  
  Neste projeto implementei análises a partir de um conjunto de dados sobre empregos. Minhas implementações são incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). E também testes para a implementação de uma análise de dados. Por fim, como bônus, tive o desafio de escrever uma rota e view para um recurso novo usando Flask!

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
</details>

# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:p4n1k0/job-insights-pythonzin.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd job-insights-pythonzin`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  
</details>


<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

</details>



<details>
  <summary><strong>🗣 Me dê feedbacks sobre o projeto!</strong></summary><br />

</details>


