# coding= utf-8
import pymysql
'''
源码
:param host: Host where the database server is located
    :param user: Username to log in as
    :param password: Password to use.
    :param database: Database to use, None to not use a particular one.
    :param port: MySQL port to use, default is usually OK. (default: 3306)
'''
dbinfo=\
	{
		'host':'127.0.0.1',
		'user': 'root',
		'password':'123456',
		'database':'myworkplace',
		'charset': 'utf8mb4'
	}
conn=pymysql.connect(**dbinfo)
cursor=conn.cursor()
result=cursor.execute('create TABLE if not EXISTS testConnetDB(id int PRIMARY  KEY AUTO_INCREMENT ,name varchar(20))')
conn.autocommit(1)
print('result',result)
if result!=0:
	print('create table success!')
# 插入数据测试10
for i in range(1,10):
	insert_sql=" insert into testConnetDB(NAME) VALUES ('meizi%s')"
	cursor.execute(insert_sql%i)
	conn.commit()
# 删除数据
# delete_sql="DELETE FROM testconnetdb WHERE NAME LIKE '%meizi%'"
# cursor.execute(delete_sql)
# 更新数据
# update_sql="UPDATE testconnetdb SET NAME=%s WHERE NAME=%s"
# params=('同学','tongxue')
# cursor.execute(update_sql,params)
conn.close()


'''
'create table user (id varchar(20) primary key, name varchar(20))'
'''