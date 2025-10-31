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
print("Executando arquivo: atividade18.py\n")

print('--- 18. Pedidos por status (asc) e data (desc) ---')
pedidos_ordem_status_data = session.query(Pedido).order_by(Pedido.status, desc(Pedido.data_pedido)).all()
for pedido in pedidos_ordem_status_data:
    print(pedido)

session.close()
