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
print("Executando arquivo: atividade40.py\n")

print('--- 40. Contagem de pedidos por status ---')
contagem_por_status = session.query(Pedido.status, func.count(Pedido.id)).group_by(Pedido.status).all()
for status, contagem in contagem_por_status:
    print(f'Status: {status}, Total: {contagem}')

session.close()
