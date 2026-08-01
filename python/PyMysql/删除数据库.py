import pymysql
# 建立链接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='Yuhaonan2048',
                       db='ai_work_demo',
                       charset='utf8')

# 创建游标获取cursor对象jd
cursor = conn.cursor()

# 执行sql语句
# sql = "delete from ai_tools where id=9"
#更新数据语句
sql="update  ai_tools  set status=1 where id=4"

#
try:
    row_count = cursor.execute(sql)
    print(f"收到{row_count}行数据")
    if row_count != 1:
        print(f"期望增加一行，但是实际改变了{row_count}行")
        conn.rollback()
    else:
        print("执行成功!")
    # 提交事物
    conn.commit()

except Exception as e:
    print(e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

