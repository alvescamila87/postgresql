from conexao_postgre import connection_db

cursor_obj = connection_db.cursor()

sql = """
    DELETE FROM game
    WHERE id = %s
"""

cursor_obj.execute(sql, (10,))

connection_db.commit()
print("Dados removidos com sucesso!")
connection_db.close()