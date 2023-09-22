from conexao_postgre import connection_db

cursor_obj = connection_db.cursor()

sql = """
    UPDATE game 
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ("Resident Evil", 10))

connection_db.commit()
print("Dados atualizados com sucesso!")
connection_db.close()