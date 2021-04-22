a = 0
b = 0
c = 0
net = 1
while net < 4:
    print("请输入第",net,"条边长：")
    num = int(input())
    if net < 2:
        a = num
    elif net < 3:
        b = num
    else:
        c = num
    net = net + 1

if (a+b>c)and(a+c>b)and(b+c>a):
    if a == b and a == c:
        print("构成等边三角形")
    elif a==b or a==c or b==c:
        print("构成等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("构成直角三角形")
    else:
        print("构成普通三角形")
else:
    print("不能构成三角形")
