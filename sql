import sqlite3
import random
con=sqlite3.connect("sql.db")
cur=con.cursor()

sql_table="CREATE TABLE movie(title,year,score)"
#cur.execute(sql_table)
con.commit()

sql_insert="INSERT INTO movie values('TITLE_0',2000,8.5),('TITLE_1',2023,9.1)"
cur.execute(sql_insert)

for i in range(100):
    a="title_"+str(i)
    b=random.randrange(2000,2023,1)
    c=random.randrange(5,9)
    sql_insert_1=INSERT INTO movie values(a,b,c)
    cur.execute(sql_insert_1)
con.commit()

sql_query="SELECT title,year,score FROM movie"
record=cur.execute(sql_query)
print(record.fetchall())


cur.close()
con.close()