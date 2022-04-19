f=open("people.txt")
c=0
content=f.read()
colist=content.split("\n")
for i in colist:
    if i:
        c=c+1
print("this is the number of line in the file")
print(c)