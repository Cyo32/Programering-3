from PIL import Image
import pilgram

im = Image.open('sample.jpg')
pilgram.inkwell(im).save('sample-inkwell.jpg')
