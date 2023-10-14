a = int(input())
x = a // 100
y = a % 10
z = a // 10 % 10
if max(x, y, z) - min(x, y, z) == x + y + z - max(x, y, z) - min(x, y, z):
    print('Число интересное')
else:
    print('Число неинтересное')
