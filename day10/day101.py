import pymysql
con = pymysql.connect(host="localhost", database="day10", user="root", password="123456")
cursor = con.cursor()

f = open(file="用户数据.txt", mode="r+", encoding="utf-8")
data = f.readlines()
users = []
for i in data:
    d = i.replace("\n","").split(",")
    users.append(d)

for i in users:
    cursor.execute("insert into 资产表 values('%s',%s,%s)"%(i[0],i[1],i[2]))
    con.commit()

cursor.execute("select sum(净资产) from 资产表")
money = cursor.fetchone()
print("资产总和==",money[0])
f.close()
cursor.close()
con.close()

