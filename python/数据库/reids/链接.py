import redis
# 1. 建立连接。开启 decode_responses=True 将自动把字节解码为字符串
r = redis.Redis(host='localhost', port=6379, decode_responses=True, protocol=2)# 2. 简单的字符串键值对 (String) 操作

r.set('foo', 'bar') # 返回 True
print(r.get('foo')) # 输出: bar

# 3. 散列/哈希 (Hash) 操作
r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
}) # 返回 True
# 获取整个哈希表
print(r.hgetall('user-session:123'))
# 输出: {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}
# 4. 结束操作，关闭连接
r.close()
