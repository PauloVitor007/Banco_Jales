import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

print("--- Exercício 3: Contador de Acessos ---")
chave_pagina = "site:pagina:home:views"
r.delete(chave_pagina) # Limpa para teste

# Incrementa acessos
r.incr(chave_pagina)
r.incr(chave_pagina)
total = r.incr(chave_pagina)

print(f"Total de acessos na Home: {total}")
print(f"Valor recuperado: {r.get(chave_pagina)}")