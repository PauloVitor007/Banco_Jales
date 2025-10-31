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
print("Executando arquivo: atividade9.py\n")

print('--- 9. Pedido ID 3 com dados do usuário (via relationship) ---')
pedido_3 = session.query(Pedido).options(joinedload(Pedido.usuario)).get(3)
if pedido_3:
    print(f'Pedido: {pedido_3}')
    print(f'Usuário do Pedido: {pedido_3.usuario}')
else:
    print('Pedido com ID 3 não encontrado.')

session.close()
