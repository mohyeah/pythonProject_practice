# 1. 导入模块
import pymysql

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
sql = "INSERT INTO students VALUES (NULL, 'Lily', 22, 'male', 98.0, 3)"

# 5. 执行SQL语句
cursor.execute(sql)
conn.commit()   # 提交修改
print(f"受影响的行数: {cursor.rowcount}")

# 6. 关闭游标和连接对象
cursor.close()
conn.close()