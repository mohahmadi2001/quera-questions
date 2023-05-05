array = []
string, result,opend = input(), 0, 0
for char in string:
     if char == "(":
          opend += 1
     else:
          if opend > 0:
               opend -=1
               result +=2
          else:
               array .append(result)
               result = 0
array.append(result)
print(max(array))