import redis
redisCli=redis.StrictRedis(host='localhost',port=6379)
# redisCli.set('str1','jieh')
# redisCli.lpush('push','1','2','3')
# redisCli.hset('bb','d','3')
# redisCli.hmset('bc',{'name':'lilei','age':20})
# redisCli.sadd('ee','1','2')
redisCli.zadd('ef',10 ,'e' ,2,'f')
