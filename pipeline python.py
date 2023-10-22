#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:     Dione Castro Alves 
#
# Created:     22/10/2023
# Copyright:   (c) Dione Castro Alves 2023
# Licence:     InNovaIdeia2023 (ideia em Desenvolvimento)
#-------------------------------------------------------------------------------

import sqlite3
import pandas as pd

# Extrai dados do arquivo CSV
data = pd.read_csv('C:\Dcoder\dio_me_projetos\projeto_dio.csv')

# Cria o banco de dados SQLite ' Dados.db'
conn = sqlite3.connect('C:\Dcoder\dio_me_projetos\dados.db')

# Passo 3: Carregar os dados no banco de dados
data.to_sql('sua_tabela', conn, if_exists='replace', index=False)

# Feche a conexão com o banco de dados
conn.close()

print("Banco de dados SQLite criado e dados carregados com sucesso!")
