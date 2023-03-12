import random

IR,MAR,IBR,MBR,MQ,AC,PC=None,None,None,None,"0"*39+"1",None,0

base=random.randint(2,9)
exp=random.randint(0,5)

add1=random.randint(-100,100)
add2=random.randint(-100,100)

sub1=random.randint(-100,100)
sub2=random.randint(-100,100)

mul1=random.randint(-100,100)
mul2=random.randint(-100,100)

dividend=random.randint(1,100)
divisor=random.randint(1,10)

rdividend=random.randint(1,100)
rdivisor=random.randint(1,10) #arguments for finding remainder

print("Base: ",base)
print("Exp: ",exp)

print("Addition argument 1: ",add1)
print("Addition argument 2: ",add2)

print("Subtraction argument 1: ",sub1)
print("Subtraction argument 2: ",sub2)

print("Multiplication argument 1: ",mul1)
print("Multiplication argument 2: ",mul2)

print("Dividend: ",dividend)
print("Divisor: ",divisor)

print("Dividend for remainder: ", rdividend)
print("Divisor for remainder: ", rdivisor)

global memory
memory={}

#returns a binary string of length 40 corresponding to the number(>0) passed as argument
def getBinaryString(n):
    l=[]
    i=0
    if (n>=0):
        pos=n
    else:
        pos=2**39+n
    
    while (pos>0):
        rem=pos%2
        l.append(str(rem))
        pos=pos//2
        i+=1

    while (i<39):
        l.append(str(0))
        i+=1
    
    if (n>=0):
        l.append("0")
    else:
        l.append("1")
    
    l.reverse()
    
    str1=""
    
    for elem in l:
        str1+=elem
    
    return str1

def getBinaryString80(n):
    l=[]
    i=0
    if (n>=0):
        pos=n
    else:
        pos=2**79+n
    
    while (pos>0):
        rem=pos%2
        l.append(str(rem))
        pos=pos//2
        i+=1

    while (i<79):
        l.append(str(0))
        i+=1
    
    if (n>=0):
        l.append("0")
    else:
        l.append("1")
    
    l.reverse()
    
    str1=""
    
    for elem in l:
        str1+=elem
    
    return str1


def getNum40(s): #converts a binary string of length 40 to integer
    ans=0
    if s[0]=="0":
        for i in range(1, 40):
        
            if s[i]=='1':
                ans+=(2**(39-i))
    else:
        for i in range(1, 40):
            if s[i]=="1":
                ans+=(2**(39-i))
        ans-=2**39
    
    return ans


def getNum12(s): #converts a binary string of length 40 to integer
    ans=0
    if s[0]=="0":
        for i in range(1, 12):
        
            if s[i]=='1':
                ans+=(2**(11-i)) 
    else:
        for i in range(1, 12):
            if s[i]=="1":
                ans+=(2**(11-i))
        ans-=2**11
    return ans


sbase=getBinaryString(base)
sexp=getBinaryString(exp-1)

sadd1=getBinaryString(add1)
sadd2=getBinaryString(add2)

ssub1=getBinaryString(sub1)
ssub2=getBinaryString(sub2)

smul1=getBinaryString(mul1)
smul2=getBinaryString(mul2)

sdividend=getBinaryString(dividend)
sdivisor=getBinaryString(divisor)

srdividend=getBinaryString(rdividend)
srdivisor=getBinaryString(rdivisor)

#Instruction Set

#LOAD-> 00000001
#MUL-> 00001011
#SUB-> 00000110
#ADD-> 00000101
#STOR-> 00100001
#JUMP+M(X,0:19)-> 00001101
#LOAD MQ M(X)-> 00001001
#LOAD MQ -> 00001010
#DIV ->00001100
#HALT -> 00000000

memory[10]="0000100100000110010000001011000001100101" #LOAD M(100) MQ, MUL M(101)
memory[11]="0000101000000000000000100001000001100100" #LOAD MQ, STOR M(100)
memory[12]="0000000100000110011000000110000001100111" #LOAD M(102), SUB M(103) 
memory[13]="0010000100000110011000001101000000001010" #STOR M(102), JUMP+ M(0, 0:19)


memory[0]="0000000100000110100000000101000001101001" #LOAD M(104), ADD M(105)
memory[1]="00100001000001101010" #STOR M(106)

memory[2]="0000000100000110101100000110000001101100" #LOAD M(107), SUB M(108)
memory[3]="00100001000001101101" #STOR M(109)

memory[4]="0000100100000110111000001011000001101111" #LOAD MQ M(110), MUL M(111)
memory[5]="0000101000000000000000100001000001110000" #LOAD MQ, STOR M(112)

memory[6]="0000000100000111000100001100000001110010" #LOAD M(113), DIV M(114)
memory[7]="0000101000000000000000100001000001110011" #LOAD MQ, STOR M(115)

memory[8]="0000000100000111010000001100000001110101" #LOAD M(116), DIV M(117) 
memory[9]="00100001000001110110" #STOR M(118)

memory[14]="00000000000000000000" #HALT

#Values set
memory[100]="0000000000000000000000000000000000000001" #stores result, initially value 1, will later be incremented
memory[101]=sbase #stores the binary of the random base generated
memory[102]=sexp #stores the binary of the random exponent generated
memory[103]="0000000000000000000000000000000000000001" #stores the constant 1

memory[104]=sadd1 #stores argument 1 of addition
memory[105]=sadd2 #stores argument 2 of addition
memory[106]="0000000000000000000000000000000000000000" #initially zero, later stores result of addition

memory[107]=ssub1 #stores argument 1 of subtraction
memory[108]=ssub2 #stores argument 2 of subtraction
memory[109]="0000000000000000000000000000000000000000" #initially zero, later stores result of subtraction

memory[110]=smul1 #stores argument 1 of multiplication
memory[111]=smul2 #stores argument 2 of multiplication
memory[112]="0000000000000000000000000000000000000000" #initially zero, later stores result of multiplication

memory[113]=sdividend #stores dividend of division
memory[114]=sdivisor #stores divisor of division
memory[115]="0000000000000000000000000000000000000000" #initially zero, later stores quotient of division

memory[116]=srdividend
memory[117]=srdivisor
memory[118]="0000000000000000000000000000000000000000" #initially zero, later stores remainder of division

def fetch():
    global IBR, MAR, IR, MBR, PC, memory
    if (IBR!=None):
        IR=IBR[0:8]
        MAR=getNum12((IBR[8:]))
        PC+=1
        IBR=None

    else:
        MAR=PC
        MBR=memory[MAR]
        if len(MBR)==40:
            IBR=MBR[20:]
            IR=MBR[0:8]
            MAR=getNum12(MBR[8:20])
        elif len(MBR)==20:
            IBR=None
            IR=MBR[0:8]
            MAR=getNum12(MBR[8:20])
            PC+=1       

#LOAD-> 00000001
#MUL-> 00001011
#SUB-> 00000110
#ADD-> 00000101
#STOR-> 00100001
#JUMP+M(X,0:19)-> 00001101
#LOAD MQ M(X)-> 00001001
#LOAD MQ -> 00001010
#DIV M(X) ->00001100
#HALT -> 00000000

def decodeAndExecute():
    
    global IR,MAR,MBR,PC,AC,MQ,IBR,memory
    if IR=="00000001":
        #instruction LOAD
        MBR=memory[MAR]
        AC=MBR

    elif IR=="00001010":
        #instruction LOAD MQ
        AC=MQ

    elif IR=="00001001":
        #instruction LOAD MQ M(X)
        MBR=memory[MAR]
        MQ=MBR

    elif IR=="00000101":
        #instruction ADD
        temp1=getNum40(AC)
        temp2=getNum40(memory[MAR])
        temp=temp1+temp2
        AC=getBinaryString(temp)

    elif IR=="00000110":
        #instruction SUB
        temp1=getNum40(AC)
        temp2=getNum40(memory[MAR])
        temp=temp1-temp2
        
        AC=getBinaryString(temp)      
    
    elif IR=="00001011":
        #instruction MUL
        temp1=getNum40(MQ)
        temp2=getNum40(memory[MAR])
        temp=temp1*temp2
        AC=getBinaryString80(temp)[0:40]
        MQ=getBinaryString80(temp)[40:]
        
    
    elif IR=="00100001":
        #instruction STOR
        MBR=AC
        memory[MAR]=MBR
    
    elif IR=="00001101":
        #instruction JUMP+
        
        if (getNum40(AC)>=0):
            PC=MAR
        else:
            pass
        
    elif IR=="00001100":
        temp1=getNum40(AC)
        temp2=getNum40(memory[MAR])
        quot=temp1//temp2
        rem=temp1%temp2
        AC=getBinaryString(rem)
        MQ=getBinaryString(quot)

    elif IR=="00000000":
        PC=1000
        print("Result of power: ",getNum40(memory[100]))
        print("Result of addition: ",getNum40(memory[106]))
        print("Result of subtraction: ",getNum40(memory[109]))
        print("Result of multiplication: ",getNum40(memory[112]))
        print("Result of division: ",getNum40(memory[115]))
        print("Result of remainder:",getNum40(memory[118]))

while (PC<1000):
    
    fetch()
    decodeAndExecute()