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
print("Executando arquivo: atividade42.py\n")

print('--- 42. Soma de quantidades por usuário (ativos > 30) ---')
soma_qtd_usuario_ativo = session.query(Usuario.nome, func.sum(Pedido.quantidade)).join(Pedido).filter(Usuario.ativo == True, Usuario.idade > 30).group_by(Usuario.nome).all()
for nome, soma in soma_qtd_usuario_ativo:
    print(f'Usuário: {nome}, Soma das Quantidades: {soma}')

session.close()
