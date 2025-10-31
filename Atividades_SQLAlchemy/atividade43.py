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
print("Executando arquivo: atividade43.py\n")

print('--- 43. Status de pedidos com > 3 registros ---')
status_com_mais_de_3 = session.query(Pedido.status, func.count(Pedido.id).label('contagem')).group_by(Pedido.status).having(func.count(Pedido.id) > 3).all()
for status, contagem in status_com_mais_de_3:
    print(f'Status: {status}, Total: {contagem}')

session.close()
