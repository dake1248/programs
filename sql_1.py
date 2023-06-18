import sqlite3
import random
dbName="sql_1.db"
table_name="movie"
con=sqlite3.connect(dbName)
cur=con.cursor()

sql="CREATE TABLE movie(title,year,score)"
cur.execute(sql)
con.commit()
#增加一列：
sql_add_column="ALTER TABLE movie ADD COLUMN note "
cur.execute(sql_add_column)
#增加表格内记录：
sql_insert="INSERT INTO movie VALUES('title_0',1975,8.2,10),('title_1',2023,8.5,20)"
for i in range(10):
	cur.execute(sql_insert)
#查询所有表格内容：
re=cur.execute("SELECT * from movie")
rec=re.fetchall()
print(rec)

#获取每行的数据并返回一个列表
#row 是逐行读取rec列表中的行数据
re=cur.execute("SELECT * from movie")
rec=re.fetchall()
for row in rec:
	print(rec)
	print("title:  "+row[0])
	print("year:  "+str(row[1]))
	print("score:  "+str(row[2]))
	print("note:  "+str(row[3]))
#获取表格名称：
sql_table="SELECT name FROM sqlite_master WHERE type='table'"
re=cur.execute(sql_table)
table=re.fetchall()
print(table)
print(table[0])
#获取表格内所有信息：
sql_all="SELECT * from sqlite_master"
re=cur.execute(sql_all)
rec=re.fetchall()
print(rec)

#更新表格内记录
sql_update="update movie set year=2000 where title='title_1'"
cur.execute(sql_update)
con.commit()
#删除表格内记录
sql_del="delete from movie where title='title_0'"
cur.execute(sql_del)
con.commit()
#删除表格
sql_drop_table="drop table if exists movie"
re=cur.execute(sql_drop_table)
rec=re.fetchall()
print(rec)
con.commit()


