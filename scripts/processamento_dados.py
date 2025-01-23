import json
import csv

class Dados:
    def __init__(self, path, type_file):
        self._path = path  
        self._type_file = type_file  
        self._dados = self._leitura_dados()  
        self._nome_colunas = self._get_colunas() 
        self._qtd_linhas = self._size_dados()  

        #privei as instÂncias para assegurar os métodos

    # Getters
    @property
    def dados(self):
        return self._dados

    @property
    def nome_colunas(self):
        return self._nome_colunas

    @property
    def qtd_linhas(self):
        return self._qtd_linhas

    # Métodos privados para leitura de arquivos
    def _leitura_json(self):
        with open(self._path, 'r') as file:
            return json.load(file)

    def _leitura_csv(self):
        dados_csv = []
        with open(self._path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def _leitura_dados(self):
        if self._type_file == 'csv':
            return self._leitura_csv()
        elif self._type_file == 'json':
            return self._leitura_json()
        elif self._type_file == 'list':
            return self._path  
        else:
            return ('Erro no formato de arquivo!')

    def _get_colunas(self):
        return list(self._dados[-1].keys()) if self._dados else []

    def _size_dados(self):
        return len(self._dados)

    # Métodos públicos 
    def rename_colunas(self, key_mapping):
        novos_dados = []
        for old_dict in self._dados:
            dict_temp = {key_mapping.get(old_key, old_key): value for old_key, value in old_dict.items()}
            novos_dados.append(dict_temp)
        self._dados = novos_dados

    @staticmethod #método indicado para usar no curso da Alura
    def join(dadosA, dadosB):
        dados_combinados = dadosA.dados + dadosB.dados
        return Dados(dados_combinados, 'list')

    def transformar_dados_tabela(self):
        tabela_dados_combinados = [self._nome_colunas]
        for row in self._dados:
            linha = [row.get(coluna, 'Indisponível') 
                     for coluna in self._nome_colunas]
            tabela_dados_combinados.append(linha)
        return tabela_dados_combinados

    def save_data(self, path):
        tabela_dados_combinados = self.transformar_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(tabela_dados_combinados)