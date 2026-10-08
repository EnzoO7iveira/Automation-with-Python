# 1. BIBLIOTECAS

import os
import pandas as pd


# 2. VARIÁVEIS

# pasta onde está o main.py
# descobre a pasta onde o main.py está salvo:
# __file__ = caminho do próprio script
# abspath  = transforma em caminho completo
# dirname  = remove o nome do arquivo e deixa só a pasta
# assim o programa funciona mesmo se for executado de outro lugar
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# caminho do fonte.txt
ARQUIVO_FONTE = os.path.join(PASTA_BASE, "fonte.txt")

# pastas da Arquitetura Medalhão
PASTA_BRONZE = os.path.join(PASTA_BASE, "bronze")
PASTA_PRATA = os.path.join(PASTA_BASE, "prata")
PASTA_OURO = os.path.join(PASTA_BASE, "ouro")

# arquivos gerados
ARQUIVO_BRONZE = os.path.join(PASTA_BRONZE, "dados_brutos.csv")
ARQUIVO_PRATA = os.path.join(PASTA_PRATA, "diagnostico.txt")


# 3. EXECUÇÃO DO PROGRAMA

# LEITURA DA FONTE
# lê a URL do fonte.txt (strip remove espaços e quebras de linha)
with open(ARQUIVO_FONTE, "r", encoding="utf-8") as arquivo:
    URL = arquivo.read().strip()

# carrega os dados usando a URL
df = pd.read_csv(URL)


# CRIAÇÃO DAS PASTAS
# os.makedirs() cria uma pasta (e, se precisar, todas as pastas do caminho).
os.makedirs(PASTA_BRONZE, exist_ok=True)
os.makedirs(PASTA_PRATA, exist_ok=True)
os.makedirs(PASTA_OURO, exist_ok=True)


# CAMADA BRONZE
# salva os dados brutos, sem nenhuma alteração
df.to_csv(ARQUIVO_BRONZE, index=False)


# CAMADA PRATA
# diagnóstico da base (apenas identifica, não trata os problemas)
with open(ARQUIVO_PRATA, "w", encoding="utf-8") as arquivo:
    arquivo.write("DIAGNÓSTICO DA BASE DE DADOS\n\n")

    # linhas e colunas
    arquivo.write(f"Quantidade de linhas: {df.shape[0]}\n")
    arquivo.write(f"Quantidade de colunas: {df.shape[1]}\n\n")

    # nomes das colunas
    arquivo.write("Colunas:\n")
    for coluna in df.columns:
        arquivo.write(f"{coluna}\n")

    # tipos de dados
    arquivo.write("\nTipos de dados:\n")
    arquivo.write(df.dtypes.to_string() + "\n\n")

    # valores ausentes
    arquivo.write("Valores ausentes por coluna:\n")
    arquivo.write(df.isnull().sum().to_string() + "\n\n")

    # registros duplicados
    arquivo.write(f"Quantidade de registros duplicados: {df.duplicated().sum()}\n\n")

    # valores únicos
    arquivo.write("Valores únicos por coluna:\n")
    arquivo.write(df.nunique().to_string() + "\n")


# CAMADA OURO
# a pasta ouro foi criada acima e fica vazia por enquanto
