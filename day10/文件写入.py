f = open(file="古诗.txt",mode="r+",encoding="utf-8")
f1 = open(file="bk.txt",mode="w+",encoding="utf-8")
data = f.read()
f1.write(data)



f1.close()
f.close()
