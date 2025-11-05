# 🚀 Projeto ETL do Aeroporto de Schiphol

## 📝 Descrição do Projeto

Este projeto implementa um pipeline de **ETL (Extract, Transform, Load)** para **extrair dados da API do Aeroporto de Schiphol, extrai flights, aircraftTypes, airlines, destinations e transforma eles para uma melhor visualização.**

**O principal objetivo é fornecer uma base de dados limpa e estruturada para que analistas possam gerar relatórios sobre os voos e tudo o que a API disponibiliza.**

## ✨ Funcionalidades Principais

* **Extração de Dados:** Dados da API do Aeroporto de Schiphol
* **Transformação de Dados:** Os dados extraídos são transformados para melhor visualização, transformando a data para UTC e filtrando os outros dados
* **Carregamento de Dados:** Os dados transformados são carregados em arquivos **CSV** utilizando a biblioteca Pandas, persistindo os resultados na pasta onde o projeto é executado.

## 🛠️ Tecnologias Utilizadas
* **Postman:** Utilizado para ver como a API funcionava antes de colocar a mão na massa.
* **Python:** Linguagem principal para o desenvolvimento do pipeline.
    * **Pandas:** Para manipulação e transformação eficiente de DataFrames.
    * **Requests:** Para extração de dados de APIs
    * **Datetime:** Para a conversão e manipulação de formatos de data e hora (especialmente para UTC).
    * **python-dotenv:** Para gerenciamento seguro de variáveis de ambiente (como as chaves da API).
* **Git / GitHub:** Para controle de versão do projeto.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o pipeline ETL em sua máquina local.

### 🛠️ **Pré-requisitos**

* Python 3.8+ instalado.
* Pip (gerenciador de pacotes do Python).
* **Chave de API do Aeroporto de Schiphol:** É necessário obter uma chave de API para acessar os dados. **link: https://developer.schiphol.nl/**

### 🐈‍⬛ **1. Clonar o Repositório**
Bash
git clone [https://github.com/dev-DaviGuerra/Primeira-ETL.git](https://github.com/dev-DaviGuerra/Primeira-ETL.git)

### 🖥️ **2. Configurar o Ambiente Virtual**
Bash

python -m venv venv
#### **No Windows (PowerShell):**
.\venv\Scripts\Activate.ps1
#### **No Linux/macOS:**
source venv/bin/activate
### 🛠️ **3. Instalar Dependências**
Bash

pip install -r requirements.txt
### 🔐 **4. Configurar a Chave de API**
Crie um arquivo chamado .env na raiz do seu projeto (na mesma pasta do README.md e da pasta aeroporto.etl) e adicione sua chave de API nele.

IMPORTANTE: O arquivo .env deve ser ignorado pelo Git (verifique o .gitignore).

# 🤐 Conteúdo do arquivo .env
APP_ID="Sua APP_ID"

APP_KEY="Sua APP_KEY"

### ☑️ **5. Executar o Pipeline ETL**
Bash

python aeroporto_etl/main.py
