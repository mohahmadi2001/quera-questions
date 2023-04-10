x, y, z = input().split()
rec = int(x) + int(y) + int(z)
if int(x) == 0 or int(y) == 0 or int(z) == 0:
    print('No')
elif rec == 180:
    print('Yes')
else:
    print('No')
