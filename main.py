text="My Phone number is 8527272639, if u want to know anything about python you can contact me on"
"Phone" in text

import re
match="Phone"
a=re.search(match,text)
print(a)
print(a.span())

text="My phone once and my phone twice"
f="phone"
b=re.findall(f,text)
print(b)
print(len(b))

for s in re.finditer("phone",text):
    print(s.span())
    print(s.group())