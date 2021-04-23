List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
i=0
while i < len(List):
    a = List.count(List[i])
    if a > 1:
        print(List[i],"重复了：",a-1,"次")
        i=i+1




