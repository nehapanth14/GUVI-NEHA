a,b=map(int,raw_input("").split())
for num in range(a,b):
    temp=num
    s=0
    while(num>0):
        dig=temp%10
        s=s+(dig**3)
        temp=temp//10
    if(s==num):
        print num

        

        
