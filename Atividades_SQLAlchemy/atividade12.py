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
print("Executando arquivo: atividade12.py\n")

print('--- 12. Produtos > R$500 com pelo menos 1 pedido ---')
produtos_caros_pedidos = session.query(Produto).join(Pedido).filter(Produto.preco > 500).distinct().all()
for produto in produtos_caros_pedidos:
    print(produto)

session.close()
