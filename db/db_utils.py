def criar_tabela(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Estudantes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Curso TEXT NOT NULL,
        Ano_de_Ingresso INTEGER
    );
    """)

def inserir_registros(conn, estudantes):
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
    VALUES(?,?,?);
    """, estudantes)
    conn.commit()

def consultar_registros(conn, variavel, operacao, valor, adicional):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Estudantes WHERE {variavel} {operacao} '{valor}' {adicional};")
    print(cursor.fetchall())

def atualizar_registros(conn, variavel, valor, adicional):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Estudantes SET {variavel} = {valor} {adicional};")
    conn.commit()
    cursor.execute("SELECT * FROM Estudantes")
    print(cursor.fetchall())

def deletar_registro(conn, variavel, operacao, valor, adicional):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM Estudantes WHERE {variavel} {operacao} {valor} {adicional};")
    conn.commit()
    cursor.execute("SELECT * FROM Estudantes")
    print(cursor.fetchall())
