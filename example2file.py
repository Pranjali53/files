my_file=open("people.txt","r")
i=0
c=0
while i<len(my_file):
    my_file.readline()
    c=c+1
i=i+1
print(c)
    