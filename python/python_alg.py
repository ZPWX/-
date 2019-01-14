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
