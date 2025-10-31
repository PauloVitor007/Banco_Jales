import sys
from sqlalchemy import create_engine, func, desc, and_, or_
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy.sql import exists
from datetime import datetime

try:
    from models import Base, Usuario, Produto, Pedido, Avaliacao
except ImportError:
    print("Erro: Não foi possível encontrar o arquivo models.py.")
    sys.exit(1)

engine = create_engine('sqlite:///exercicios.db')
Session = sessionmaker(bind=engine)
session = Session()
print("Executando arquivo: atividade1.py\n")

print('--- 1. Todos os produtos ---')
produtos_todos = session.query(Produto).all()
for produto in produtos_todos:
    print(produto)

session.close()
