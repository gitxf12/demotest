class Cook:
    __name = ""
    __age = 0
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
    def cook_rice(self):
        print()

class Cooks(Cook):
    def fry_food(self):
        print()

class Cookes(Cooks):
    def cook_rice(self):
        print("蒸饭")
    def fry_food(self):
        print("炒菜")

class Test(Cooks):
    cook = Cook()
    cook.setName("王五")
    cook.setAge(25)
    print(cook.getName(),cook.getAge())
    cookes = Cookes()
    cookes.cook_rice()
    cookes.fry_food()






