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
print("Executando arquivo: atividade20.py\n")

print('--- 20. 5 produtos mais baratos com estoque (> 0) ---')
produtos_baratos_estoque_limit = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco).limit(5).all()
for produto in produtos_baratos_estoque_limit:
    print(produto)

session.close()
