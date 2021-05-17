class Person:
    def per(self, name, sex, age):
        print(name, sex, age)
class Worker(Person):
    def word(self):
        print("干活")

class Student(Person):
    num = 0
    def study(self,num):
        print("学习，他的学号是：",num)
    def sing(self,num):
        print("唱歌，他的学号是：",num)

class Test(Person):
    person = Person()
    person.per(name="张三", sex="男", age=22)
    worker = Worker()
    worker.word()
    student = Student()
    student.study(num=1001)
    student.sing(num=1002)
