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
print("Executando arquivo: atividade16.py\n")

print('--- 16. Usuários por ordem alfabética (nome) ---')
usuarios_ordem_nome = session.query(Usuario).order_by(Usuario.nome).all()
for usuario in usuarios_ordem_nome:
    print(usuario)

session.close()
