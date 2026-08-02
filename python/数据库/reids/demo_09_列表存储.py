import redis  # 导入 redis 库，用于连接和操作 Redis 数据库

# ==================== 1. 创建 Redis 连接对象 ====================
r = redis.Redis(
    host="localhost",  # Redis 服务器地址，localhost 表示本机
    port=6379,  # Redis 默认端口号 6379
    db=0,  # 使用的数据库编号（0-15），默认使用 0 号数据库
    decode_responses=True,  # 自动将 Redis 返回的字节串解码为字符串，方便阅读
    protocol=2
)
# decode_responses=True 时，返回的列表元素都是 str 类型；否则是 bytes 类型

# ==================== 2. 异常处理（确保最后关闭连接） ====================
try:
    # 定义存储任务列表的键名
    # 冒号 : 是命名习惯，表示层级关系：day08模块下的tasks列表
    task_key = "day08:tasks"

    # ==================== 3. 清理旧数据（保证演示结果可预测） ====================
    # delete 方法：删除指定的一个或多个键
    # 这里先删除已存在的旧列表，避免之前运行残留的数据干扰本次演示结果
    # 如果键不存在，delete 不会报错，只是返回 0
    r.delete(task_key)
    # 注意：delete 可以删除任何类型的键（string、hash、list、set 等）

    # ==================== 4. 左侧推入元素（头插法） ====================
    # lpush 命令：将一个或多个值从列表的左侧（头部）插入
    # l代表lest
    # 语法：lpush(key, value1, value2, ...)
    # 插入顺序：先插 task1，再插 task2，最后插 task3
    # 因此最终列表顺序（从左到右）：task3 -> task2 -> task1
    r.lpush(task_key, "task1", "task2", "task3")
    # 1.["task1"]
    # 2.["task2","task1"]
    # 3.["task3","task2","task1"]
    # 执行后列表内容：["task3", "task2", "task1"]

    # ==================== 5. 右侧推入元素（尾插法） ====================
    # rpush 命令：将一个或多个值从列表的右侧（尾部）追加
    # r代表right
    # 在现有列表末尾追加 task4 和 task5
    r.rpush(task_key, "task4", "task5")
    # 原始：["task3","task2","task1"]
    # 1. ["task3","task2","task1", "task4"]
    # 2. ["task3","task2","task1", "task4", "task5"]
    # 执行后列表内容：["task3", "task2", "task1", "task4", "task5"]

    # ==================== 6. 查看完整列表 ====================
    # lrange 命令：获取列表中指定范围内的元素
    # 参数：key, start_index, end_index
    # 索引从 0 开始，-1 表示最后一个元素
    # lrange(key, 0, -1) 表示从第一个到最后一个，即获取整个列表
    print("全部任务：", r.lrange(task_key, 0, -1))
    # 输出：全部任务： ['task3', 'task2', 'task1', 'task4', 'task5']
    # 注意：lrange 不会修改列表，只是读取

    # ==================== 7. 左侧弹出一个元素 ====================
    # lpop 命令：移除并返回列表左侧（头部）的第一个元素
    # 执行后：task3 被移除并返回
    print("左侧弹出：", r.lpop(task_key))
    # 原始列表：["task3", "task2", "task1", "task4", "task5"]
    # 输出：左侧弹出： task3
    # 此时列表变为：["task2", "task1", "task4", "task5"]

    # ==================== 8. 右侧弹出一个元素 ====================
    # rpop 命令：移除并返回列表右侧（尾部）的最后一个元素
    # 执行后：task5 被移除并返回
    print("右侧弹出：", r.rpop(task_key))
    # 原始列表：["task2", "task1", "task4", "task5"]
    # 输出：右侧弹出： task5
    # 此时列表变为：["task2", "task1", "task4"]

    # ==================== 9. 再次查看剩余列表 ====================
    # 查看经过两次弹出操作后的最终列表内容
    print("剩余任务：", r.lrange(task_key, 0, -1))
    # 输出：剩余任务： ['task2', 'task1', 'task4']

# ==================== 10. 无论是否异常，最后都要关闭连接 ====================
finally:
    r.close()  # 关闭 Redis 连接，释放网络资源