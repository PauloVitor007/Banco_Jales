import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

print("--- Exercício 5: Rate Limiting ---")
user_limit = "limite:user:999"
r.delete(user_limit) # Limpa para teste
MAX_REQ = 5

print("Tentando fazer 7 requisições seguidas...")
for i in range(1, 8):
    # Incrementa contador
    req_count = r.incr(user_limit)
    
    # Se for a primeira requisição, define a janela de 60 segundos
    if req_count == 1:
        r.expire(user_limit, 60)
        
    if req_count <= MAX_REQ:
        print(f"Req {i}: Sucesso")
    else:
        print(f"Req {i}: BLOQUEADA (Limite {MAX_REQ} excedido)")

print(f"TTL restante da chave: {r.ttl(user_limit)} segundos")