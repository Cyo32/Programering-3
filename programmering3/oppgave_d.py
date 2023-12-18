from PIL import Image
import pilgram

image = Image.open('sample.jpg')
new_image = image.resize((1080,729))
new_image.save('sample_1080.jpg')