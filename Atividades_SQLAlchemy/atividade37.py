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
print("Executando arquivo: atividade37.py\n")

print('--- 37. Nome e idade de todos os usuários ---')
usuarios_nome_idade = session.query(Usuario.nome, Usuario.idade).all()
for nome, idade in usuarios_nome_idade:
    print(f'Nome: {nome}, Idade: {idade}')

session.close()
