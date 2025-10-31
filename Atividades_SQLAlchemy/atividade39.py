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
print("Executando arquivo: atividade39.py\n")

print('--- 39. Usuário (nome), Pedido (ID) e Quantidade ---')
user_pedido_qtd = session.query(Usuario.nome, Pedido.id, Pedido.quantidade).join(Pedido).all()
for nome, pedido_id, qtd in user_pedido_qtd:
    print(f'Usuário: {nome}, Pedido ID: {pedido_id}, Qtd: {qtd}')

session.close()
