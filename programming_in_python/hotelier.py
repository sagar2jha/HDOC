n = input()
string = input()
result = ['0']*10
res = ""
for x in string:
	if x is 'L':
		for i in range(0,10):
			if result[i] == '0':
				result[i] = '1'
				break
	elif x is 'R':
		for j in range(0,10):
			if result[9-j] == '0':
				result[9-j] = '1'
				break
	else:
		result[int(x)] = '0'
print(res.join(result))	

		
