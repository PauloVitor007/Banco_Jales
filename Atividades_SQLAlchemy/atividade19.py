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
print("Executando arquivo: atividade19.py\n")

print('--- 19. 6 primeiros usuários (por ID) ---')
primeiros_6_usuarios = session.query(Usuario).order_by(Usuario.id).limit(6).all()
for usuario in primeiros_6_usuarios:
    print(usuario)

session.close()
