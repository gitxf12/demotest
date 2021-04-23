list = [1,2,3,4,5,6,7,8,9]

i = 0
a = 0


while a < len(list):
    while i < len(list)-1:
        if list[i]<list[i+1]:
           z = list[i]
           list[i]=list[i+1]
           list[i+1]=z
        i=i+1
    a=a+1
    i=0

print(list)