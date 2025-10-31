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
print("Executando arquivo: atividade33.py\n")

print('--- 33. Usuários que compraram "livros" (produto e qtd) ---')
pedidos_livros = session.query(Usuario.nome, Produto.nome, Pedido.quantidade).join(Pedido).join(Produto).filter(Produto.categoria == 'livros').all()
for user_nome, prod_nome, qtd in pedidos_livros:
    print(f'Usuário: {user_nome}, Produto: {prod_nome}, Qtd: {qtd}')

session.close()
