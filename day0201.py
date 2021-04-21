code = input("请输入您的身份证编号：")
name = input("请输入您的姓名：")
gender = input("请输入您的性别：")
age = input("请输入您的年龄：")
herght = input("请输入您的身高：")
live = input("请输入您的居住地址：")

info = '''
++++++++++个人信息++++++++++
身份证编号：%s，
姓名：     %s，
性别：     %s，
年龄：     %s，
身高：     %s，
居住地址：  %s
+++++++++++++++++++++++++++
'''
print(info % (code,name,gender,age,herght,live))
