# coding= utf-8
from openpyxl.workbook import Workbook
import pymysql
wb = Workbook()
ws1 = wb.active
# # active[param]方法是 获取当前的工作空间，param是Excel中的列表名，A开头数字表示行号。
ws1.title=u'测试'
# 连接数据库，将数据库的东西写到Excel中
# 连接数据库
dbinfo=\
	{
		'host':'127.0.0.1',
		'user': 'root',
		'password':'123456',
		'charset': 'utf8mb4'
	}

conn=pymysql.connect(**dbinfo)
# 命名数据库
database='myworkplace'
conn.select_db(database)
# 创建数据库操作对象
cursor=conn.cursor()
# 编写SQL语句
sql='select * from %s'

# 选取表名
table_name='testconnetdb'
# 调用执行方法获取数据
cursor.execute(sql%table_name)
# 获取结果集
results=cursor.fetchall()
#给出表的标题
col_nul=1;
ws1['A'+str(col_nul)]='编号'
ws1['B'+str(col_nul)]='名字'
for result in results :
	col_nul+=1
	id=result[0]
	#将编码写入到表中
	ws1['A'+str(col_nul)]=id
	name=result[1]
	#将姓名写入到表中
	ws1['B'+str(col_nul)]=name
# 将数据写入到Excel中

# def create_sheet(self, title=None, index=None):
# Create a worksheet (at an optional index).
#
# :param title: optional title of the sheet
# :type title: unicode
# :param index: optional position at which the sheet will be inserted
# :type index: int

# 保存文件
wb.save('test.xlsx')
print('done!')


