import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

print("--- Exercício 6: Interseção e Diferença ---")
meus_seguidores = "social:1:seguidores"
estou_seguindo = "social:1:seguindo"
r.delete(meus_seguidores, estou_seguindo) # Limpa para teste

# Quem me segue
r.sadd(meus_seguidores, "Alice", "Bob", "Carol")
# Quem eu sigo
r.sadd(estou_seguindo, "Bob", "Carol", "Dave", "Eve")

# 1. Amigos em comum (Interseção)
comum = r.sinter(meus_seguidores, estou_seguindo)
print(f"Amigos em comum: {comum}")

# 2. Todos os contatos (União)
todos = r.sunion(meus_seguidores, estou_seguindo)
print(f"Todos os envolvidos: {todos}")

# 3. Sigo mas não me segue (Diferença)
nao_reciproco = r.sdiff(estou_seguindo, meus_seguidores)
print(f"Sigo mas não me segue de volta: {nao_reciproco}")