import random
print("*_________________________________*")
print("|            中国工商银行           |")
print("|            账户管理系统           |")
print("*_________________________________*")
print("|-------------1.开户--------------|")
print("|-------------2.存款--------------|")
print("|-------------3.取款--------------|")
print("|-------------4.转账--------------|")
print("|-------------5.查询--------------|")
print("|-------------6.退出--------------|")
print("*_________________________________*")

num=["12345678","23456789"]
numE=[10000,3000]
numPassWord=[123456,121212]
numName=["张三","李四"]
numD=["北京","南京"]
numH=["昌平分行","南京分行"]
#请输入要办理业务的编号
code=0
while code < 6:
    code = input("1.开户2.存钱3.取钱4.转账5.查询6.退出\n请输入您要办理业务的编号：")
    if code.isdigit():
        code = int(code)
        if code == 1:
            print("----<<<<开户>>>>----")
            zh = random.randint(9999999, 100000000)
            i = 0
            if len(num) > 99:
                print("用户库已满")
                break
            while i < len(num):
                zh = str(zh)
                if num[i]==zh:
                    print("该账号已存在")
                    break
                elif i < len(num)-1:
                    i = i + 1
                else:
                    print("生成账号：", zh)
                    name = input("请输入姓名：")
                    passWord = input("请输入密码：")
                    passWord = int(passWord)
                    d = input("请输入地址：")
                    e = input("请输入存款数额：")
                    e = int(e)
                    h = input("请输入开户行：")
                    num.append(zh)
                    numName.append(name)
                    numPassWord.append(passWord)
                    numD.append(d)
                    numE.append(e)
                    numH.append(h)
                    info = '''
                    ++++++++添加用户成功+++++++++
                    账号：%s
                    姓名：%s
                    密码：%s
                    地址：%s
                    存款余额：%s
                    开户行：%s
                    +++++++++++++++++++++++++++
                    '''
                    print(info % (zh, name, passWord, d, e, h))
                    break


        # 存款
        elif code == 2:
            print("----<<<<存款>>>>----")
            zh = input("请输入您的账号：")
            ea = input("请输入存款金额：")
            i = 0
            while i < len(num):
                if num[i] == zh:
                    ea = int(ea)
                    numE[i] = numE[i] + ea
                    print("成功存入：", ea, "元，当前余额：", numE[i], "元")
                    break
                elif i < len(num) - 1:
                    i = i + 1
                else:
                    print("账号输入有误")
                    break
        # 取款
        elif code == 3:
            print("----<<<<取款>>>>----")
            zh = input("请输入您的账号：")
            passWord = input("请输入您的密码：")
            eb = input("请输入取款金额：")
            i = 0
            while i < len(num):
                if num[i] == zh:
                    passWord = int(passWord)
                    if numPassWord[i] == passWord:
                        eb = int(eb)
                        if eb < numE[i]:
                            numE[i] = numE[i] - eb
                            print("成功取款：", eb, "元--当前余额：", numE[i], "元")
                            break
                        else:
                            print("当前余额不足")
                            break
                    else:
                        print("输入密码有误")
                        break
                elif i < len(num) - 1:
                    i = i + 1
                else:
                    print("输入账号有误")
                    break
        # 转账
        elif code == 4:
            print("----<<<<转账>>>>----")
            zh = input("请输入您的账号：")
            i = 0
            j = 0
            while i < len(num):
                if num[i] == zh:
                    zha = input("请输入您要转入的账号：")
                    while j < len(num):
                        if num[j] == zha and zh != zha:
                            passWord = input("请输入您的密码：")
                            passWord = int(passWord)
                            m = i
                            if passWord == numPassWord[m]:
                               ec = input("请输入转账金额：")
                               ec = int(ec)
                               if numE[i] > ec:
                                   numE[i] = numE[i] - ec
                                   numE[j] = numE[j] + ec
                                   print("转账成功，转出", ec, "元，当前余额：", numE[i], "元")
                                   break
                               else:
                                   print("余额不足")
                                   break
                            else:
                               print("输入密码有误")
                               break
                        elif j < len(num) - 1:
                            j = j + 1
                        else:
                            print("输入转入账号有误")
                            break
                elif i < len(num) - 1:
                    i = i + 1
                else:
                    print("输入账号有误")
                    break
                break
        # 查询
        elif code == 5:
            print("----<<<<查询>>>>----")
            zh = input("请输入您的账号：")
            i = 0
            while i < len(num):
                if zh == num[i]:
                    passWord = input("请输入您的密码：")
                    passWord = int(passWord)
                    numPassWord.append(passWord)
                    if passWord == numPassWord[i]:
                        info = '''
                                    ++++++++查询用户成功+++++++++
                                    账号：%s
                                    姓名：%s
                                    密码：%s
                                    地址：%s
                                    存款余额：%s
                                    开户行：%s
                                    +++++++++++++++++++++++++++
                                    '''
                        print(info % (num[i], numName[i], numPassWord[i], numD[i], numE[i], numH[i]))
                        break
                    else:
                        print("输入密码有误")
                        break
                elif i < len(num) - 1:
                    i = i + 1
                else:
                    print("输入账号有误")
                    break

        elif code == 6:
            print("感谢您对本系统的使用，期待您再次光临!!!")
            break
        else:
            print("您输入的编号有误，请输入上方提示内容内的编号！！！")

    else:
        print("您输入的编号有误，请输入上方提示内容内的编号！！！")