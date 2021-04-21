#File Reading and wrting
f=open("Abhijeet.txt","r")
for line in f :
    print(line)

#content = f.read(3)
content = f.read()
print(content)
f.close()