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
