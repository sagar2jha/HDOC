seq = list(input().split())
lis = [1 for i in range(len(seq))]
sub_seq = []
for i in range(1,len(seq)):
	for j in range(i):
		if(seq[j]<seq[i] and lis[i]<lis[j]+1):
			lis[i] = lis[j]+1
print(max(lis))			
