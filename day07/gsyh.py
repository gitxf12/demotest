import random
# 1. 空的银行的库 ： 100个
users = {
'6104a598':{'username': '张三', 'password': 123456, 'country': '中国', 'province': '北京', 'street': '昌平大街', 'door': '0101', 'money': 10000, 'bank_name': '中国工商银行的昌平支行'},
'12345678':{'username': '李四', 'password': 123123, 'country': '中国', 'province': '南京', 'street': '阳光大街', 'door': '0601', 'money': 5000, 'bank_name': '中国工商银行的南京支行'}
}
# 2.银行的名称写死
bank_name = "中国工商银行的昌平支行"

# 打印欢迎页面
def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    if len(users) >= 100:
        return 3

    # 判断是否存在
    if account in users:
        return 2

    #正常开户
    users[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1

# 存款逻辑
def bank_deposit(account,money):
    if account in users:
        users[account]["money"]=users[account]["money"]+money
        return True
    else:
        return False

# 取款逻辑
def bank_getMoney(account,password,money):
    if account not in users:
        return 1
    if password != users[account]["password"]:
        return 2
    if money > users[account]["money"]:
        return 3
    # 正常扣款
    users[account]["money"]=users[account]["money"]-money
    return 0

# 转账逻辑
def bank_transfer_accounts(account,accounts,password,money):
    if account not in users or accounts not in users:
        return 1
    if password != users[account]["password"]:
        return 2
    if money > users[account]["money"]:
        return 3
    # 正常转账
    users[account]["money"]=users[account]["money"]-money
    users[accounts]["money"]=users[accounts]["money"]+money
    return 0

# 查询逻辑
def bank_query(account,password):
    if account not in users:
        print("该用户不存在！！！")
    if password != users[account]["password"]:
        print("输入密码错误！！！")
    # 正常查询
    print("查询成功！")
    info = '''
                ------------个人信息----------------
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
    print(info % (account,users[account]["username"],password,users[account]["country"],users[account]["province"],users[account]["street"],users[account]["door"],users[account]["money"],bank_name))

# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    password = int(password)
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
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
        print(info % (account,name,password,country,province,street,door,users[account]["money"],bank_name))
    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

# 存款
def addMoney():
    account = input("请输入您的账号：")
    money = input("请输入存款金额：")
    money = int(money)
    sta = bank_deposit(account,money)
    if sta == True:
        print("成功存入：", money, "元，当前余额：", users[account]["money"], "元")
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
        print("取款成功！！！取出：",money,"元，还剩余额：",users[account]["money"],"元")
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
        print("转账成功！！！转出：",money,"元，还剩余额：",users[account]["money"],"元")
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


while True:
    welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()
        elif num == 2:
            addMoney()
        elif num == 3:
            getMoney()
        elif num == 4:
            transferAccounts()
        elif num == 5:
            queryUser()
        elif num == 6:
            print("拜拜了您嘞，欢迎下次光临！！！")
            break
        else:
            print("输入非法！请重新输入！！！别瞎弄！！！")
    else:
        print("您输入非法！请重新输入！！！")
