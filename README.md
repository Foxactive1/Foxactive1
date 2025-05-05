Projeto: Importação de Dados CSV para SQLite

Autor: Dione Castro Alves
Licença: InNovaIdeia2023 (ideia em Desenvolvimento)

Descrição

Este projeto visa a criação automatizada de um banco de dados SQLite a partir de um arquivo CSV, utilizando Python, pandas e sqlite3. Ideal para pipelines de dados, ETL simplificados e prototipagem rápida de bancos de dados relacionais.

Funcionalidades

Leitura de dados de um arquivo .csv com pandas

Criação de um banco de dados SQLite

Importação automática dos dados para uma tabela

Substituição da tabela caso já exista (opção if_exists='replace')

Mensagem de confirmação no terminal


Pré-requisitos

Certifique-se de ter instalados os seguintes pacotes:

pip install pandas

Como executar

1. Edite o caminho do arquivo CSV no código, se necessário:

data = pd.read_csv('C:\Dcoder\dio_me_projetos\projeto_dio.csv')
conn = sqlite3.connect('C:\Dcoder\dio_me_projetos\dados.db')


2. Execute o script Python:

python modulo1.py


3. Verifique o arquivo dados.db gerado no diretório especificado.



Notas importantes

O caminho dos arquivos deve utilizar dupla barra invertida (\) ou r-string (prefixo r) para evitar erros de escape em Windows.
Exemplo recomendado:

data = pd.read_csv(r'C:\Dcoder\dio_me_projetos\projeto_dio.csv')

A tabela será substituída a cada execução para evitar duplicação de dados.


Licença

Este projeto está sob a licença InNovaIdeia2023 (ideia em Desenvolvimento).


---

Dione Castro Alves
InNovaIdeia Assessoria em Tecnologia ®
