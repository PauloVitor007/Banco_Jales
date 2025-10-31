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
print("Executando arquivo: atividade32.py\n")

print('--- 32. Produtos e quantidades (Usuário "João") ---')
pedidos_joao = session.query(Produto.nome, Pedido.quantidade).join(Pedido).join(Usuario).filter(Usuario.nome == 'João').all()
if not pedidos_joao:
    print('João não realizou pedidos.')
else:
    for nome_produto, qtd in pedidos_joao:
        print(f'Produto: {nome_produto}, Quantidade: {qtd}')

session.close()
