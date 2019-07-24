
def parantheses(instr):
    paran = {'{' : '}','(' : ')','[' : ']'}
    outstr = []
    for i in range(len(instr)):
        if instr[i] in paran.keys():
            k=i
            outstr.append(instr[i])   
        elif instr[i] == paran[instr[k]]:    
            outstr.remove(list(paran.keys())[list(paran.values()).index(instr[i])])    
            k-=1
        else:
            return i+1    
    if len(outstr) == 0:
        return 0
    else:
        return len(instr)+1

ins = input()
print(parantheses(ins))
