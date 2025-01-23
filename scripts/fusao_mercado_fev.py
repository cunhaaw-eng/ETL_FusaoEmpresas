
from processamento_dados import Dados

# Extraindo os paths do script
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Transformação dos dados
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# Leitura dos dados
dados_empresaA = Dados(path_json, 'json')
dados_empresaA.rename_colunas(key_mapping)
print(f"Transformação dos dados A: {dados_empresaA.nome_colunas}")
print(f"Quantidade de linhas da empresa A: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
dados_empresaB.rename_colunas(key_mapping)
print(f"Transformação dos dados B: {dados_empresaB.nome_colunas}")
print(f"Quantidade de linhas da empresa B: {dados_empresaB.qtd_linhas}")

# Fusão dos dados das duas empresas
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Transformação dos dados: {dados_fusao.nome_colunas}")
print(f"Quantidade de linhas da fusão: {dados_fusao.qtd_linhas}")

#Salvando os dados
dados_fusao.save_data(path_dados_combinados)
print(f"Dados salvos no: {path_dados_combinados}")
