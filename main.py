# ========================================
# BIBLIOTECAS
# ========================================
import os
import pandas as pd

# ========================================
# VARIÁVEIS
# ========================================
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_FONTE = os.path.join(PASTA_BASE, "fonte.txt")

PASTA_BRONZE = os.path.join(PASTA_BASE, "bronze")
PASTA_PRATA = os.path.join(PASTA_BASE, "prata")
PASTA_OURO = os.path.join(PASTA_BASE, "ouro")

ARQUIVO_BRONZE = os.path.join(PASTA_BRONZE, "dados_brutos.csv")
ARQUIVO_PRATA = os.path.join(PASTA_PRATA, "diagnostico.txt")

# ========================================
# FUNÇÕES - LEITURA DA FONTE
# ========================================

def ler_fonte():
    """
    Lê o endereço da base de dados no fonte.txt.
    Retorna a URL como texto.
    """
    with open(ARQUIVO_FONTE, "r", encoding="utf-8") as arquivo:
        URL = arquivo.read().strip()
    return URL

def carregar_dados(URL):
    """
    Carrega o CSV a partir da URL e retorna o DataFrame.
    """
    return pd.read_csv(URL)

# ========================================
# FUNÇÕES - CRIAÇÃO DAS PASTAS
# ========================================

def criar_pasta(caminho):
    """
    Cria uma pasta se ela ainda não existir.
    """
    os.makedirs(caminho, exist_ok=True)

def criar_estrutura():
    """
    Cria as três pastas da Arquitetura Medalhão.
    """
    criar_pasta(PASTA_BRONZE)
    criar_pasta(PASTA_PRATA)
    criar_pasta(PASTA_OURO)

# ========================================
# FUNÇÕES - CAMADAS
# ========================================

def salvar_bronze(df):
    """
    Camada Bronze: salva os dados brutos, sem nenhuma alteração.
    """
    df.to_csv(ARQUIVO_BRONZE, index=False)

def gerar_diagnostico(df):
    """
    Camada Prata: grava o diagnóstico da base em diagnostico.txt.
    Apenas identifica os problemas, sem tratá-los.
    """
    with open(ARQUIVO_PRATA, "w", encoding="utf-8") as arquivo:
        arquivo.write("DIAGNÓSTICO DA BASE DE DADOS\n\n")

        arquivo.write(f"Quantidade de linhas: {df.shape[0]}\n")
        arquivo.write(f"Quantidade de colunas: {df.shape[1]}\n\n")

        arquivo.write("Colunas:\n")
        for coluna in df.columns:
            arquivo.write(f"{coluna}\n")

        arquivo.write("\nTipos de dados:\n")
        arquivo.write(df.dtypes.to_string() + "\n\n")

        arquivo.write("Valores ausentes por coluna:\n")
        arquivo.write(df.isnull().sum().to_string() + "\n\n")

        arquivo.write(f"Quantidade de registros duplicados: {df.duplicated().sum()}\n\n")

        arquivo.write("Valores únicos por coluna:\n")
        arquivo.write(df.nunique().to_string() + "\n")

# ========================================
# FUNÇÃO PRINCIPAL
# ========================================

def main():
    """
    Fluxo: ler fonte -> carregar dados -> criar pastas
           -> bronze -> prata -> ouro (vazia)
    """
    URL = ler_fonte()
    df = carregar_dados(URL)

    criar_estrutura()

    salvar_bronze(df)
    gerar_diagnostico(df)

    # a pasta ouro já foi criada em criar_estrutura() e fica vazia

# ========================================
# INICIALIZAÇÃO DO PROGRAMA
# ========================================

if __name__ == '__main__':
    main()