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
print("Executando arquivo: atividade17.py\n")

print('--- 17. Produtos do mais caro para o mais barato (preço desc) ---')
produtos_ordem_preco = session.query(Produto).order_by(desc(Produto.preco)).all()
for produto in produtos_ordem_preco:
    print(produto)

session.close()
