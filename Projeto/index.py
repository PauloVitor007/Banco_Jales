class Usuario:
    def __init__(self, user_id, email, nome, senha):
        self.user_id = user_id
        self.email = email
        self.nome = nome
        self.senha = senha

usuario1 = Usuario(1, "Paulo.Hermogens@email.com", "Paulo Vitor", "senha123")
print(usuario1.nome, usuario1.user_id, usuario1.email, usuario1.senha)