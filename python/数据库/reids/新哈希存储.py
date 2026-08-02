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

    task_name='day08:task'
    r.delete(task_name)
    # 左侧插入
    r.lpush(task_name,123,456,789)
    # 右侧插入
    r.rpush(task_name,987,654,321)
    print("全部任务",r.lrange(task_name,0,-1))
    print("获取前三个任务",r.lrange(task_name,0,2))
    print("获取后三个任务",r.lrange(task_name,-3,-1))
    print("左侧弹出:",r.lpop(task_name))
    print("右侧弹出:",r.rpop(task_name))
    print("列表长度:",r.llen(task_name))
finally:
    r.close()



