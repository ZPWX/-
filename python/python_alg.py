num = 1
sum = 0
while num <= 100:
    if num % 2 == 0:
        sum = sum + num
    num += 1
print(sum)

i = 100
while i <= 999:
    a = i // 100
    b = i % 10
    if a == b:
        print(i)
    i += 1

#j = 1
#while j <= 5:
#    i = 1
#    while i <= 3:
#        print(i)
#        i += 1
#    j += 1


j = 1
while j <= 5:
    i = 1
    while i <= j:
        print("*" , end = "")
        i += 1
    print()
    j += 1


j = 1
while j <= 9:
    i = 1
    while i <= j:
        print("%d*%d=%d" % (i , j , i*j ),end="\t")
        i += 1
    print()
    j += 1
    #遍历
list1 = [1,2,3,4,5]
print(list1)
for data in list1:
    print(data)

i = 0
while i < 5:
    print("hello")
    i += 1

for _ in range(3):
    print("world")
    #排序
r = range(1,5)
print(list(r))
    #逆序
list2 = [1,2,3,4,5]
list2.sort(reverse=True)
print(list2)
    #利用切片执行逆序操作
print(list1[::-1])
    #插入
list2.insert(2,6)
print(list2)
    #合并
list1.extend(list2)
print(list1)
print(list2 + list1)
    #查找
print(3 in list1)
    #初始化推导式
list3 = [i for i in range(1,5)]
print(list3)
list3 = [i for i in range(1,5) if i % 2 ==0]
print(list3)
    #可变参数
def sum(*args):
    sums = 0
    for num in args:
        sums += num
    print(sums)

sum(1,2,3,4,5)
    #递归调用
def sum1(num):
    if num == 1:
        return 1
    return sum1(num-1)+num
print(sum1(100))
    #匿名函数的定义
c = (lambda a,b : a + b) (3,4)
print(c)
