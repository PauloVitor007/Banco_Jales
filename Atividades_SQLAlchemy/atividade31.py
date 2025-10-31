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
print("Executando arquivo: atividade31.py\n")

print('--- 31. Usuário (nome) e Pedido (ID) ---')
user_pedidos = session.query(Usuario.nome, Pedido.id).join(Pedido).all()
for nome, pedido_id in user_pedidos:
    print(f'Usuário: {nome}, Pedido ID: {pedido_id}')

session.close()
