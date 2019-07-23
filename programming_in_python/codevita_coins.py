def change_base(num , base):
	rep = [int(i,base) for i in str(number)]
    rep.reverse()
    k = 0
    for i in range(len(rep)):
      k+=rep[i]*base**i
    return result
N = input.split()
array = []
result = []
for i in range(len(N)):
  array_object = N[i]
  temp = max(array_object)
  array_object_x = temp
  if ord(temp)>=49 and ord(temp) <=57:
    temp=int(array_object_x)+1
    array.append(temp)
  else:
    temp1 = ord(temp)
    temp2 = temp1 - 55
    temp2+=1
    array.append(temp)
for i in range(len(N)):
  array_object = change_base(N[i],result[i])
  result.append(array_object)
print(min(result))  
    
