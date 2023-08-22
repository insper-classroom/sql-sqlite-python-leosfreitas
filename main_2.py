from db import db_utils
import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

db_utils.criar_tabela(conn)

estudantes = [ 
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira',' Química', 2022),
]

db_utils.inserir_registros(conn, estudantes)

db_utils.consultar_registros(conn, 'Ano_de_Ingresso', '>=', '2019', 'AND Ano_de_Ingresso <= 2020')

db_utils.atualizar_registros(conn, 'Ano_de_Ingresso', '1980', 'WHERE ID == 1')

db_utils.deletar_registro(conn, 'ID', '=', '2', '')

db_utils.consultar_registros(conn, 'Ano_de_Ingresso', '>', '2019', 'AND Curso == "Computação"')

db_utils.atualizar_registros(conn, 'Ano_de_Ingresso','2018', 'WHERE Curso == "Computação"')