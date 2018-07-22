a=int(raw_input())
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=(rev*10)+dig
    a=a//10
print rev
