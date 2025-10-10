from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///escola.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)

# Cria uma classe Session configurada
Session = sessionmaker(bind=engine, expire_on_commit=False, future=True)

Base = declarative_base()


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer)

    def __repr__(self):
        return f"<Aluno(id={self.id}, nome={self.nome!r}, idade={self.idade})>"


def init_db():
    """Cria as tabelas no banco se não existirem."""
    Base.metadata.create_all(engine)


def criar_aluno(nome: str, idade: int) -> Aluno:
    """Cria um aluno e retorna a instância persistida."""
    with Session() as session:
        aluno = Aluno(nome=nome, idade=idade)
        session.add(aluno)
        # commit salva a transação e popula atributos como 'id'
        session.commit()
        # refresh opcional se expire_on_commit=True
        session.refresh(aluno)
        return aluno


def listar_alunos() -> list[Aluno]:
    """Retorna todos os alunos cadastrados."""
    with Session() as session:
        return session.query(Aluno).order_by(Aluno.id).all()


def main():
    init_db()

    print("Inserindo 3 alunos de exemplo...")
    criar_aluno("Ana", 20)
    criar_aluno("Bruno", 22)
    criar_aluno("Carla", 19)

    print("Alunos no banco:")
    for a in listar_alunos():
        print(a)


if __name__ == "__main__":
    main()
