import random
num = random.randint(0,100)
C = 0
j = 200

while C < 7 and j >= 100:
         m = input("请输入中奖号码：")
         m = int(m)
         C = C + 1
         j = j - 100
         if m > num:
            print("大了,您已猜了", C, "次，还剩", j, "金币")
         elif m < num:
            print("小了,您已猜了", C, "次，还剩", j, "金币")
         else:
            print("恭喜您猜中中奖号码：", num, "本次共猜了", C, "次，还剩", j, "金币")
            break

if C < 0:
    print("您猜号码已达上限")
else:
    print("您当前金币不足")

print("退出系统")


