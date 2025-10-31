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
print("Executando arquivo: atividade24.py\n")

print('--- 24. Pedidos (data desc), ignorando os 8 primeiros (offset 8) ---')
pedidos_recentes_offset_8 = session.query(Pedido).order_by(desc(Pedido.data_pedido)).offset(8).all()
for pedido in pedidos_recentes_offset_8:
    print(pedido)

session.close()
