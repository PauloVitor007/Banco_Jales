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
print("Executando arquivo: atividade2.py\n")

print('--- 2. Usuários ativos > 18 anos ---')
usuarios_ativos_maiores = session.query(Usuario).filter(Usuario.ativo == True, Usuario.idade > 18).all()
for usuario in usuarios_ativos_maiores:
    print(usuario)

session.close()
