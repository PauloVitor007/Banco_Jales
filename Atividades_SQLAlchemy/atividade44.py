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
print("Executando arquivo: atividade44.py\n")

print('--- 44. Categorias com preço médio > R$200 ---')
categoria_media_maior_200 = session.query(Produto.categoria, func.avg(Produto.preco).label('media_preco')).group_by(Produto.categoria).having(func.avg(Produto.preco) > 200).all()
for categoria, media in categoria_media_maior_200:
    print(f'Categoria: {categoria}, Preço Médio: R$ {media:.2f}')

session.close()
