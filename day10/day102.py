
f1 = open(file="E:/course/day10/tea.jpg",mode="rb")
f2 = open(file="E:/demo/day10/tea.jpg",mode="wb")

data = f1.read()
f2.write(data)

f2.close()
f1.close()