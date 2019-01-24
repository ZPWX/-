# 打印机：打印操作，并且生成打印的任务队列
# 经理：添加打印操作
# 职员：添加打印操作

class Manager:
    def use_printer(self,infor,pr):
        pr.add_task(infor)
class Staff:
    def use_printer(self,infor,pr):
        pr.add_task(infor)
class Printer:
    __instance = None
    __is_init = False
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
        return cls.__instance
    def __init__(self): #设置打印任务队列
        if Printer.__is_init == False:
            self.list_print = []
            Printer.__is_init = True 
    def add_task(self,infor): #添加打印任务到打印队列中
        self.list_print.append(infor)
    def print(self): #执行打印操作
        print(self.list_print)

'''经理操作'''
pr1 = Printer()
m1 = Manager()
m1.use_printer("hello",pr1)

'''员工'''
pr2 = Printer()
st1 = Staff()
st1.use_printer("itcast",pr2)

'''打印机'''
pr = Printer()
pr.print()
