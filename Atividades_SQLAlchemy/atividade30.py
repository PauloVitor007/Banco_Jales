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
print("Executando arquivo: atividade30.py\n")

print('--- 30. Status únicos (usuários ativos > 25) ---')
status_unicos_condicao = session.query(Pedido.status).join(Usuario).filter(Usuario.ativo == True, Usuario.idade > 25).distinct().all()
for (status,) in status_unicos_condicao:
    print(status)

session.close()
