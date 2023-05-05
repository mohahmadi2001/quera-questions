x = input()
y = input()

a = int(x[::-1])
b = int(y[::-1])

if a > b:
    print(y, '<', x)
if a < b:
    print(x, '<', y)
if a == b:
    print(x, '=', y)
