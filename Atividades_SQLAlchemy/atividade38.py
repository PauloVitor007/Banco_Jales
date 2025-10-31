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
print("Executando arquivo: atividade38.py\n")

print('--- 38. Nome e preço de todos os produtos ---')
produtos_nome_preco = session.query(Produto.nome, Produto.preco).all()
for nome, preco in produtos_nome_preco:
    print(f'Produto: {nome}, Preço: R$ {preco:.2f}')

session.close()
