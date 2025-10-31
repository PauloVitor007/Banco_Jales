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
print("Executando arquivo: atividade3.py\n")

print('--- 3. Pedidos > 01/03/2025 E Quantidade > 5 ---')
data_limite_3 = datetime(2025, 3, 1)
pedidos_recentes_grandes = session.query(Pedido).filter(Pedido.data_pedido > data_limite_3, Pedido.quantidade > 5).all()
for pedido in pedidos_recentes_grandes:
    print(pedido)

session.close()
