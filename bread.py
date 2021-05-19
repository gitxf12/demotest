import threading
import time

sum = 0
data = 3
class Provider(threading.Thread):
    d = 0
    def run(self) -> None:
        global sum
        global data
        while data > 0:
            if sum < 300:
                sum = sum + 1
                time.sleep(1)
                data = data - 1
                print("造成一块面包，篮子现有",sum,"块面包")
            else:
                print("厨师休息中...")
                time.sleep(3)
        print("一共做了",sum+c1.s+c2.s+c3.s+c4.s+c5.s,"块")

class Client(threading.Thread):
    n = ""
    s = 0
    def run(self) -> None:
        global sum
        global data
        while data > 0:
            if sum > 0:
                self.s = self.s + 1
                print(self.n,"成功抢购一块面包,一共抢购了",self.s,"块")
        print(self.n,"一共消费了", self.s*10, "元")

class Data(threading.Thread):
    def run(self) -> None:
        global data
        for i in range(data):
            time.sleep(1)
            data = data - 1
        return data

d = Data()
d.start()

p = Provider()
p1 = Provider()
p2 = Provider()
p3 = Provider()
p4 = Provider()
c1 = Client()
c2 = Client()
c3 = Client()
c4 = Client()
c5 = Client()
c1.n = "一号"
c2.n = "二号"
c3.n = "三号"
c4.n = "四号"
c5.n = "五号"
p.start()
p1.start()
p2.start()
p3.start()
p4.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()





