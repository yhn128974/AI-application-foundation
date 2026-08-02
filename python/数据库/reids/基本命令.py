import time

import redis

r=redis.Redis(host='localhost',
              port=6379,
              db=0,
              decode_responses=True,
              protocol=2)

# r = redis.Redis(host='localhost',
#                 port=6379,
#                 decode_responses=True,
#                 protocol=2)
# 2. 简单的字符串键值对 (String) 操作

try:
    print("Redis链接:",r.ping())
    # r.set('day08:redis:intro','redis 可以用缓存')
    # res=r.get('day08:redis:intro')
    # 吧一个值，保存到 Redis,并设置缓存时间,以秒为单位
    r.setex("dify",3,"AI编程")
    # 休眠
    time.sleep(4)
    res = r.get('dify')

    # 显示剩余时间
    print(res,r.ttl("dify"))
    #
finally:
    r.close()



