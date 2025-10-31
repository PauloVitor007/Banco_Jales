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
print("Executando arquivo: atividade45.py\n")

print('--- 45. Usuários com soma de quantidades > 10 ---')
usuario_soma_maior_10 = session.query(Usuario.nome, func.sum(Pedido.quantidade).label('soma_total')).join(Pedido).group_by(Usuario.nome).having(func.sum(Pedido.quantidade) > 10).all()
for nome, soma in usuario_soma_maior_10:
    print(f'Usuário: {nome}, Soma Total: {soma}')

session.close()
