import pymysql
host = "localhost"
database="银行数据库"
user="root"
password="123456"

# 可以处理增，删，改的所有操作
def update(sql,param):
    con = pymysql.connect(host=host,database=database,user=user,password=password)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()  # 提交数据

# 可以处理查询所有操作
def select(sql,param,mode="many",size=0):
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()  # 提交数据
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

# 关闭
def close():
    con = pymysql.connect(host=host, database=database, user=user, password=password)
    cursor = con.cursor()
    cursor.close()
    con.close()








