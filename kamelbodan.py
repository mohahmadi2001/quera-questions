n = int(input())
list=[]
sum=0
for i in range(1,n+1):
    if n%i == 0:
        list.append(i)
list.remove(n)
for j in list:
    sum += j
if sum == n:
    print('YES')
else:
    print('NO')

