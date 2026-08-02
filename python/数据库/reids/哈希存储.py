import time

import redis

r=redis.Redis(host='localhost',
              port=6379,
              db=0,
              decode_responses=True,
              protocol=2)

r.config_set("stop-writes-on-bgsave-error", "no")

try:
    print("Redis链接:",r.ping())
    
    r.hset("user-session:123",mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})
    #字典值设置 
    r.hset("user-session:123",'name','Tim')
    print(r.hgetall("user-session:123"))



    # print("获取单个字段：", r.hget("user-session:123", "name"))
    # print("获取多个字段：", r.hmget("user-session:123", ["name", "age"]))
    # print("获取所有字段名：", r.hkeys("user-session:123"))
    # print("获取所有字段值：", r.hvals("user-session:123"))
    # print("获取哈希表大小：", r.hlen("user-session:123"))
    # print("判断字段是否存在：", r.hexists("user-session:123", "name"))
    # print("判断字段是否存在：", r.hexists("user-session:123", "age"))

finally:
    r.close()



