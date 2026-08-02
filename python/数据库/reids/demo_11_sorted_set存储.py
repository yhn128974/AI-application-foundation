import redis  # 导入 redis 库

r = redis.Redis(
    host="localhost",      # Redis 服务器地址
    port=6379,             # Redis 默认端口
    db=0,                  # 使用 0 号数据库
    decode_responses=True,  # 自动解码为字符串
    protocol=2
)

try:
    # ==================== 1. 删除旧排行榜 ====================
    # delete - 发音：/dɪˈliːt/ (di-LEET)
    # 全拼：（英文单词，意为"删除"）
    rank_key = "day08:leaderboard"
    r.delete(rank_key)

    # ==================== 2. ZADD - 添加成员和分数 ====================
    # zadd - 发音：/ziː æd/ (Z-add) 或单独读字母 Z-A-D-D
    # 全拼：Sorted Set Add（有序集合添加）
    # 作用：向有序集合（Sorted Set）中添加元素及其分数
    # 特性：根据分数自动排序，分数可重复，成员唯一
    # mapping 参数：字典，键=成员名，值=分数
    r.zadd(rank_key, {
        "player1": 1000,
        "player2": 1500,
        "player3": 800,
        "player4": 2000
    })
    # 存储结构（按分数排序）：
    # player3(800) < player1(1000) < player2(1500) < player4(2000)
    sorted_players = r.zrange(rank_key, 0, -1, withscores=True)
    print("默认升序：", sorted_players)

    # ==================== 3. ZREVRANGE - 获取降序排行榜 ====================
    # zrevrange - 发音：/ziː ˈrɛv reɪndʒ/ (Z-rev-range)
    # 全拼：Sorted Set Reverse Range（有序集合反向范围）
    # 参数：(key, start, stop, withscores)
    #   - start: 起始索引（0 表示第一个）
    #   - stop: 结束索引（-1 表示最后一个）
    #   - withscores=True: 同时返回成员和分数
    # 作用：按分数从高到低返回指定范围的成员
    print("排行榜：", r.zrevrange(rank_key, 0, -1, withscores=True))
    # 输出示例：[('player4', 2000.0), ('player2', 1500.0), ('player1', 1000.0), ('player3', 800.0)]
    # 注意：withscores=True 时返回列表，每个元素是 (成员, 分数) 的元组

    # ==================== 4. ZINCRBY - 增加分数 ====================
    # zincrby - 发音：/ziː ˈɪŋkər baɪ/ (Z-incre-by)
    # 全拼：Sorted Set Increment By（有序集合增加）
    # 参数：(key, increment, member)
    #   - increment: 要增加的分数（可以是负数表示减少）
    #   - member: 要操作的成员
    # 作用：对指定成员的分数增加指定数值
    r.zincrby(rank_key, 500, "player2")
    print("增加后排行榜：", r.zrevrange(rank_key, 0, -1, withscores=True))
    # player2 原分数 1500 → 增加 500 → 新分数 2000
    # 此时排序变化：player2(2000) 与 player4(2000) 分数相同
    # Redis 会按字典序（成员名字的二进制顺序）排列同分元素

    # ==================== 5. ZREVRANK - 获取降序排名 ====================
    # zrevrank - 发音：/ziː ˈrɛv ræŋk/ (Z-rev-rank)
    # 全拼：Sorted Set Reverse Rank（有序集合反向排名）
    # 作用：返回成员在有序集合中的降序排名（从高到低）
    # 返回值：从 0 开始的索引（0 表示第一名）
    # 如果是升序排名用 zrank
    rank = r.zrevrank(rank_key, "player4")
    # player2 分数 2000，与 player4 并列第一
    # 实际排名：player2 和 player4 中字典序较大的排在前面？
    # 更准确说：同分时排名相同，但 zrevrank 返回的是基于底层存储的位置
    print("player4 当前名次：", rank + 1)
    # rank 从 0 开始，所以展示给用户时需要 +1

finally:
    r.close()