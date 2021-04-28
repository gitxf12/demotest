
'''
    商城：
        1.商品
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1够了，就添加我的购物车，薪资减去相对应的金额
            4.2不够，买其他的。
        继续买东西，一直到输入Q获取q，退出
'''

shop = [
    ["lenovo thinkpad e580",5000],  # 0
    ["ipad 2021",3000],   # 1
    ["华为手表",3000], #
    ["辣条",100],
    ["大米",50],
    ["旺财QQ糖",50],
    ["卡通模型",500],
    ["汽车玩具",120],
    ["遥控飞机玩具",630],
    ["网球套装",1800],
    ["手套",25],
    ["篮球",430],
]

# 2.初始化自己的薪资
salary = input("请输入您的薪资：")
salary = int(salary)
A = salary
# 我的购物车
mycart = []
import random
lt = 0
yhj=random.randint(0,4)
if yhj == 1:
    print("恭喜您抽中1张辣条优惠券：满600减300")
    y=1
else:
    print("恭喜您抽中1张Lenovo电脑优惠券：半折甩卖")
    y=2
while True:
    # 3.展示商品
    for index,value in enumerate(shop): #enumerate()枚举：将所有的可能都列举出来
        print(index,"  ",value)
    # 4.输入要买的编号:num 是商品编号
    num = input("请输入您要买的商品编号：")

    # 若是 0 1 2 3 4 5 6 7 8 9 ，  若是  Q或者q  ,  输入非法
    if num.isdigit():
        num = int(num) # 转换成数字
        # 判断是否有这个商品
        if num > len(shop)-1:  # 不存在
            print("商品不存在！！！请重新输入！！！")
        else:
            # 可以买东西
            if salary >= shop[num][1]:  # 某个商品的价格:正常买
                # 添加到购物车
                mycart.append(shop[num])  # 添加购物车
                salary = salary - shop[num][1]  # 减去金额
                i = 0
                j = 0
                while i < len(mycart):
                    if mycart[i][0] == "辣条" and y == 1:
                        lt = lt+mycart[i][1]
                        if lt == 600:
                            salary = salary + 300
                            print("您成功使用了辣条满600减300优惠券！余额为：", salary,"元")
                            y=0
                            break
                        else:
                            print("您还有一张优惠券未用：辣条满600减300优惠券！")
                            break
                    elif i < len(mycart)-1:
                        i = i + 1
                    else:
                        break
                while j < len(mycart):
                    if mycart[j][0] == "lenovo thinkpad e580" and y == 2:
                        salary = salary + mycart[j][1]/2
                        print("您成功使用了Lenovo电脑优惠券：半折甩卖,余额为：", salary,"元")
                        y=0
                        break
                    elif j < len(mycart)-1:
                        j = j + 1
                    else:
                        break
                print("成功添加到购物车！！！余额为：", salary,"元")
            else:
                print("对不起，穷鬼，您的金额不足！！！！！")
    elif num == "Q" or num == "q":
        print("------------欢迎下次光临！！！！----------")
        break
    else:
        print("输入非法！请重新输入！购买完毕请按 Q 或 q")

# 打印购物小条：
print("您本次购物商品如下：")
for index,value in enumerate(mycart):
    print(index,"  ",value)
print("您的余额为：",salary,"元，本次购物获得：",(A-salary)/10,"积分")


