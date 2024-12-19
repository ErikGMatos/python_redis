from typing import Optional

import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# para inert e update
redis_conn.set('chave_1', 'trocando o meu valor')

# select
valor: Optional[bytes] = redis_conn.get("chave_1")
if valor is not None:
    valor = valor.decode('utf-8')

# delete dados
redis_conn.delete('chave_1')


# comandos para hash
redis_conn.hset('meu_hash', 'nome', 'joao')
redis_conn.hset('meu_hash', 'idade', '30')
redis_conn.hset('meu_hash', 'cidade', 'curitiba')

valor_1 = redis_conn.hget('meu_hash', 'nome').decode("utf-8")

redis_conn.hdel('meu_hash', 'cidade')

# buscas por existencia chaves normais
elem = redis_conn.exists('chave_1')
print(elem)
# buscas por existencia chaves hashes
elem2 = redis_conn.hexists('meu_hash', "nome")
print(elem2)

# Expiracão de dados TTL -> Time To Live
redis_conn.set("chave_del", "esse valor sera deletado", 12)

redis_conn.expire("meu_hash", 30)
