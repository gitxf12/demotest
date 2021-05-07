import pymysql
from DBUtils import select
from DBUtils import update
from DBUtils import close
# 确定用户库
bank = {}
# 确定银行的开户名称
bank_name = "中国工商银行昌平区回龙观支行"

info = '''
    *********************************
    *    中国工商银行账户管理系统     *
    *********************************
    *   1.开户                      *
    *   2.存款                      *
    *   3.取款                      *
    *   4.转账                      *
    *   5.查询账户                  *
    *   6.Bye！                     *
    ********************************
'''
import random

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    # 判断数据库是否已满
    sql1 = "select  count(*)  from user";
    data = select(sql1,[])
    if data[0][0] >= 100:  #如果返回的统计数据超出100，则已满
        return 3
    # 判断数据是否存在改用户
    # 获取所有键，然后在判断是否有
    sql2 = "select * from user  where  account = %s"
    param2 = [account]
    data2 = select(sql2,param2)
    if len(data2) != 0: # 如果通过sql语句能查到数据并且不为空，则说明改用户已存在
        return 2
    # 正常开户：insert into 表  ，否则则执行存储数据操作
    sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param3 = [account,username,password,country,province,street,door,money,bank_name]
    update(sql3,param3)
    return 1

# 存款逻辑
def bank_deposit(account,money):
    sql = "select * from user where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) != 0:
        sql1 = "update user set money=money+%s where account = %s"
        param1 = [money,account]
        update(sql1,param1)
        return True
    else:
        return False

# 取款逻辑
def bank_getMoney(account,password,money):
    sql = "select * from user where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) == 0:
        return 1
    sql1 = "select password from user where account = %s"
    data = select(sql1,param)
    if data[0][0] != password:
        return 2
    sql2 = "select money from user where account = %s"
    data = select(sql2,param)
    if data[0][0] < money:
        return 3
    # 正常取款
    sql3 = "update user set money=money-%s where account = %s"
    param1 = [money,account]
    update(sql3,param1)
    return 0

# 转账逻辑
def bank_transfer_accounts(account,accounts,password,money):
    sql = "select account from user where account=%s"
    sq = "select account from user where account=%s"
    param = [account]
    par = [accounts]
    data = select(sql,param)
    d = select(sq,par)
    if len(data) == 0 and len(d) == 0:
        return 1
    sql1 = "select password from user where account = %s"
    param1 = [account]
    data = select(sql1,param1)
    if data[0][0] != password:
        return 2
    sql2 = "select money from user where account = %s"
    data = select(sql2,param1)
    if data[0][0] < money:
        return 3
    # 正常转账
    sql3 = "update user set money=money-%s where account = %s"
    parma3 = [money,account]
    update(sql3,parma3)
    sql4 = "update user set money=money+%s where account = %s"
    parma4 = [money,accounts]
    update(sql4,parma4)
    return 0


# 查询逻辑
def bank_query(account,password):
    sql = "select account from user where account = %s"
    param = [account]
    data = select(sql,param)
    if len(data) == 0:
        print("该用户不存在！！！")
    sql1 = "select password from user where account = %s"
    data = select(sql1,param)
    if data[0][0] != password:
        print("密码输入错误！！！")

    # 正常查询
    print("查询成功！")
    sql2 = "select * from user where account = %s"
    data = select(sql2,param)
    print(data)
    info = '''
                ------------个人账户信息----------------
                账号：%s,
                用户名：%s,
                取款密码：%s,
                地址信息：
                    国家：%s,
                    省份：%s,
                    街道：%s,
                    门牌号：%s,
                余额：%s,
                开户行：%s
                -----------------------------------
            '''
    print(info % (data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8]))


# 开户方法
def addUser():
    # 生成账号：  8位随机
    string = ""  # 随机数缓冲
    for i in range(8):  # 循环8次取字符

        string = string + "1234567890"[random.randint(0,9)]  # 拼接

    account = string
    print("账号为：",account)
    username = input("请输入姓名：")
    password  = input("请输入密码：")
    print("接下来输入地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street = input("\t输入街道：")
    door = input("\t输入门牌号：")
    money = int(input("请初始化您的余额："))

    # 调用银行的开户方法
    s = bank_addUser(account,username,password,country,province,street,door,money)

    if s == 1:
        print("开户成功！")
        print("以下是您的开户个人信息：")
        print("***********************")
        print("账号：",account)
        print("用户名：", username)
        print("密码：******")
        print("国家：", country)
        print("省份：", province)
        print("街道：", street)
        print("门牌号：", door)
        print("账户余额：", money)
        print("******************开户行地址：", bank_name)

    elif s == 2:
        print("该用户已存在！")
    elif s ==  3:
        print("对不起，该银行已满！请携带证件到其他银行办理！")

# 存款
def addMoney():
    account = input("请输入您的账号：")
    money = input("请输入存款金额：")
    money = int(money)
    sta = bank_deposit(account,money)
    if sta == True:
        print("成功存入：", money, "元")
    elif sta == False:
        print("存款失败！！！该账号不存在！！！")
    else:
        print("网络繁忙！请稍后重试！")

# 取款
def getMoney():
    account = input("请输入您的账号：")
    password = input("请输入您的密码：")
    password = int(password)
    money = input("请输入取款金额：")
    money = int(money)
    sta = bank_getMoney(account,password,money)
    if sta == 0:
        print("取款成功！！！取出：",money,"元")
    elif sta == 1:
        print("取款失败！！账号输入有误！！！")
    elif sta == 2:
        print("取款失败！！密码输入有误！！！")
    elif sta == 3:
        print("取款失败！！当前余额不足！！！")
    else:
        print("网络繁忙！请稍后重试！")

# 转账
def transferAccounts():
    account = input("请输入您的账号：")
    accounts = input("请输入您要转入的账号：")
    password = input("请输入您的密码：")
    password = int(password)
    money = input("请输入转账金额：")
    money = int(money)
    sta = bank_transfer_accounts(account,accounts,password,money)
    if sta == 0:
        print("转账成功！！！转出：",money,"元")
    elif sta == 1:
        print("转账失败！！账号输入有误！！！")
    elif sta == 2:
        print("转账失败！！密码输入有误！！！")
    elif sta == 3:
        print("转账失败！！当前您的账户余额不足！！！")
    else:
        print("网络繁忙！请稍后重试！")


# 查询
def queryUser():
    account = input("请输入您的账号：")
    password = input("请输入您的密码：")
    password = int(password)
    bank_query(account,password)


while True:  # 一直循环的进入选项
    print(info)
    chose = input("请输入您的选项：")
    if chose == "1": # 判断是否是1
        addUser()
    elif chose == "2": # 判断是否是2
        addMoney()
    elif chose == "3":  # 判断是否是3
        getMoney()
    elif chose == "4":  # 判断输入的是否是4
        transferAccounts()
    elif chose == "5": # 判断输入的是否是5
        queryUser()
    elif chose == "6":   # 判断输入的是否是6，若是6则需要退出 break
        close()
        print("拜拜了您嘞！")
        break
    else:
        print("输入非法！重新输入！")





















