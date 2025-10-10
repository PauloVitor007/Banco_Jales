# Exemplo: Criando e usando Session (SQLAlchemy)

Este repositório contém um exemplo simples de como criar e usar uma `Session` do SQLAlchemy com SQLite.

Arquivos principais:

- `main.py`: contém o modelo `Aluno`, a criação do banco e exemplos de inserir e listar registros usando `Session` como context manager.
- `requirements.txt`: dependências necessárias.

Como executar:

1. Instale as dependências (recomendado em um virtualenv):

```bash
pip install -r requirements.txt
```

2. Rode o script:

```bash
python main.py
```

Isto criará `escola.db` no diretório e mostrará os alunos inseridos.

Próximos passos sugeridos: usar `scoped_session` em aplicações web, adicionar validações e testes.
