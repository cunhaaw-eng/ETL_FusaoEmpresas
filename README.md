# 🚀 Pipeline de Dados: Fusão de Informações de Empresas

Este projeto consiste na construção de uma pipeline de dados para consolidar informações de duas empresas que utilizam formatos de dados distintos (JSON e CSV). O processo foi desenvolvido com Python, seguindo boas práticas de **Engenharia de Software** e utilizando o paradigma de **Programação Orientada a Objetos (P.O.O)**.

## 📂 Estrutura do Projeto

Abaixo está a organização dos diretórios e arquivos do projeto:


## 🛠️ Funcionalidades

1. **Extração dos Dados**:  
   - Carregamento de arquivos nos formatos JSON e CSV.
   - Uso de classes para abstração e encapsulamento dos dados.

2. **Transformação dos Dados**:  
   - Padronização de colunas com um mapeamento pré-definido.
   - Integração dos dados das duas empresas, respeitando critérios estabelecidos.

3. **Carregamento dos Dados**:  
   - Salva os dados consolidados no formato CSV, pronto para análise.

4. **Organização do Projeto**:  
   - Diretórios bem definidos para facilitar manutenção e escalabilidade.
   - Testes e validações realizadas com Jupyter Notebook.

## 🔑 Principais Scripts

### `processamento_dados.py`
Contém a classe **`Dados`**, que realiza as operações essenciais para a pipeline de dados:
- Leitura de arquivos nos formatos JSON e CSV.
- Renomeação e padronização de colunas.
- Fusão de dados de múltiplas fontes.
- Salvamento de dados consolidados em formato CSV.

### `fusao_mercado_fevereiro.py`
Executa o processo completo de ETL:
1. Carrega os dados brutos das empresas.
2. Renomeia as colunas com base no mapeamento fornecido.
3. Realiza a fusão dos dados.
4. Salva o resultado consolidado em `data_processed/dados_combinados.csv`.

