import csv
import re

import pyodbc
#import win32com.client

import random

from faker import Faker
import pyodbc

# 数据库文件
accessfile = r'D:\demo.accdb'

# 最高薪资(单位为K)
maxsalary = 30


def fakedata(maxtimes):
    # 模拟数据。人名+薪资
    fake = Faker('zh_CN')
    data_total = [[fake.name(), random.randint(0, maxsalary)]
                  for x in range(maxtimes)]
    return data_total


def operator(filename):
    fakesalary = fakedata(100)

    connection = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+filename+';')
    connection.autocommit = True

    # 创建工资表
    create_table_sql = '''create table salary_table ( id autoincrement primary key, name varchar(255) , salary int ) '''

    # 插入语句
    insert_table_sql = '''insert into salary_table(name, salary) values (?, ?) '''

    # 查询语句
    select_public_servant_sql = '''select * from salary_table where salary > 10 '''

    with connection.cursor() as cursor:
        # DDL
        cursor.execute(create_table_sql)

        # 插入数据
        for info in fakesalary:
            name = info[0]
            pay = info[1]
            cursor.execute(insert_table_sql, (name, pay))

        # 查询之
        cursor.execute(select_public_servant_sql)
        results = cursor.fetchall()
        for row in results:
            print(row)


operator(accessfile)