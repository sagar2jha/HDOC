
def sudofibo(arr,array):
	if array[len(array)-2] + array[len(array)-1]  not in arr:
		return array
	else:
		array.append(array[len(array)-2] + array[len(array)-1])
		return sudofibo(arr,array)
def compare(arr):
	mx = 1
	for i in range(1,len(arr)):
		if len(arr[i])>mx: 
			mx = len(arr[i])
	for j in range(len(arr)):
		if len(arr[j]) == mx:
			return arr[j]

arr = list(map(int,input().split()))
array = [[]] 
arr.sort()
for i in range(len(arr)-2):
	for j in range(i+1,len(arr)):
		if arr[i] + arr[j] in arr:
			array.append([arr[i],arr[j],arr[i]+arr[j]])
for k in range(1,len(array)):
	sudofibo(arr,array[k])
print(compare(array))	


