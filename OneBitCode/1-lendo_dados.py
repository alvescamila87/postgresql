# 1 - Estabelecer conexão
from conexao_postgre import connection_db

# 2 - Criar cursor
cursor_obj = connection_db.cursor()
print(cursor_obj)

# 3 - Executar query
cursor_obj.execute("SELECT * FROM game")

# 4 - Exibir resultado de todos os registros
result = cursor_obj.fetchall()

for row in result:
    print(f"{row}")

# 5 - Imprimir resultado
print(result)

