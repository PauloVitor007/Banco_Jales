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
print("Executando arquivo: atividade13.py\n")

print('--- 13. Usuários inativos (ativo=False) ---')
usuarios_inativos = session.query(Usuario).filter_by(ativo=False).all()
for usuario in usuarios_inativos:
    print(usuario)

session.close()
