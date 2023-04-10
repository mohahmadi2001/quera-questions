a,b,l= [int(x) for x in input().split()]
sum = l //2*(a  + b)
if l % 2 != 0:
    sum += a

print(int(sum))

