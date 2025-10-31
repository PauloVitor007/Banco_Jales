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
print("Executando arquivo: atividade22.py\n")

print('--- 22. Usuários, ignorando os 5 primeiros (offset 5) ---')
usuarios_offset_5 = session.query(Usuario).order_by(Usuario.id).offset(5).all()
for usuario in usuarios_offset_5:
    print(usuario)

session.close()
