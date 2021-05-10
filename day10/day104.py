
info = '''
+++++++++++++++++++++++++++++++
-----------欢迎进入系统-----------
------请选择对应服务的数字----------
------1.注册--------------------
------2.登录--------------------
------3.修改密码-----------------
------4.上传头像-----------------
++++++++++++++++++++++++++++++++
'''


users = []
f = open(file="Names.txt",mode="r+",encoding="utf-8")
data = f.readlines()
f.close()
for i in data:
    da = i.replace("\n","").split(",")
    users.append(da)

# 注册
zc = []
def zhuC():
    name = input("请输入要注册的用户名：")
    password = input("请输入您的密码：")
    gender = input("请输入您的性别：")
    age = input("请输入您的年龄：")
    address = input("请输入您的地址：")
    zc.append(name)
    zc.append(password)
    zc.append(gender)
    zc.append(age)
    zc.append(address)
    users.append(zc)
    print("注册成功！")



# 登录
def dengL():
    while True:
        name = input("请输入用户名：")
        password = input("请输入您的密码：")
        # 跟缓存区校验
        a = 0
        for i in users:
            if name == i[0] and password == i[1]:
                a = 1
                break
        if a == 1:
            print("登陆成功！")
        elif a == 0:
            print("登陆失败！")
        break



# 修改密码
def xiuG():
    while True:
        name = input("请输入用户名：")
        password = input("请输入您的密码：")
        # 跟缓存区校验
        a = 0
        for i in users:
            if name == i[0] and password == i[1]:
                password1 = input("请输入您修改后的密码：")
                i[1] = password1
                a = 1
                break
        if a == 1:
            print("修改密码成功！")
        else:
            print("用户名或密码输入错误！")
        break

# 上传头像
def shangC():
    while True:
        name = input("请输入用户名：")
        password = input("请输入您的密码：")
        b = 0
        for i in users:
            if name == i[0] and password == i[1]:
                jpg = input("请输入头像地址：")
                i.append(jpg)
                f1 = open(file=jpg, mode="rb")
                f2 = open(file="头像.jpg", mode="wb")
                f3 = open(file="Names.txt", mode="a", encoding="utf-8")
                data = f1.read()
                f2.write(data)
                f3.write(str(i))
                f1.close()
                f2.close()
                b = 1
                break
        if b == 1:
            print("上传成功！")
        else:
            print("上传失败！")
        break






while True:
    print(info)
    num = input("请输入对应服务的数字：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            zhuC()
        if num == 2:
            dengL()
        if num == 3:
            xiuG()
        if num == 4:
            shangC()
        if num == 5:
            print("退出系统！")
            break

    else:
        print("输入非法！")



