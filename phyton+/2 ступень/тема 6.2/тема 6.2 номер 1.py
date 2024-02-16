from PIL import Image
image = Image.open(input("-"))
width, height = image.size
pixels = image.load()
for x in range(width):
    for y in range(height):
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]
        pixels[x, y] = 255 - r, 255 - g, 255 - b
image.save('1_invert.jpg')

image.show()



