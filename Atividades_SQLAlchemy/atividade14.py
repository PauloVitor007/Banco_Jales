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
print("Executando arquivo: atividade14.py\n")

print('--- 14. Livros com preço < R$100 ---')
livros_baratos = session.query(Produto).filter_by(categoria='livros').filter(Produto.preco < 100).all()
for livro in livros_baratos:
    print(livro)

session.close()
