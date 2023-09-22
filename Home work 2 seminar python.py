
n = int(input('n = '))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    if x == 1:
        count_one += 1
    else: print()
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


s = int(input('s = '))
p = int(input('p = '))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число ="{x}", второе число ="{y}"')



n = int(input('Введи число N:'))
i = 0
while 2 ** i <= n:
    print(f' 2 в степени {i} равна {2 ** i}')
    i += 1

