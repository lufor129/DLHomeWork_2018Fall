from PIL import Image
im = Image.open("./westbrook.jpg");
pixelMap = im.load()

img = Image.new(im.mode,im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        temp = pixelMap[i,j]
        pixelsNew[i,j] = (int(temp[0]/2),int(temp[1]/2),int(temp[2]/2))
img.save("reverse.jpg")