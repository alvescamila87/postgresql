# 1 - Install SQL Alchemy

# 2 - Import SQL Alchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative (deprecated since: 2.0) --> import declarative_base pn sqlalchemy.orm 

# 3 - Variável para receber a URL de conexão com postgreSQL

user = 'postgres'
password = '12345'
host = 'localhost'
database = 'blog'

# DATABASE_URI = 'postgresql://postgres:12345@localhost/blog'
DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

# Configurações do sql alchemy para estabelecer conexão ORM
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()




