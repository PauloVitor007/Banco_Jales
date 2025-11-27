"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-19724.crce196.sa-east-1-2.ec2.redns.redis-cloud.com',
    port=19724,
    decode_responses=True,
    username="default",
    password="0jIh9yLSqKqURyuiiSyRDpd1wYgQMzHe",
)

r.set('chave', 10)
print(r.get('chave'))
if r.exists('chave'):
    r.incr('chave')
    print(r.get('chave'))
    r.incrby('chave', 5)
    print(r.get('chave'))
    r.decr('chave')
    print(r.get('chave'))
    r.decrby('chave', 3)
    print(r.get('chave'))
    r.delete('chave')
    print(r.exists('chave'))
