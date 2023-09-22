from conexao_postgre import connection_db

cursor_obj = connection_db.cursor()

games = [
    ('Homen Aranha', 1995, 8),
    ('F-Zero', 1994, 7)
]

for game in games:
    # print(f"{game}")
    cursor_obj.execute("""
        INSERT INTO game(name, year, score)
        VALUES (%s, %s, %s)
                       """, game)
    
connection_db.commit()
print("Dados inseridos com sucesso!")
connection_db.close()