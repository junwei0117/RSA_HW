p=input("p = ")
P=int(p)
q=input("q = ")
Q=int(q)
N=P*Q
print("n =",N)
e=input("e = ")
E=int(e)

D=0
while True:
    if (E*D)%(P*Q-P-Q+1)==1:
        break
    else:
        D=D+1
print("d =",D)

plain=input("plain text = ")
Str=''
count=0

for i in range(len(plain)):
    if plain[i:i+1] == 'A':
        Str+='00'
    elif plain[i:i+1] == 'B':
        Str+='01'
    elif plain[i:i+1] == 'C':
        Str+='02'
    elif plain[i:i+1] == 'D':
        Str+='03'
    elif plain[i:i+1] == 'E':
        Str+='04'
    elif plain[i:i+1] == 'F':
        Str+='05'
    elif plain[i:i+1] == 'G':
        Str+='06'
    elif plain[i:i+1] == 'H':
        Str+='07'
    elif plain[i:i+1] == 'I':
        Str+='08'
    elif plain[i:i+1] == 'J':
        Str+='09'
    elif plain[i:i+1] == 'K':
        Str+='10'
    elif plain[i:i+1] == 'L':
        Str+='11'
    elif plain[i:i+1] == 'M':
        Str+='12'
    elif plain[i:i+1] == 'N':
        Str+='13'
    elif plain[i:i+1] == 'O':
        Str+='14'
    elif plain[i:i+1] == 'P':
        Str+='15'
    elif plain[i:i+1] == 'Q':
        Str+='16'
    elif plain[i:i+1] == 'R':
        Str+='17'
    elif plain[i:i+1] == 'S':
        Str+='18'
    elif plain[i:i+1] == 'T':
        Str+='19'
    elif plain[i:i+1] == 'U':
        Str+='20'
    elif plain[i:i+1] == 'V':
        Str+='21'
    elif plain[i:i+1] == 'W':
        Str+='22'
    elif plain[i:i+1] == 'X':
        Str+='23'
    elif plain[i:i+1] == 'Y':
        Str+='24'
    elif plain[i:i+1] == 'Z':
        Str+='25'
    elif plain[i:i+1] == ' ':
        Str+='26'
    count+=1

if len(Str)%2==1:
    Str+='00'
    
print("M =",Str)

a=0
c=''
for x in range(0,len(Str),4):
    a=int(Str[x:x+4])
    a=a**E
    a=a%(P*Q)
    c+=str(a).zfill(4)
    a=0
print("C =",c)

m=''
for y in range(0,len(c),4):
    a=int(c[y:y+4])
    a=a**D
    a=a%(P*Q)
    m+=str(a).zfill(4)
    a=0
print("After decoding : ")
print(m)
