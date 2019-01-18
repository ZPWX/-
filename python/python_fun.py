def sum(a):
    #用于计算指定数字和#
    i = 1
    sums = 0
    while i <= a:
        sums += i
        i += 1
    print(sums)

sum(10)
# 成员方法的调用
class Cat:
    def catch(self):

        self.jump()
        self.grasp()
        self.bite()

    def jump(self):
        print("jump")
    def grasp(self):
        print("grasp")
    def bite(self):
        print("bite")
cat1 = Cat()
cat1.catch()
# 私有成员变量的调用
class Card:
    def __init__(self):
        self.card_id = None
        self.__pwd = None

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self,pwd):
        self.__pwd = pwd

c = Card()
c.set_pwd("gxtao")
print(c.get_pwd())
"""
# 类变量
class Cat1:
    subject = "cat"
    def _init_(self, type, name):
        self.__type = type
        self.__name = name
    def get_type(self):
        # print("bosicat")
        return self.__type
    def set_type(self,type):
        self.__type = type
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
cat1 = Cat1("bosicat","shortcat")
cat2 = Cat1("bosicat","hadsome")
"""
# 类方法
class Chinese:
    country = "China"
    def __init__(self,id,name):
        self.id = id
        self.name = name
    @classmethod
    def show_country(cls): #类方法的定义
        print("i'am chinese")

