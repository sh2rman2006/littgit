from PIL import Image
image = Image.open(input("-"))
width, height = image.size
pixels = image.load()
for x in range(width):
    for y in range(height):
        r = pixels[x, y][0]
        g = pixels[x, y][1]
        b = pixels[x, y][2]
        sr = (r + g + b) // 3
        pixels[x, y] = sr, sr, sr

image.save('1_grey.jpg')

image.show()
for x in range(width):
    for y in range(height):
         r = pixels[x, y][0] # узнаём значение красного цвета пикселя
         g = pixels[x, y][1] # зелёного
         b = pixels[x, y][2] # синего
         sr = (r + g + b) // 3
         if sr>100:
             sr=255
         pixels[x, y] = sr, sr, sr

image.save('1_invert_grey_100.jpg')

image.show()
