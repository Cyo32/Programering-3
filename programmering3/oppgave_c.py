from PIL import Image
import pilgram


image = Image.open('sample.jpg')

rotate = image.rotate(90)

rotate.show()