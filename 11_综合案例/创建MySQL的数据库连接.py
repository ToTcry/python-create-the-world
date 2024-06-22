from pymysql import Connection


# 获取到MySQL数据库的链接对象
conn = Connection(
    host='localhost',       # 主机名
    port=3306,              # 端口
    user='root',            # 账户
    password='123456',      # 密码
)

# 打印MySQL数据库软件信息
print(conn.get_server_info())
# 获取油标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('test')

# 使用游标对象，创建table
# cursor.execute('create table test_pymysql(id int,info varchar(255))')
# cursor.execute('select * from test_pymysql')


# 使用游标对象，查询table
cursor.execute('select * from student')
results = cursor.fetchall()
for i in results:
    print(i)






# 关闭数据库的链接
conn.close()




