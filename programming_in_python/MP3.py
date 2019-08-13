import math
def countit(rang,arr):
    lis = []    
    for ran in rang:
        arr2 = arr.copy()
        count = 0
        for val in range(len(arr2)):
            if arr2[val] < ran[0]:
                arr2[val] = ran[0]
                count+=1
            if arr2[val] > ran[1]:
                arr2[val] = ran[1]
                count+=1
            if len(arr2)*math.ceil(math.log2(len(set(arr2)))) <= 8*i:         
                lis.append(count)
    return lis 

n,i = map(int,input().split())
arr = list(map(int,input().split()))
arr1 = arr.copy()
dummy = list(set(arr1))
dummy.sort()
rang = []

for distinct in range(2,int(math.pow(2,i))+1):
    for x in range(len(dummy)-distinct+1):
        l,r = dummy[x],dummy[x+distinct-1]
        rang.append((l,r))
lis = countit(rang,arr)        
if len(arr)*math.ceil(math.log2(len(set(arr)))) <= 8*i:
    lis.append(0)               
if len(countit(rang,arr)) is not 0:
    print(min(lis))
else:
    print(len(arr)-arr.count(max(arr)))    

        



