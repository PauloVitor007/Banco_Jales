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
print("Executando arquivo: atividade8.py\n")

print('--- 8. Produto ID 5 com estoque positivo ---')
produto_5 = session.query(Produto).get(5)
if produto_5 and produto_5.estoque > 0:
    print(f'Produto encontrado e com estoque positivo: {produto_5}')
elif produto_5:
    print(f'Produto encontrado, mas sem estoque (Estoque: {produto_5.estoque})')
else:
    print('Produto com ID 5 não encontrado.')

session.close()
