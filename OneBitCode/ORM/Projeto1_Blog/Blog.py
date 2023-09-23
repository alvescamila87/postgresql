from conexao_orm import Base, engine, session
from Post import Post
from User import User

# Cria as tabelas
Base.metadata.create_all(engine)

# Função para exibir o menu de opções:
def show_menu():
    print("Menu de opções")
    print("[1] Adicionar usuário")
    print("[2] Adicionar post")
    print("[3] Consultar usuários e seus posts")
    print("[4] Sair")
    print()

# Função para Adicionar usuário
def add_user():
    print("Adicionando novo usuário")
    name = str(input("Nome de usuário: "))
    email = str(input("E-mail de usuário: "))
    user = User(name, email)
    session.add(user)
    session.commit()
    print("Usuário adicionado com sucesso!")

# Função para Adicionar post
def add_post():
    print("Adicionando novo post")
    title = str(input("Título do post: "))
    content = str(input("Conteúdo do post: "))
    author_id = int(input("ID do autor do post: "))
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print("Post adicionado com sucesso!")
    else:
        print("Usuário NÃO encontrado.")

# Função para Consultar usuários e posts
def query_users_posts():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"Users: {user.name}, Email: {user.email}")
        for post in user.posts:
            print(f"Post: {post.title}, Conteúdo: {post.content}")

