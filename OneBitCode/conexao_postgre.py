# 1 - Instalar biblioteca no pip psycopg2

# 2 - Importar biblioteca
import psycopg2

connection_db = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = '12345',
    host = 'localhost',
    port = '5432',
)

