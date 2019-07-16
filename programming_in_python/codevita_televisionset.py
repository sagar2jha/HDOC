import calendar
N = int(input())
R1 , R2 = map(int,input().split())
target = int(input())
iters = []
for x in range(1,13):
	(month_iterable,days_iterable) = (x,calendar.monthrange(2020,x))
	iters.append((month_iterable,days_iterable))
num_pat = []
for i in range(len(iters)):
	for y in range(1,int(iters[i][1][1])+1):
		num_pat.append((6-iters[i][1][0])**2 + abs(y-15))
possiblity = []
for k in range(N+1):
	possiblity.append((k,N-k))
money_possiblity = []
for columns in range(len(possiblity)):
	money_daily= []
	for rows in range(len(num_pat)):
		if (num_pat[rows]-N)>=0:
			money_daily.append(R1*possiblity[columns][0] + R2*possiblity[columns][1])
		else:
			if (num_pat[rows]<=possiblity[columns][1]):
				money_daily.append(R2*num_pat[rows])
			else:
				money_daily.append(R1*(num_pat[rows]-possiblity[columns][1]) + R2*possiblity[columns][1])
	money_possiblity.append(sum(money_daily))
final = []
for it in range(len(money_possiblity)):
	if (money_possiblity[it] >= target):
		final.append(money_possiblity[it])
if len(final) > 0:
	print(money_possiblity.index(min(final)))
else:
	print(N)	



			

	
		
