import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

print("--- Exercício 2: Ranking (Leaderboard) ---")
chave_ranking = "game:ranking"
r.delete(chave_ranking) # Limpa para teste

# Adiciona jogadores e pontuações
r.zadd(chave_ranking, {"Ana": 100, "Bruno": 150, "Carlos": 80, "Daniel": 200, "Eduardo": 120})

# Atualiza pontuação
r.zadd(chave_ranking, {"Ana": 180})

# Lista Top 3 (do maior para o menor)
top_3 = r.zrange(chave_ranking, 0, 2, desc=True, withscores=True)
print(f"Top 3 Jogadores: {top_3}")