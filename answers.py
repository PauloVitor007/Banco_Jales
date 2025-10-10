from sqlalchemy import create_engine, or_, func, desc
from sqlalchemy.orm import sessionmaker, joinedload
from datetime import datetime
from models import Base, Usuario, Produto, Pedido, Avaliacao

engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()

print("Questão 1: Todos os produtos")
produtos_todos = session.query(Produto).all()
for produto in produtos_todos:
    print(produto)