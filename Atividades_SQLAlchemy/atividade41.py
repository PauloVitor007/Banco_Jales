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
print("Executando arquivo: atividade41.py\n")

print('--- 41. Preço médio por categoria de produto ---')
media_por_categoria = session.query(Produto.categoria, func.avg(Produto.preco)).group_by(Produto.categoria).all()
for categoria, media in media_por_categoria:
    print(f'Categoria: {categoria}, Preço Médio: R$ {media:.2f}')

session.close()
