a=int(raw_input(""))
fact=1
while a>0:
    if a==0:
        fact=1
        print fact
        break
    else:
        fact=fact*a
        a=a-1
print fact
