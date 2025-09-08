#
# Model baseada em banco de dados
#

import sqlite3

#Criação das tabelas

sql_create_table_livros = '''
CREATE TABLE IF NOT EXISTS livros (
   id, INTEGER PRIMARY KEY NOT NULL,
   codigo TEXT,
   titulo TEXT,
   emprestado INTEGER
);
'''

conexao = sqlite3.connect("biblioteca.db")
conexao.execute(sql_create_table_livros)
conexao.commit()
conexao.close()

dados_livros = [
    ()
]