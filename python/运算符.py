
name1 = "gxtao"
name2 = "gxtao"
print(name1 < name2)

name1 = "0"
name2 = "9"
print(name1 < name2)

office = True
money = True
print(office and money)
print(office + money) 

train = True
bus = False
print(train or bus)

score = 100
if score == 100:
    print("A")
elif score >= 60 and score < 100:
    print("B")
else:
    print("C")

week = int(input("input a number/string"))
if week == 1:
    print("A")
elif week == 2:
    print("B")

x = 0
if x >= 0:
    print("这个是正数")
    if x % 2 == 0:
        print("这个是偶数")
    else:
        print("这个是奇数")
else:
    print("这个是负数")

i = 0
while i < 5:
    print("hello python")
    i += 1

j = 1
while j <= 5:
    i = 1
    while i <= 3:
        print(i)
        i += 1
    j += 1

