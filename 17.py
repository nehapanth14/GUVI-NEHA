a=int(raw_input(""))
temp=a
s=0
while(a>0):
    n=a%10
    s=s+(n**3)
    a=a//10
if(temp==s):
    print"yes"
else:
    print"no"
        
