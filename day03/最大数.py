
net = 1
num = 0
n = 0
while net < 11:
    print("请输入第",net,"个数字：")
    a = int(input())
    num = num+a
    if a > n:
        n = a

    net = net + 1

print("输入数字的总和是：",num)
print("输入的最大数是：",n)
print("输入数字的平均数是：",num/(net-1))


