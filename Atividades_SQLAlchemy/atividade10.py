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
print("Executando arquivo: atividade10.py\n")

print('--- 10. Usuários com idade entre 25 e 35 ---')
usuarios_idade_range = session.query(Usuario).filter(Usuario.idade.between(25, 35)).all()
for usuario in usuarios_idade_range:
    print(usuario)

session.close()
