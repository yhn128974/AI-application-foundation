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
#     字符串典型的场景，计数
    r.set("counter","0")
    res=r.get("counter")
    print(res)
#     incv自增操作
    r.incr("counter")
    print(f"增加后:{r.get("counter")}")
#     一次增加5个
    r.incr("counter",5)
    print(f"增加后:{r.get("counter")}")
#   自减decr
    r.decr("counter")
    print(f"自减后:{r.get("counter")}")
# 自减3次
    r.decr("counter",3)
    print(f"自减后:{r.get("counter")}")
finally:
    r.close()



