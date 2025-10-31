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
print("Executando arquivo: atividade11.py\n")

print('--- 11. Pedidos cancelados/pendentes feitos depois de 2024 ---')
data_limite_11 = datetime(2024, 12, 31)
pedidos_status = session.query(Pedido).filter(or_(Pedido.status == 'cancelado', Pedido.status == 'pendente'), Pedido.data_pedido > data_limite_11).all()
for pedido in pedidos_status:
    print(pedido)

session.close()
