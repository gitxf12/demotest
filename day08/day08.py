import pymysql

con = pymysql.connect(host="localhost",user="root",password="123456",database="销售数据库")

cursor = con.cursor()

sql = "insert into article values('s005','手机','3600','120')"

num = cursor.execute(sql)

print("共",num,"行数据收到影响！！！")

con.commit()

cursor.close()
con.close()