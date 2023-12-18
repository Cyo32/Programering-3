from PIL import Image
import pilgram

#importer bilde
from PIL import Image
image = Image.open('sample.jpg')

#alternativ måte å importere bilder på
with Image.open('sample.jpg') as image:
    image.show()

#Lage et bilde fra start
image_blank = Image.new('RGBA',(1000,600))
image_blank.show()

#vis bilde
image.show()

#Lagre bilde
image.save('test_save.png')

#Innformasjon om bildet
print (image.size)
print (image.format)
print (image.format_description)