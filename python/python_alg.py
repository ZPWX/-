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
        print(i,end="-")
    i += 1
