#File Writing
"""
f= open("Abhijeet2.txt","a")
f.write("\nAbhijeet is not so tall")
f.close()
"""

f=open("Abhijeet2.txt","r+")
print(f.read())
f.write("\nThank you")