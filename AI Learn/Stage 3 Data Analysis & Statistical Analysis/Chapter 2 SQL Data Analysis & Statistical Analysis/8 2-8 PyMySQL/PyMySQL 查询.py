# 1. 导入模块
import pymysql
import time
# 2. 创建连接对象
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='',
                       db='db_mysql_learn',
                       charset='UTF8MB4')
# 3. 获取游标对象
cursor = conn.cursor()

# 4. 定义SQL语句
sql = "SELECT * FROM students;"

# 5. 执行SQL语句
row_count = cursor.execute(sql)
print(f"受影响的行数: {row_count}")

# 6. 获取查询结果
# fetch_one()
for row in cursor.fetchall():
    print(row)

# 7. 关闭游标对象与连接对象
cursor.close()
conn.close()