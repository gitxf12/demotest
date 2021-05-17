import time
class OldPhone:
    __phoneName = ""
    def getPhoneName(self):
        return self.__phoneName
    def setPhoneName(self,phoneName):
        self.__phoneName = phoneName

    def call(self,name):
        print("正在给",name,"打电话")
        for i in range(6):
            time.sleep(1)
            print(".",end="")

class NewPhone(OldPhone):
    def call(self,name):
        super().call(name)
        print("语言拨号中...")
    def present(self):
        print("品牌为：",self.getPhoneName(),"的手机很好用...")

class Test(NewPhone):
    newPhone = NewPhone()
    newPhone.setPhoneName("oppo")
    newPhone.present()
    newPhone.call("张三")
