from PIL import Image
win=Image.open('image.jpg')
#win.show()
print(win.size)
x=0
y=0
w=1920/3
h=1080/10
m = win.crop((x,y,w,h))
m.show()