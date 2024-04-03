# Projeto de Processamento de Linguagem Natural (PLN) com Python

Este repositório contém um projeto de Processamento de Linguagem Natural (PLN) desenvolvido em Python. O objetivo do projeto é realizar a extração de textos de páginas da Wikipedia, segmentar esses textos em orações menores, e utilizar o modelo BERT para a tarefa de Masked Language Modeling (MLM).


## Sumário

- [Arquivos](#arquivos)
- [Funcionalidades](#funcionalidades)
- [Como-instalar](#como-instalar)
- [Pontos-de-Melhoria](#pontos-de-melhoria)

## Arquivos

- [`cli.py`](app/cli.py): Contém a definição do CLI utilizando a biblioteca `Typer`, incluindo os comandos `default` e `request-wiki` para executar as funcionalidades principais do projeto.
  
- [`compare.py`](app/compare.py): Implementa a classe responsável por comparar a sentença original, a sentença preenchida por MASK e a sentença gerada pelo modelo BERT. Essa classe é fundamental para avaliar a qualidade das previsões do modelo.
  
- [`complete.py`](app/complete.py): Inclui a função que utiliza o modelo BERT para preencher as strings com máscaras, permitindo realizar a tarefa de Masked Language Modeling (MLM) de forma eficiente.
  
- [`tokens.py`](app/tokens.py): Define classes que processam e segmentam as orações em textos menores, facilitando o processamento e análise de dados no projeto.
  
- [`wiki_classes.py`](app/wiki_classes.py): Contém a classe responsável por fazer requests e tratar as páginas da Wikipedia, realizando o web scraping e a extração dos textos necessários para o processamento de PLN.

- [`configs`](app/supply/configs.py): Contém variáveis de suporte e definições de comportamento para outros arquivos do projeto. 

## Funcionalidades

### 1. Extração de Textos da Wikipedia

Utiliza a biblioteca `BeautifulSoup` em conjunto com o `requests` para realizar o web scraping em páginas da Wikipedia, extraindo seus textos para utilização no processamento de PLN.

### 2. Segmentação de Textos em Orações Menores

Após a extração dos textos, o projeto segmenta esses textos em orações menores. Essa segmentação utiliza a biblioteca `Spacy` para a detecção de sintagmas, lemas e tokenização das palavras. O modelo utilizado foi o padrão `pt_core_news_md`.

### 3. Utilização do Modelo BERT para Masked Language Modeling (MLM)

O modelo BERT (Bidirectional Encoder Representations from Transformers) é utilizado para a tarefa de Masked Language Modeling (MLM). Nessa tarefa, partes das orações segmentadas são ocultadas ([MASK]) e o modelo BERT é utilizado para prever as palavras ocultas com base no contexto das orações.

### 4. Command Line Interface (CLI)

O projeto implementa um CLI (Command Line Interface) com dois comandos principais:

- `default`: Executa o processo padrão do projeto, incluindo a extração de textos, segmentação em orações menores e aplicação do modelo BERT para MLM.
  
- `request-wiki`: Realiza requests para páginas da Wikipedia, extrai os textos e executa o processamento conforme descrito no comando `default`.

## Como instalar

1. **Clone o Repositório:** No terminal, use o comando `git clone` seguido do URL do repositório do GitHub:
   ```bash
   git clone https://github.com/Jojojmo/CLI-Test-Project.git
   ```


3. **Crie e Ative um Ambiente Virtual:**
   ```bash
   python -m venv .env
   ```
   Em seguida, ative o ambiente virtual:
   - No Windows:
     ```bash
     .env\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .env/bin/activate
     ```

4. **Instale as Dependências:** Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Pontos de Melhoria

- Adicionar mais comandos no CLI para maior flexibilidade e funcionalidades adicionais.
- Melhorar o processamento e interações com o usuário para uma experiência mais intuitiva.
- Realizar o tuning do modelo BERT para melhorar a qualidade das previsões em Masked Language Modeling.