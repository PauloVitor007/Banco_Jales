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
print("Executando arquivo: atividade35.py\n")

print('--- 35. Existe pedido para produto sem estoque? ---')
pedido_estoque_zero = session.query(session.query(Pedido).join(Produto).filter(Produto.estoque == 0).exists()).scalar()
print(f'Existe pedido para produto sem estoque? {pedido_estoque_zero}')

session.close()
