Automação de dados com Arquitetura Medalhão

Programa em Python que automatiza a organização inicial de uma base de dados CSV, usando como referência a Arquitetura Medalhão.

O fluxo seguido é: receber → preservar → conhecer → preparar para decidir.

O que o programa faz
Lê o endereço (URL) de uma base de dados CSV a partir do arquivo fonte.txt.
Carrega os dados com o Pandas.
Cria automaticamente as pastas bronze/, prata/ e ouro/.
Bronze: salva uma cópia dos dados brutos, sem nenhuma alteração.
Prata: gera um diagnóstico da base, sem tratar nenhum problema encontrado.
Ouro: cria a pasta, que permanece vazia por enquanto.
Camadas
Camada	Pasta	Arquivo gerado	Descrição
Bronze	bronze/	dados_brutos.csv	Dados brutos: nenhuma coluna removida, nenhum valor corrigido, ausentes e duplicados preservados
Prata	prata/	diagnostico.txt	Diagnóstico da base de dados
Ouro	ouro/	(vazia)	Reservada para etapas futuras
Conteúdo do diagnóstico

O arquivo prata/diagnostico.txt registra, com títulos identificando cada resultado:

quantidade de linhas;
quantidade de colunas;
nomes das colunas;
tipos de dados de cada coluna;
quantidade de valores ausentes por coluna;
quantidade de registros duplicados;
quantidade de valores únicos por coluna.

Nesta etapa os problemas são apenas identificados. Nenhum valor é removido ou modificado.

Requisitos
Python 3.8 ou superior
Biblioteca Pandas
bash
pip install pandas
Como executar
Deixe o main.py em uma pasta.
Crie, na mesma pasta, o arquivo fonte.txt contendo apenas a URL de um CSV.
Execute o programa:
bash
python main.py
Fontes para teste
Iris: https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv
Penguins: https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv

Para trocar de base, basta substituir a URL no fonte.txt e executar novamente. Não é necessário alterar o código.

Estrutura

Antes da execução:

text
projeto/
├── main.py
└── fonte.txt

Depois da execução:

text
projeto/
├── main.py
├── fonte.txt
├── bronze/
│   └── dados_brutos.csv
├── prata/
│   └── diagnostico.txt
└── ouro/
Organização do código

O main.py é dividido em funções, cada uma com uma responsabilidade:

Função	Responsabilidade
ler_fonte()	Lê a URL do fonte.txt e a retorna
carregar_dados(URL)	Carrega o CSV e retorna o DataFrame
criar_pasta(caminho)	Cria uma pasta, se ainda não existir
criar_estrutura()	Cria as pastas bronze, prata e ouro
salvar_bronze(df)	Salva os dados brutos na camada Bronze
gerar_diagnostico(df)	Grava o diagnóstico na camada Prata
main()	Executa as etapas na ordem correta
Decisões de projeto
A URL não está escrita no código: ela é sempre lida do fonte.txt.
Os caminhos são construídos a partir da pasta do main.py (os.path.dirname(os.path.abspath(__file__))), então o programa funciona independentemente de onde for executado.
os.makedirs(..., exist_ok=True) permite executar o programa várias vezes sem erro.
O código não usa nomes de colunas fixos, por isso funciona com qualquer CSV.
df.to_csv(..., index=False) evita que o Pandas acrescente uma coluna de índice aos dados brutos.
Possíveis erros
Erro	Causa provável
FileNotFoundError: fonte.txt	O fonte.txt não existe na mesma pasta do main.py ou está com o nome errado (por exemplo, fonte.txt.txt)
Erro ao ler o CSV	URL inválida, com espaços extras ou sem acesso à internet
ModuleNotFoundError: pandas	O Pandas não está instalado (pip install pandas)
Próximas etapas

A pasta ouro/ será utilizada após novas instruções, na fase de preparação dos dados para uma finalidade específica.
