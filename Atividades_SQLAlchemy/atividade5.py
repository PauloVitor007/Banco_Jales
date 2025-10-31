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
print("Executando arquivo: atividade5.py\n")

print('--- 5. Produto eletrônico mais barato ---')
eletronico_barato = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco).first()
print(eletronico_barato)

session.close()
