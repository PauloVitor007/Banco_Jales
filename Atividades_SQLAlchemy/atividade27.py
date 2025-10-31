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
print("Executando arquivo: atividade27.py\n")

print('--- 27. Contagem de eletrônicos (estoque > 0, preço > 100) ---')
total_eletronicos_condicao = session.query(Produto).filter(Produto.categoria == 'eletrônicos', Produto.estoque > 0, Produto.preco > 100).count()
print(f'Total de eletrônicos (estoque > 0, preço > 100): {total_eletronicos_condicao}')

session.close()
