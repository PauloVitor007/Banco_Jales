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
print("Executando arquivo: atividade21.py\n")

print('--- 21. 3 pedidos mais recentes (usuários > 30 anos) ---')
pedidos_recentes_idade_30 = session.query(Pedido).join(Usuario).filter(Usuario.idade > 30).order_by(desc(Pedido.data_pedido)).limit(3).all()
for pedido in pedidos_recentes_idade_30:
    print(f"{pedido} (Usuário: {pedido.usuario.nome}, {pedido.usuario.idade} anos)")

session.close()
