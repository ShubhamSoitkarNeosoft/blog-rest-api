import redis
import json 

redis_client = redis.Redis(host="localhost",port=6379,db=0)

username = redis_client.get('username')
print(username)

redis_client.set("mis_data",json.dumps({"pe":33}))