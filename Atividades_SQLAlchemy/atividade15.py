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
print("Executando arquivo: atividade15.py\n")

print('--- 15. 3 produtos mais caros com estoque (> 0) ---')
produtos_caros_estoque = session.query(Produto).filter(Produto.estoque > 0).order_by(desc(Produto.preco)).limit(3).all()
for produto in produtos_caros_estoque:
    print(produto)

session.close()
