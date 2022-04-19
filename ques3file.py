f=open("question3.txt","w")
colour=["red","yellow","white","black"]
i=0
while i<len(colour):
    print(colour[i])
    f.write("/n")
    i=i+1
f.close()