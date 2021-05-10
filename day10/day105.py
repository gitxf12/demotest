import re

f = open(file="scores.txt", mode="r+", encoding="utf-8")
f1 = open(file="scoresSum.txt", mode="w+", encoding="utf-8")
names = []
num = []
zNum = []
nameNum = {}
data = f.readlines()
for i in data:
    names.append(re.sub("\d", "", i).replace("\n",""))

    num.append(re.sub("\D",",",i).split(","))

for i in num:
    nums = list(filter(None,i))
    n = [int(i) for i in nums]
    a = 0
    zn = 0
    while True:
        if a < len(n):
            zn = zn + n[a]
            a = a + 1

        else:
            zNum.append(zn)
            break

b = 0
while b < len(names):
    nameNum[names[b]] = zNum[b]
    b = b + 1

f1.write(str(nameNum))
f1.close()
f.close()


