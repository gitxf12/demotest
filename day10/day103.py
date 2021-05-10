

jpg = input("请输入您要上传证件的路径：")
f = open(file=jpg, mode="rb")
f1 = open(file="证件上传.jpg", mode="wb")

data = f.read()
f1.write(data)

f.close()
f1.close()
print("上传成功！")