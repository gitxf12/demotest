a = [1,5,21,30,15,9,30,24]
l = 0
z = 0
#print(len(a))
while l < len(a):
    if a[l]%5==0:
        z = z + a[l]
        l = l +1
    else:
        l = l + 1
print("其中是5的倍数之和是：",z)