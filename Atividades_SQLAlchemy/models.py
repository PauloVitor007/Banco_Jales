from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)

    # relacionamento com pedidos e avaliações
    pedidos = relationship("Pedido", back_populates="usuario")
    avaliacoes = relationship("Avaliacao", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', idade={self.idade}, ativo={self.ativo})>"


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(50))
    preco = Column(Float)
    estoque = Column(Integer)

    pedidos = relationship("Pedido", back_populates="produto")
    avaliacoes = relationship("Avaliacao", back_populates="produto")

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', categoria='{self.categoria}', preco={self.preco})>"


class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    data_pedido = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="pedidos")
    produto = relationship("Produto", back_populates="pedidos")

    def __repr__(self):
        return f"<Pedido(id={self.id}, usuario_id={self.usuario_id}, produto_id={self.produto_id}, quantidade={self.quantidade}, data={self.data_pedido.date()})>"


class Avaliacao(Base):
    __tablename__ = "avaliacoes"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    nota = Column(Float)
    comentario = Column(String(200))

    usuario = relationship("Usuario", back_populates="avaliacoes")
    produto = relationship("Produto", back_populates="avaliacoes")

    def __repr__(self):
        return f"<Avaliacao(id={self.id}, usuario_id={self.usuario_id}, produto_id={self.produto_id}, nota={self.nota})>"
