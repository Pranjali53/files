f=open("people.txt")
print("people.txt","w")
for i in f:
    if "delhi" in i:
        f1=open("delhi.txt","a")
        f1.write(i)
    if "shimla" in i:
        f2=open("shimla.txt","a")
        f2.write(i)
    if "delhi"not in i and "shimla" not in i:
        f3=open("others.txt","a")
        f3.write(i)
        