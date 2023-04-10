number=[]
while True:
    num= int(input())
    if num == 0:
        break
    number.append(num)
for x in reversed(number):
    print(x)
    
'''
n= int(input())
list=[]
list.append(n)
while n!=0:
    n= int(input())
    list.append(n)
list.remove(0)
for x in reversed(list):
     print(x)

'''