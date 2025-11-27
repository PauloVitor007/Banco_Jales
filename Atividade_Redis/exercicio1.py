import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

print("--- Exercício 1: Lista de Tarefas ---")
chave_tarefas = "tarefas:usuario:1"
r.delete(chave_tarefas) # Limpa para teste

# Adiciona tarefas
r.rpush(chave_tarefas, "Estudar Redis")
r.rpush(chave_tarefas, "Fazer exercícios de BD2")
r.rpush(chave_tarefas, "Comprar café")

# Lista todas
tarefas = r.lrange(chave_tarefas, 0, -1)
print(f"Tarefas iniciais: {tarefas}")

# Remove a primeira
item_removido = r.lpop(chave_tarefas)
print(f"Tarefa concluída (removida): {item_removido}")
print(f"Tarefas restantes: {r.lrange(chave_tarefas, 0, -1)}")