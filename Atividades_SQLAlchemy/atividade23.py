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
print("Executando arquivo: atividade23.py\n")

print('--- 23. Produtos mais caros, pulando os 3 primeiros (offset 3) ---')
produtos_caros_offset_3 = session.query(Produto).order_by(desc(Produto.preco)).offset(3).all()
for produto in produtos_caros_offset_3:
    print(produto)

session.close()
