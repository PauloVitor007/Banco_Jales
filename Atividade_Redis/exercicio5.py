import redis
import time

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.cloud.redislabs.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

try:
    r.ping()
    print("Conectado ao seu Redis Cloud com sucesso!")
except Exception as e:
    print(f"Erro ao conectar: {e}")

def tentar_acao_usuario(user_id):
    """Verifica se um usuário pode realizar uma ação com base no limite."""
    limite_por_minuto = 5
    tempo_expiracao = 60
    
    chave = f'ratelimit:{user_id}'

    contagem = r.incr(chave)

    if contagem == 1:
        r.expire(chave, tempo_expiracao)
        print(f"Usuário '{user_id}' fez a 1ª requisição. Iniciando janela de 60s.")

    if contagem > limite_por_minuto:
        ttl = r.ttl(chave)
        print(f"Usuário '{user_id}': AÇÃO BLOQUEADA. Limite excedido. Tente em {ttl}s.")
        return False
    else:
        print(f"Usuário '{user_id}': Ação permitida ({contagem}/{limite_por_minuto}).")
        return True

user = 'paulo_vitor'

r.delete(f'ratelimit:{user}')

print(f"--- Simulando 7 requisições rápidas para '{user}' ---")
for i in range(7):
    tentar_acao_usuario(user)
    time.sleep(0.1)