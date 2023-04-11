from PIL import Image

joseph = Image.open('joseph_pic.jpg')
#joseph.show()

n,p = joseph.size

def f(x,y):
    return joseph.getpixel((i,j))
