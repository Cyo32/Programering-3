from PIL import Image
import pilgram

#finne fram til riktig bilde
img = Image.open('sample.jpg')

#Legg til filter og Lagre bilde
pilgram._1977(img).save('sample-_1977.jpg')

#importer bilde
img = Image.open('sample-_1977.jpg')

#vis bilde
img.show()