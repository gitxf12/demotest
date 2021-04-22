name = "root"
password = "admin"
net = 1
while net < 4:
    a = input("请输入用户名：")
    if a == name:
        b = input("请输入密码：")
        if b == password:
            print("登录成功")
            break
        else:
            print("密码错误")
            net = net +1
            if net > 3:
                print("输入密码错误三次已被锁定")