# li = [1,3,55,4,6,9,7]
# print(li)
# li.append(11)
# print(li)
# li[2]=4
# print(li)
# li.remove(1)
# print(li)
# li.remove(li[1])
# print(li)

names = ["小明","小刚","小红","小刘"]
import random
while True:  # 死循环
    print("1：随机点名.   2：随机处罚>>>:")
    num = input("请输入编号：")
    # 判断num是不是数字，若是，则转换int，若不是就不转换了
    if num.isdigit():  # isdigit判断是否能看成数字
        num = int(num)   # 如果能看成，则转换成整型
        if num == 1:
            rannum = random.randint(0,len(names)-1)  # 随机从0~列表长度产生一个编号
            print(names[rannum])  # 随机打印姓名
        elif num == 2:
            a = random.randint(0,100)
            print("恭喜您！您已被处罚",a,"遍！")
    elif num == "q" or num == "Q":
        print("欢迎下次光临！！！")
        break # 跳出循环
    else:
        print("对不起，您的输入非法！请重新输入！！！！")



