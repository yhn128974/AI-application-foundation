import redis  # 导入 redis 库

r = redis.Redis(
    host="localhost",      # Redis 服务器地址
    port=6379,             # Redis 默认端口
    db=0,                  # 使用 0 号数据库
    decode_responses=True,  # 自动解码为字符串
    protocol=2
)

try:
    # ==================== 1. 删除旧集合 ====================
    # delete - 发音：/dɪˈliːt/ (di-LEET)
    # 全拼：（英文单词，意为“删除”）
    r.delete("day08:tags", "day08:user:1:tags", "day08:user:2:tags")

    # ==================== 2. SADD - 添加成员 ====================
    # sadd - 发音：/es æd/ (S-add) 或单独读字母 S-A-D-D
    # 全拼：Set Add（集合添加）
    # 作用：向集合（Set）中添加一个或多个元素
    # 特性：自动去重，重复添加相同元素只保留一个
    r.sadd("day08:tags", "python", "redis", "database", "python")
    # 实际存入：{"python", "redis", "database"}  # python 只出现一次

    # ==================== 3. SMEMBERS - 获取所有成员 ====================
    # smembers - 发音：/es ˈmembərz/ (S-members) 或 S-MEMBERS
    # 全拼：Set Members（集合成员）
    # 作用：返回集合中的所有元素（无序）
    # 注意：返回顺序不保证与插入顺序一致
    print("所有标签：", r.smembers("day08:tags"))
    # 输出示例：{'redis', 'python', 'database'}

    # ==================== 4. SISMEMBER - 判断成员是否存在 ====================
    # sismember - 发音：/es ˈɪz ˌmembər/ (S-is-member) 或 S-IS-MEMBER
    # 全拼：Set Is Member（集合是否为成员）
    # 作用：判断指定元素是否存在于集合中
    # 返回值：True（存在）或 False（不存在）
    print("是否包含 redis：", r.sismember("day08:tags", "redis"))
    print("是否包含 numpy：", r.sismember("day08:tags", "numpy"))
    # 输出：True（因为前面添加过 redis）

    # ==================== 5. 准备用户标签数据 ====================
    # 用户1的兴趣标签
    r.sadd("集合1", "python", "redis", "ai")
    # 用户2的兴趣标签
    r.sadd("集合2", "redis", "mysql", "ai")

    # ==================== 6. SINTER - 求交集 ====================
    # sinter - 发音：/es ˈɪntər/ (S-inter) 或 S-INTER
    # 全拼：Set Intersection（集合交集）
    # 作用：返回多个集合的公共元素（同时存在于所有集合中的元素）
    # 数学符号：∩
    print("共同标签：", r.sinter("集合1", "集合2"))
    # 计算过程：{"python", "redis", "ai"} ∩ {"redis", "mysql", "ai"}
    #          = {"redis", "ai"}（redis 和 ai 在两个集合中都存在）
    # 输出示例：{'redis', 'ai'}

finally:
    r.close()